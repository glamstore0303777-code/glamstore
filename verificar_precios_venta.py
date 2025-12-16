#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto
from decimal import Decimal

print("=" * 70)
print("VERIFICACIÓN Y ACTUALIZACIÓN DE PRECIOS DE VENTA")
print("=" * 70)

# Obtener todos los productos
todos_productos = Producto.objects.all()
print(f"\nTotal de productos en BD: {todos_productos.count()}")

# Contar productos con precio_venta = 0
sin_precio = todos_productos.filter(precio_venta=0)
print(f"Productos con precio_venta = 0: {sin_precio.count()}")

# Contar productos con precio = 0
sin_costo = todos_productos.filter(precio=0)
print(f"Productos con precio (costo) = 0: {sin_costo.count()}")

print("\n" + "-" * 70)
print("ACTUALIZANDO PRODUCTOS SIN PRECIO_VENTA...")
print("-" * 70)

actualizados = 0
errores = 0

for producto in sin_precio:
    try:
        if producto.precio and producto.precio > 0:
            nuevo_precio = producto.calcular_precio_venta()
            producto.precio_venta = nuevo_precio
            producto.save()
            print(f"✓ ID {producto.idProducto}: {producto.nombreProducto}")
            print(f"  Precio (costo): ${producto.precio} → Precio Venta: ${nuevo_precio}")
            actualizados += 1
        else:
            print(f"⚠ ID {producto.idProducto}: {producto.nombreProducto}")
            print(f"  No tiene precio (costo) definido")
    except Exception as e:
        print(f"✗ ID {producto.idProducto}: {producto.nombreProducto}")
        print(f"  Error: {str(e)}")
        errores += 1

print("\n" + "=" * 70)
print("RESUMEN")
print("=" * 70)
print(f"Productos actualizados: {actualizados}")
print(f"Errores: {errores}")
print(f"Total procesados: {actualizados + errores}")

# Verificación final
sin_precio_final = Producto.objects.filter(precio_venta=0)
print(f"\nProductos con precio_venta = 0 después de actualización: {sin_precio_final.count()}")

if sin_precio_final.count() > 0:
    print("\nProductos que aún tienen precio_venta = 0:")
    for p in sin_precio_final[:10]:
        print(f"  - ID {p.idProducto}: {p.nombreProducto} (precio: ${p.precio})")

print("=" * 70)
