from django.db import transaction
from core.models import LoteProducto, MovimientoProducto, MovimientoLote
from decimal import Decimal
from datetime import datetime

class LotesService:
    """
    Servicio para manejar la lógica de lotes con trazabilidad FIFO
    """
    
    @staticmethod
    def crear_lote_entrada(producto, codigo_lote, cantidad, costo_unitario, 
                          fecha_vencimiento=None, total_con_iva=None, iva=None, 
                          proveedor=None, descripcion=""):
        """
        Crea un nuevo lote o actualiza uno existente cuando hay una entrada de producto
        """
        # Validar producto antes de hacer nada
        if not producto:
            raise ValueError("Producto no puede ser None")
        
        # Obtener el ID del producto de forma segura
        producto_id = None
        if hasattr(producto, 'idProducto'):
            producto_id = producto.idProducto
        elif hasattr(producto, 'id'):
            producto_id = producto.id
        
        if not producto_id:
            raise ValueError(f"Producto inválido o sin ID: {producto}")
        
        # Recargar el producto desde la BD para asegurar que tiene ID válido
        from core.models import Producto
        try:
            producto_db = Producto.objects.get(idProducto=producto_id)
            if not producto_db or not producto_db.idProducto:
                raise ValueError(f"Producto cargado pero sin ID válido: {producto_db}")
        except Producto.DoesNotExist:
            raise ValueError(f"Producto con ID {producto_id} no existe en la BD")
        except Exception as e:
            raise ValueError(f"Error al cargar producto: {str(e)}")
        
        with transaction.atomic():
            # Buscar si ya existe un lote con el mismo código para este producto
            lote_existente = LoteProducto.objects.filter(
                producto=producto_db,
                codigo_lote=codigo_lote
            ).first()
            
            if lote_existente:
                # Actualizar el lote existente
                lote_existente.cantidad_inicial += cantidad
                lote_existente.cantidad_disponible += cantidad
                if fecha_vencimiento:
                    lote_existente.fecha_vencimiento = fecha_vencimiento
                if costo_unitario:
                    lote_existente.costo_unitario = costo_unitario
                    lote_existente.precio_venta = costo_unitario * Decimal('1.25')
                if total_con_iva:
                    lote_existente.total_con_iva = (lote_existente.total_con_iva or 0) + total_con_iva
                if iva:
                    lote_existente.iva = (lote_existente.iva or 0) + iva
                if proveedor:
                    lote_existente.proveedor = proveedor
                lote_existente.save()
                lote = lote_existente
            else:
                # Validar que producto_db sea válido antes de crear el lote
                if not producto_db or not producto_db.idProducto:
                    raise ValueError(f"No se puede crear lote: producto_db inválido o sin ID")
                
                # Crear nuevo lote - usar producto_db en lugar de producto
                lote = LoteProducto.objects.create(
                    producto=producto_db,
                    codigo_lote=codigo_lote,
                    fecha_vencimiento=fecha_vencimiento,
                    cantidad_inicial=cantidad,
                    cantidad_disponible=cantidad,
                    costo_unitario=costo_unitario,
                    precio_venta=costo_unitario * Decimal('1.25'),  # +25%
                    total_con_iva=total_con_iva,
                    iva=iva,
                    proveedor=proveedor
                )
            
            # Crear el movimiento de producto - usar producto_db
            stock_anterior = producto_db.stock
            stock_nuevo = stock_anterior + cantidad
            
            movimiento = MovimientoProducto.objects.create(
                producto=producto_db,
                tipo_movimiento='AJUSTE_MANUAL_ENTRADA',
                cantidad=cantidad,
                precio_unitario=costo_unitario,
                costo_unitario=costo_unitario,
                stock_anterior=stock_anterior,
                stock_nuevo=stock_nuevo,
                lote=codigo_lote,
                total_con_iva=total_con_iva,
                iva=iva,
                descripcion=descripcion
            )
            
            # Actualizar stock del producto - usar producto_db
            producto_db.stock = stock_nuevo
            producto_db.save()
            
            return lote, movimiento
    
    @staticmethod
    def procesar_salida_fifo(producto, cantidad_salida, id_pedido=None, descripcion=""):
        """
        Procesa una salida de producto usando lógica FIFO
        Retorna una lista de movimientos creados con sus lotes de origen
        """
        movimientos_creados = []
        cantidad_restante = cantidad_salida
        
        with transaction.atomic():
            # Obtener lotes disponibles ordenados por FIFO (fecha de entrada)
            lotes_disponibles = LoteProducto.objects.filter(
                producto=producto,
                cantidad_disponible__gt=0
            ).order_by('fecha_entrada')
            
            if not lotes_disponibles.exists():
                raise ValueError(f"No hay lotes disponibles para el producto {producto.nombreProducto}")
            
            stock_anterior = producto.stock
            
            for lote in lotes_disponibles:
                if cantidad_restante <= 0:
                    break
                
                # Determinar cuánto tomar de este lote
                cantidad_a_tomar = min(cantidad_restante, lote.cantidad_disponible)
                
                # Crear movimiento de producto
                movimiento = MovimientoProducto.objects.create(
                    producto=producto,
                    tipo_movimiento='SALIDA_VENTA',
                    cantidad=cantidad_a_tomar,
                    precio_unitario=lote.costo_unitario,
                    costo_unitario=lote.costo_unitario,
                    stock_anterior=stock_anterior,
                    stock_nuevo=stock_anterior - cantidad_a_tomar,
                    id_pedido=id_pedido,
                    lote=lote.codigo_lote,
                    lote_origen=lote,
                    descripcion=descripcion
                )
                
                # Crear movimiento de lote para trazabilidad
                MovimientoLote.objects.create(
                    lote=lote,
                    movimiento_producto=movimiento,
                    cantidad=cantidad_a_tomar
                )
                
                # Actualizar lote
                lote.cantidad_disponible -= cantidad_a_tomar
                lote.save()
                
                # Actualizar stock del producto
                stock_anterior -= cantidad_a_tomar
                
                movimientos_creados.append(movimiento)
                cantidad_restante -= cantidad_a_tomar
            
            if cantidad_restante > 0:
                raise ValueError(f"No hay suficiente stock en lotes. Faltaron {cantidad_restante} unidades")
            
            # Actualizar stock final del producto
            producto.stock = stock_anterior
            producto.save()
            
            return movimientos_creados
    
    @staticmethod
    def obtener_trazabilidad_producto(producto):
        """
        Obtiene la trazabilidad completa de un producto mostrando todos los lotes
        """
        lotes = LoteProducto.objects.filter(producto=producto).order_by('fecha_entrada')
        
        trazabilidad = []
        for lote in lotes:
            movimientos_salida = MovimientoLote.objects.filter(lote=lote).select_related('movimiento_producto')
            
            trazabilidad.append({
                'lote': lote,
                'movimientos_salida': movimientos_salida,
                'cantidad_usada': lote.cantidad_inicial - lote.cantidad_disponible,
                'porcentaje_usado': lote.porcentaje_usado
            })
        
        return trazabilidad
    
    @staticmethod
    def obtener_lotes_por_vencer(dias=30):
        """
        Obtiene lotes que están próximos a vencer
        """
        from django.utils import timezone
        from datetime import timedelta
        
        fecha_limite = timezone.now().date() + timedelta(days=dias)
        
        return LoteProducto.objects.filter(
            fecha_vencimiento__lte=fecha_limite,
            cantidad_disponible__gt=0
        ).order_by('fecha_vencimiento')