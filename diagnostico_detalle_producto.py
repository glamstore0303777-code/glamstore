import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection
from core.models import Producto, MovimientoProducto, LoteProducto

print("=== DIAGNOSTICO DE DETALLE PRODUCTO ===\n")

# Verificar que la tabla de productos existe
print("1. Verificando tabla de productos...")
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM productos")
    count = cursor.fetchone()[0]
    print(f"   Total de productos: {count}")

# Verificar que la tabla de movimientos existe
print("\n2. Verificando tabla de movimientos...")
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM movimientos_producto")
    count = cursor.fetchone()[0]
    print(f"   Total de movimientos: {count}")

# Verificar que la tabla de lotes existe
print("\n3. Verificando tabla de lotes...")
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM lotes_producto")
    count = cursor.fetchone()[0]
    print(f"   Total de lotes: {count}")

# Obtener el primer producto
print("\n4. Obteniendo primer producto...")
producto = Producto.objects.first()
if producto:
    print(f"   Producto: {producto.nombreProducto} (ID: {producto.idProducto})")
    
    # Obtener movimientos
    print("\n5. Obteniendo movimientos recientes...")
    movimientos = MovimientoProducto.objects.filter(producto=producto).order_by('-fecha')[:5]
    print(f"   Total: {movimientos.count()}")
    for mov in movimientos:
        print(f"     - {mov.fecha}: {mov.tipo_movimiento} ({mov.cantidad})")
    
    # Obtener lote activo
    print("\n6. Obteniendo lote activo...")
    lote = LoteProducto.objects.filter(
        producto=producto,
        cantidad_disponible__gt=0
    ).order_by('fecha_entrada').first()
    if lote:
        print(f"   Lote: {lote.codigo_lote}")
        print(f"   Disponible: {lote.cantidad_disponible}")
    else:
        print("   No hay lotes disponibles")
else:
    print("   ERROR: No hay productos en la BD")

print("\n=== FIN DEL DIAGNOSTICO ===")
