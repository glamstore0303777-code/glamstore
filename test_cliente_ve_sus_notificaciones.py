#!/usr/bin/env python
"""
Test: Verificar que el cliente ve sus notificaciones reportadas
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.test import Client, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from core.Clientes.views import notificaciones_cliente
from core.models import Cliente, Pedido, NotificacionProblema, Usuario

print("\n" + "="*70)
print("TEST: CLIENTE VE SUS NOTIFICACIONES REPORTADAS")
print("="*70)

# 1. Obtener un cliente con notificaciones
print("\n1. Buscando cliente con notificaciones...")
cliente = Cliente.objects.filter(
    pedido__notificacionproblema__isnull=False
).distinct().first()

if not cliente:
    print("   ✗ No hay clientes con notificaciones")
    exit(1)

print(f"   ✓ Cliente encontrado: {cliente.nombre} (ID: {cliente.idCliente})")

# 2. Obtener sus notificaciones
print("\n2. Obteniendo notificaciones del cliente...")
notificaciones = NotificacionProblema.objects.filter(
    idPedido__idCliente=cliente
).select_related('idPedido', 'idPedido__idCliente')

print(f"   Total: {notificaciones.count()}")
for notif in notificaciones:
    print(f"   - Notif #{notif.idNotificacion}: Pedido #{notif.idPedido.idPedido}")

# 3. Simular una solicitud con cliente_id en sesión
print("\n3. Simulando solicitud con cliente_id en sesión...")
factory = RequestFactory()
request = factory.get('/notificaciones_cliente/')

# Agregar sesión
middleware = SessionMiddleware(lambda x: None)
middleware.process_request(request)
request.session['cliente_id'] = cliente.idCliente
request.session.save()

# Llamar a la vista
try:
    response = notificaciones_cliente(request)
    print(f"   ✓ Vista ejecutada correctamente")
    print(f"   Status: {response.status_code}")
    
    # Verificar contexto
    if hasattr(response, 'context_data'):
        context = response.context_data
        print(f"\n4. Contexto de la respuesta:")
        print(f"   - cliente: {context.get('cliente', 'N/A')}")
        print(f"   - notificaciones: {len(context.get('notificaciones', []))} notificaciones")
        
        for notif in context.get('notificaciones', []):
            print(f"     * Notif #{notif.idNotificacion}: {notif.motivo[:50]}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    import traceback
    traceback.print_exc()

# 4. Verificar que el contexto tiene las notificaciones
print("\n4. Verificando contexto de la respuesta:")
if hasattr(response, 'context_data'):
    context = response.context_data
    notificaciones_en_contexto = context.get('notificaciones', [])
    print(f"   - Notificaciones en contexto: {len(notificaciones_en_contexto)}")
    
    if len(notificaciones_en_contexto) > 0:
        print(f"   ✓ El cliente VE sus notificaciones")
        for notif in notificaciones_en_contexto:
            print(f"     * Notif #{notif.idNotificacion}: {notif.motivo[:50]}")
    else:
        print(f"   ✗ El cliente NO ve sus notificaciones")

print("\n" + "="*70)
print("FIN DEL TEST")
print("="*70 + "\n")
