#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto, MovimientoProducto, LoteProducto
from django.db import connection

print("=" * 80)
print("DIAGNÓSTICO DE MOVIMIENTOS Y DETALLES DE PRODUCTOS")
print("=" * 80)

# 1. Verificar tablas
print("\n1. VERIFICAR TABLAS EN BD:")
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' 
        AND name IN ('productos', 'movimientos_producto', 'lote_producto')
    """)
    tablas = cursor.fetchall()
    for tabla in tablas:
        print(f"   ✓ Tabla {tabla[0]} existe")

# 2. Contar registros
print("\n2. CONTAR REGISTROS:")
print(f"   Productos: {Producto.objects.count()}")
print(f"   Movimientos: {MovimientoProducto.objects.count()}")
print(f"   Lotes: {LoteProducto.objects.count()}")

# 3. Verificar estructura de MovimientoProducto
print("\n3. ESTRUCTURA DE MOVIMIENTOPRODUCTO:")
print(f"   Campos: {[f.name for f in MovimientoProducto._meta.get_fields()]}")

# 4. Verificar si hay errores en las vistas
print("\n4. VERIFICAR VISTAS:")
try:
    from core.Gestion_admin.views import movimientos_producto_view, producto_detalle_view
    print("   ✓ Vistas importadas correctamente")
except Exception as e:
    print(f"   ✗ Error al importar vistas: {e}")

# 5. Crear un producto de prueba
print("\n5. CREAR PRODUCTO DE PRUEBA:")
try:
    from core.models import Categoria
    cat = Categoria.objects.first()
    if not cat:
        cat = Categoria.objects.create(nombreCategoria="Test")
    
    prod = Producto.objects.create(
        nombreProducto="Producto Test",
        precio=100,
        stock=10,
        idCategoria=cat
    )
    print(f"   ✓ Producto creado: {prod.nombreProducto} (ID: {prod.idProducto})")
    
    # Crear movimiento de prueba
    mov = MovimientoProducto.objects.create(
        producto=prod,
        tipo_movimiento='ENTRADA_INICIAL',
        cantidad=10,
        stock_anterior=0,
        stock_nuevo=10,
        precio_unitario=100,
        costo_unitario=100
    )
    print(f"   ✓ Movimiento creado: {mov.idMovimiento}")
    
except Exception as e:
    print(f"   ✗ Error al crear datos de prueba: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
print("DIAGNÓSTICO COMPLETADO")
print("=" * 80)
