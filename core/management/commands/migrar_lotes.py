from django.core.management.base import BaseCommand
from core.models import MovimientoProducto, LoteProducto, Producto
from decimal import Decimal
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Migra movimientos existentes para crear lotes retroactivos'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando migración de lotes...')
        
        # Obtener todos los productos
        productos = Producto.objects.all()
        
        for producto in productos:
            self.stdout.write(f'Procesando producto: {producto.nombreProducto}')
            
            # Obtener movimientos de entrada que no tienen lote_origen
            movimientos_entrada = MovimientoProducto.objects.filter(
                producto=producto,
                tipo_movimiento__contains='ENTRADA'
            ).order_by('fecha')
            
            lote_counter = 1
            
            for movimiento in movimientos_entrada:
                if movimiento.lote:
                    codigo_lote = movimiento.lote
                else:
                    codigo_lote = f"LOTE-{producto.idProducto}-{lote_counter:03d}"
                    lote_counter += 1
                
                # Verificar si ya existe el lote
                lote_existente = LoteProducto.objects.filter(
                    producto=producto,
                    codigo_lote=codigo_lote
                ).first()
                
                if not lote_existente:
                    # Crear lote retroactivo
                    lote = LoteProducto.objects.create(
                        producto=producto,
                        codigo_lote=codigo_lote,
                        fecha_entrada=movimiento.fecha,
                        fecha_vencimiento=movimiento.fecha_vencimiento,
                        cantidad_inicial=movimiento.cantidad,
                        cantidad_disponible=0,  # Inicialmente 0, se calculará después
                        costo_unitario=movimiento.costo_unitario or movimiento.precio_unitario or 0,
                        precio_venta=(movimiento.costo_unitario or movimiento.precio_unitario or 0) * Decimal('1.25'),
                        total_con_iva=movimiento.total_con_iva,
                        iva=movimiento.iva,
                        proveedor="Migración automática"
                    )
                    
                    # Actualizar el movimiento para referenciar el lote
                    movimiento.lote = codigo_lote
                    movimiento.save()
                    
                    self.stdout.write(f'  Creado lote: {codigo_lote}')
            
            # Ahora procesar las salidas y asignarlas a lotes usando FIFO
            self.asignar_salidas_a_lotes(producto)
        
        self.stdout.write(self.style.SUCCESS('Migración completada exitosamente'))
    
    def asignar_salidas_a_lotes(self, producto):
        """Asigna las salidas existentes a lotes usando lógica FIFO"""
        
        # Obtener todos los lotes del producto ordenados por fecha (FIFO)
        lotes = LoteProducto.objects.filter(producto=producto).order_by('fecha_entrada')
        
        # Resetear cantidad disponible de todos los lotes
        for lote in lotes:
            lote.cantidad_disponible = lote.cantidad_inicial
            lote.save()
        
        # Obtener movimientos de salida ordenados por fecha
        movimientos_salida = MovimientoProducto.objects.filter(
            producto=producto,
            tipo_movimiento__contains='SALIDA'
        ).order_by('fecha')
        
        for movimiento in movimientos_salida:
            cantidad_restante = movimiento.cantidad
            
            # Buscar lotes disponibles para esta salida
            for lote in lotes:
                if cantidad_restante <= 0:
                    break
                
                if lote.cantidad_disponible > 0:
                    # Determinar cuánto tomar de este lote
                    cantidad_a_tomar = min(cantidad_restante, lote.cantidad_disponible)
                    
                    # Si es la primera asignación a este movimiento, actualizar el lote_origen
                    if not movimiento.lote_origen:
                        movimiento.lote_origen = lote
                        movimiento.lote = lote.codigo_lote
                        movimiento.fecha_vencimiento = lote.fecha_vencimiento
                        movimiento.save()
                    
                    # Reducir cantidad disponible del lote
                    lote.cantidad_disponible -= cantidad_a_tomar
                    lote.save()
                    
                    cantidad_restante -= cantidad_a_tomar
                    
                    self.stdout.write(f'  Asignado {cantidad_a_tomar} unidades del lote {lote.codigo_lote} al movimiento {movimiento.idMovimiento}')
            
            if cantidad_restante > 0:
                self.stdout.write(self.style.WARNING(f'  No se pudo asignar {cantidad_restante} unidades del movimiento {movimiento.idMovimiento}'))