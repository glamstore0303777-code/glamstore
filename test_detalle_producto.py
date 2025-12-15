#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto, MovimientoProducto, LoteProducto
from django.db.models import Sum

print("Intentando obtener detalle de producto...")
try:
    # Obtener el primer producto
    producto = Producto.objects.first()
    
    if not producto:
        print("No hay productos en la BD")
    else:
        print(f"Producto: {producto.nombreProducto}")
        
        # Obtener movimientos recientes
        movimientos_recientes = MovimientoProducto.objects.filter(
            producto=producto
        ).order_by('-fecha')[:5]
        print(f"✓ Movimientos recientes: {movimientos_recientes.count()}")
        
        # Obtener lote activo
        lote_activo = LoteProducto.objects.filter(
            producto=producto,
            cantidad_disponible__gt=0
        ).order_by('fecha_entrada').first()
        print(f"✓ Lote activo: {lote_activo}")
        
        # Calcular estadísticas
        total_entradas = MovimientoProducto.objects.filter(
            producto=producto,
            tipo_movimiento__in=['ENTRADA_INICIAL', 'AJUSTE_MANUAL_ENTRADA']
        ).aggregate(total=Sum('cantidad'))['total'] or 0
        print(f"✓ Total entradas: {total_entradas}")
        
        total_salidas = MovimientoProducto.objects.filter(
            producto=producto,
            tipo_movimiento__in=['SALIDA_VENTA', 'AJUSTE_MANUAL_SALIDA']
        ).aggregate(total=Sum('cantidad'))['total'] or 0
        print(f"✓ Total salidas: {total_salidas}")
        
        print("\n✓ Vista debería funcionar correctamente")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
