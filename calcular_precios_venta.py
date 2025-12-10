#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Producto
from decimal import Decimal

print("Calculando precios de venta para todos los productos...")
print("="*60)

productos = Producto.objects.all()
print(f"Total de productos: {productos.count()}\n")

actualizados = 0
sin_precio = 0

for producto in productos:
    # Calcular precio_venta
    if producto.precio:
        precio_decimal = Decimal(str(producto.precio)) if not isinstance(producto.precio, Decimal) else producto.precio
        precio_calculado = float(precio_decimal * Decimal('1.19') * Decimal('1.06'))
        precio_redondeado = round(precio_calculado / 50) * 50
        precio_venta = int(precio_redondeado)
        
        # Actualizar si es diferente
        if producto.precio_venta != precio_venta:
            producto.precio_venta = precio_venta
            producto.save()
            print(f"✓ {producto.nombreProducto}")
            print(f"  Costo: ${producto.precio} → Venta: ${precio_venta}")
            actualizados += 1
        else:
            print(f"✓ {producto.nombreProducto} (ya actualizado)")
    else:
        print(f"✗ {producto.nombreProducto} (sin precio de costo)")
        sin_precio += 1

print("\n" + "="*60)
print(f"Resumen:")
print(f"  Actualizados: {actualizados}")
print(f"  Sin precio de costo: {sin_precio}")
print(f"  Total procesados: {actualizados + sin_precio}")
print("="*60)
