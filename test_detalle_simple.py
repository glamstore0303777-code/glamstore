import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto, MovimientoProducto, LoteProducto
from django.db.models import Sum

try:
    print("Intentando obtener detalle de producto...")
    producto = Producto.objects.first()
    
    if not producto:
        print("ERROR: No hay productos en la BD")
    else:
        print(f"Producto: {producto.nombreProducto}")
        
        # Obtener movimientos recientes
        movimientos_recientes = MovimientoProducto.objects.filter(
            producto=producto
        ).order_by('-fecha')[:5]
        print(f"OK - Movimientos recientes: {movimientos_recientes.count()}")
        
        # Obtener lote activo
        lote_activo = LoteProducto.objects.filter(
            producto=producto,
            cantidad_disponible__gt=0
        ).order_by('fecha_entrada').first()
        print(f"OK - Lote activo: {lote_activo}")
        
        # Calcular estadísticas
        total_entradas = MovimientoProducto.objects.filter(
            producto=producto,
            tipo_movimiento__in=['ENTRADA_INICIAL', 'AJUSTE_MANUAL_ENTRADA']
        ).aggregate(total=Sum('cantidad'))['total'] or 0
        print(f"OK - Total entradas: {total_entradas}")
        
        total_salidas = MovimientoProducto.objects.filter(
            producto=producto,
            tipo_movimiento__in=['SALIDA_VENTA', 'AJUSTE_MANUAL_SALIDA']
        ).aggregate(total=Sum('cantidad'))['total'] or 0
        print(f"OK - Total salidas: {total_salidas}")
        
        print("\nTodo OK - Vista deberia funcionar")
        
except Exception as e:
    print(f"ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
