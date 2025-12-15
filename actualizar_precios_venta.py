#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto

# Obtener todos los productos con precio_venta = 0
productos_sin_precio = Producto.objects.filter(precio_venta=0)

print(f"Encontrados {productos_sin_precio.count()} productos sin precio_venta")
print("-" * 60)

actualizados = 0
for p in productos_sin_precio:
    if p.precio and p.precio > 0:
        nuevo_precio = p.calcular_precio_venta()
        p.precio_venta = nuevo_precio
        p.save()
        print(f"ID {p.idProducto}: {p.nombreProducto}")
        print(f"  Precio: {p.precio} -> Precio Venta: {p.precio_venta}")
        actualizados += 1

print("-" * 60)
print(f"Total actualizado: {actualizados} productos")
