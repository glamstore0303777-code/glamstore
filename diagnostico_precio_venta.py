#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto

# Buscar el producto "Bronceador trendy nn"
producto = Producto.objects.filter(nombreProducto__icontains='Bronceador trendy').first()

if producto:
    print(f"Producto encontrado: {producto.nombreProducto}")
    print(f"ID: {producto.idProducto}")
    print(f"Precio (costo): {producto.precio}")
    print(f"Precio Venta: {producto.precio_venta}")
    print(f"Stock: {producto.stock}")
    
    # Si el precio_venta es 0, recalcularlo
    if not producto.precio_venta or producto.precio_venta == 0:
        print("\nRecalculando precio_venta...")
        nuevo_precio = producto.calcular_precio_venta()
        print(f"Nuevo precio calculado: {nuevo_precio}")
        producto.precio_venta = nuevo_precio
        producto.save()
        print("✓ Guardado correctamente")
    else:
        print(f"\n✓ El precio_venta ya está calculado: ${producto.precio_venta}")
else:
    print("Producto no encontrado")
