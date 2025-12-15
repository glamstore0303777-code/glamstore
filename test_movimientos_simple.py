import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto, MovimientoProducto

try:
    print("Intentando obtener movimientos...")
    producto = Producto.objects.first()
    
    if not producto:
        print("ERROR: No hay productos")
    else:
        print(f"Producto: {producto.nombreProducto}")
        
        # Obtener movimientos con defer para no cargar lote_origen
        movimientos = MovimientoProducto.objects.filter(
            producto=producto
        ).select_related('id_pedido').defer('lote_origen').order_by('-fecha')
        
        print(f"OK - Movimientos: {movimientos.count()}")
        for mov in movimientos[:3]:
            print(f"  - {mov.fecha}: {mov.tipo_movimiento}")
        
except Exception as e:
    print(f"ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
