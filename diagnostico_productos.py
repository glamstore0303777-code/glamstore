#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto

# Obtener todos los productos
productos = Producto.objects.all().order_by('-idProducto')[:10]

print("Últimos 10 productos:")
print("-" * 80)

for p in productos:
    print(f"ID: {p.idProducto} | Nombre: {p.nombreProducto}")
    print(f"  Precio (costo): {p.precio}")
    print(f"  Precio Venta: {p.precio_venta}")
    print(f"  Stock: {p.stock}")
    print()

# Buscar productos con precio_venta = 0
print("\n" + "=" * 80)
print("Productos con precio_venta = 0:")
print("=" * 80)

productos_sin_precio = Producto.objects.filter(precio_venta=0)
for p in productos_sin_precio:
    print(f"ID: {p.idProducto} | Nombre: {p.nombreProducto}")
    print(f"  Precio (costo): {p.precio}")
    print(f"  Precio Venta: {p.precio_venta}")
    
    # Recalcular
    if p.precio and p.precio > 0:
        nuevo_precio = p.calcular_precio_venta()
        print(f"  Nuevo precio calculado: {nuevo_precio}")
        p.precio_venta = nuevo_precio
        p.save()
        print(f"  ✓ Actualizado")
    print()
