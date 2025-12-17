#!/usr/bin/env python
"""
Script para probar que el admin puede ver las notificaciones correctamente
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.test import Client
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory
from core.Gestion_admin.views import notificaciones_view
from core.models import NotificacionProblema, Usuario

print("\n" + "="*70)
print("TEST: ADMIN VE NOTIFICACIONES")
print("="*70)

# 1. Verificar que hay notificaciones
print("\n1. Verificando notificaciones en BD:")
notificaciones = NotificacionProblema.objects.all()
print(f"   Total: {notificaciones.count()}")
for notif in notificaciones:
    print(f"   - Notif #{notif.idNotificacion}: Pedido #{notif.idPedido_id}")

# 2. Simular una solicitud del admin
print("\n2. Simulando solicitud del admin a /notificaciones/:")
factory = RequestFactory()
request = factory.get('/notificaciones/')

# Agregar sesión
middleware = SessionMiddleware(lambda x: None)
middleware.process_request(request)
request.session.save()

# Agregar usuario admin a la sesión
request.session['usuario_id'] = 1
request.session['usuario_nombre'] = 'Admin Test'
request.session['usuario_rol'] = 'Administrador'

# Llamar a la vista
try:
    response = notificaciones_view(request)
    print(f"   ✓ Vista ejecutada correctamente")
    print(f"   Status: {response.status_code}")
    
    # Verificar contexto
    if hasattr(response, 'context_data'):
        context = response.context_data
        print(f"\n3. Contexto de la respuesta:")
        print(f"   - notificaciones: {context.get('notificaciones', 'N/A')}")
        print(f"   - notificaciones_no_leidas: {context.get('notificaciones_no_leidas', 'N/A')}")
        print(f"   - mensajes_contacto: {context.get('mensajes_contacto', 'N/A')}")
        print(f"   - total_no_leidas: {context.get('total_no_leidas', 'N/A')}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
print("FIN DEL TEST")
print("="*70 + "\n")
