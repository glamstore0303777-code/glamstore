#!/usr/bin/env python
"""
Script para probar la función reportar_problema_entrega
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.test import RequestFactory, Client
from django.contrib.sessions.middleware import SessionMiddleware
from core.Clientes.views import reportar_problema_entrega
from core.models import Cliente, Pedido, Usuario
from django.utils import timezone
from datetime import timedelta

print("\n" + "="*70)
print("PRUEBA: Función reportar_problema_entrega")
print("="*70)

# Crear cliente
cliente, _ = Cliente.objects.get_or_create(
    email='test_reportar@example.com',
    defaults={
        'nombre': 'Test',
        'apellido': 'User',
        'telefono': '3001234567',
        'direccion': 'Calle Test'
    }
)
print(f"\n✓ Cliente creado: {cliente.nombre} (ID: {cliente.idCliente})")

# Crear pedido
pedido, _ = Pedido.objects.get_or_create(
    idCliente=cliente,
    defaults={
        'total': 50000,
        'estado': 'Entregado',
        'estado_pedido': 'Entregado',
        'estado_pago': 'Pago Completo',
        'fechaCreacion': timezone.now() - timedelta(days=1),
        'fecha_vencimiento': timezone.now().date()
    }
)
print(f"✓ Pedido creado: #{pedido.idPedido}")

# Crear usuario
usuario, _ = Usuario.objects.get_or_create(
    email='test_user@example.com',
    defaults={
        'nombre': 'Test User',
        'password': 'test123',
        'id_rol': 3,
        'idCliente': cliente
    }
)
print(f"✓ Usuario creado: {usuario.nombre} (ID: {usuario.idUsuario})")

# Crear request con sesión
factory = RequestFactory()
request = factory.post(f'/reportar_problema/{pedido.idPedido}/', {
    'motivo': 'El producto llegó dañado',
})

# Agregar sesión
middleware = SessionMiddleware(lambda x: None)
middleware.process_request(request)
request.session.save()

# Agregar usuario a la sesión
request.session['usuario_id'] = usuario.idUsuario
request.session['usuario_nombre'] = usuario.nombre
request.session.save()

print(f"\n✓ Request creado con sesión")
print(f"  - usuario_id: {request.session.get('usuario_id')}")
print(f"  - cliente_id: {request.session.get('cliente_id')}")

# Probar la función
print(f"\n[PRUEBA] Llamando a reportar_problema_entrega...")
try:
    response = reportar_problema_entrega(request, pedido.idPedido)
    print(f"✓ Función ejecutada exitosamente")
    print(f"  - Status code: {response.status_code}")
    print(f"  - Tipo: {type(response).__name__}")
except Exception as e:
    print(f"✗ Error: {str(e)}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70 + "\n")
