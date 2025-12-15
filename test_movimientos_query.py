#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto, MovimientoProducto

print("Intentando obtener movimientos con select_related...")
try:
    # Obtener el primer producto
    producto = Producto.objects.first()
    
    if not producto:
        print("No hay productos en la BD")
    else:
        print(f"Producto: {producto.nombreProducto}")
        
        # Intentar la query con select_related
        movimientos = MovimientoProducto.objects.filter(
            producto=producto
        ).select_related('id_pedido', 'lote_origen').order_by('-fecha')
        
        print(f"✓ Query ejecutada correctamente")
        print(f"  Total: {movimientos.count()}")
        
        for mov in movimientos[:5]:
            print(f"  - {mov.idMovimiento}: {mov.tipo_movimiento}")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
