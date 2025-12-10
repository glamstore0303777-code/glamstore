from django.core.management.base import BaseCommand
from core.models import MovimientoProducto
from decimal import Decimal

class Command(BaseCommand):
    help = 'Actualiza los valores de IVA y Total con IVA en los movimientos existentes'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando actualización de movimientos...')
        
        # Obtener todos los movimientos que no tienen IVA calculado
        movimientos_sin_iva = MovimientoProducto.objects.filter(
            iva__isnull=True
        ) | MovimientoProducto.objects.filter(
            total_con_iva__isnull=True
        )
        
        total_movimientos = movimientos_sin_iva.count()
        self.stdout.write(f'Encontrados {total_movimientos} movimientos para actualizar')
        
        actualizados = 0
        errores = 0
        
        for movimiento in movimientos_sin_iva:
            try:
                # Solo actualizar movimientos de salida/venta
                if 'SALIDA' in movimiento.tipo_movimiento or 'VENTA' in movimiento.tipo_movimiento or 'PREPARACION' in movimiento.tipo_movimiento:
                    producto = movimiento.producto
                    
                    # Obtener el costo unitario
                    if movimiento.costo_unitario and movimiento.costo_unitario > 0:
                        costo_unitario = float(movimiento.costo_unitario)
                    elif movimiento.lote_origen and movimiento.lote_origen.costo_unitario:
                        costo_unitario = float(movimiento.lote_origen.costo_unitario)
                    elif producto.precio:
                        costo_unitario = float(producto.precio)
                    else:
                        costo_unitario = 0
                    
                    # Obtener el precio de venta
                    if movimiento.precio_unitario and movimiento.precio_unitario > 0:
                        precio_venta = float(movimiento.precio_unitario)
                    elif producto.precio_venta:
                        precio_venta = float(producto.precio_venta)
                    else:
                        # Calcular precio de venta: costo × 1.19 × 1.06
                        precio_venta = costo_unitario * 1.19 * 1.06
                    
                    # Calcular IVA (19% sobre el costo)
                    iva_por_unidad = costo_unitario * 0.19
                    iva_total = iva_por_unidad * movimiento.cantidad
                    
                    # Calcular total con IVA (precio de venta × cantidad)
                    total_con_iva = precio_venta * movimiento.cantidad
                    
                    # Actualizar el movimiento
                    movimiento.precio_unitario = int(precio_venta)
                    movimiento.costo_unitario = int(costo_unitario)
                    movimiento.iva = int(iva_total)
                    movimiento.total_con_iva = int(total_con_iva)
                    movimiento.save()
                    
                    actualizados += 1
                    
                    if actualizados % 10 == 0:
                        self.stdout.write(f'Actualizados {actualizados}/{total_movimientos}...')
                
            except Exception as e:
                errores += 1
                self.stdout.write(
                    self.style.ERROR(f'Error al actualizar movimiento {movimiento.idMovimiento}: {str(e)}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Actualización completada!')
        )
        self.stdout.write(f'  - Movimientos actualizados: {actualizados}')
        self.stdout.write(f'  - Errores: {errores}')
