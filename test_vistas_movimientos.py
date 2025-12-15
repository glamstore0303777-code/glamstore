#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.test import RequestFactory
from core.Gestion_admin.views import movimientos_producto_view, producto_detalle_view
from core.models import Producto, MovimientoProducto, Categoria
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import AnonymousUser

print("=" * 80)
print("TEST DE VISTAS: MOVIMIENTOS Y DETALLE PRODUCTO")
print("=" * 80)

# Crear datos de prueba
print("\n1. CREAR DATOS DE PRUEBA:")
cat = Categoria.objects.first() or Categoria.objects.create(nombreCategoria="Test")
prod = Producto.objects.create(
    nombreProducto="Producto Test 2",
    precio=100,
    stock=10,
    idCategoria=cat
)
print(f"   ✓ Producto creado: {prod.nombreProducto} (ID: {prod.idProducto})")

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

# Crear request factory
factory = RequestFactory()

# Test 1: movimientos_producto_view
print("\n2. TEST VISTA: movimientos_producto_view")
try:
    request = factory.get(f'/productos/movimientos/{prod.idProducto}/')
    request.user = AnonymousUser()
    request.session = {}
    
    # Agregar middleware de sesión
    middleware = SessionMiddleware(lambda x: None)
    middleware.process_request(request)
    request.session.save()
    
    response = movimientos_producto_view(request, prod.idProducto)
    print(f"   ✓ Vista ejecutada correctamente")
    print(f"   Status: {response.status_code if hasattr(response, 'status_code') else 'N/A'}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    import traceback
    traceback.print_exc()

# Test 2: producto_detalle_view
print("\n3. TEST VISTA: producto_detalle_view")
try:
    request = factory.get(f'/productos/detalle/{prod.idProducto}/')
    request.user = AnonymousUser()
    request.session = {}
    
    # Agregar middleware de sesión
    middleware = SessionMiddleware(lambda x: None)
    middleware.process_request(request)
    request.session.save()
    
    response = producto_detalle_view(request, prod.idProducto)
    print(f"   ✓ Vista ejecutada correctamente")
    print(f"   Status: {response.status_code if hasattr(response, 'status_code') else 'N/A'}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
print("TEST COMPLETADO")
print("=" * 80)
