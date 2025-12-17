#!/usr/bin/env python
"""
Test para verificar que el panel de admin muestra las notificaciones correctamente
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from core.models import NotificacionProblema

print("\n" + "="*70)
print("TEST: PANEL DE ADMIN - NOTIFICACIONES")
print("="*70)

# 1. Verificar que hay notificaciones
print("\n1. Verificando notificaciones en BD:")
notificaciones = NotificacionProblema.objects.all()
print(f"   Total: {notificaciones.count()}")

# 2. Crear un cliente de prueba
print("\n2. Creando cliente de prueba para simular admin...")
client = Client()

# 3. Simular una solicitud GET a /notificaciones/
print("\n3. Simulando solicitud GET a /notificaciones/:")
try:
    # Nota: Esta solicitud fallará porque no hay autenticación
    # Pero podemos ver si la URL existe
    response = client.get('/notificaciones/')
    print(f"   Status: {response.status_code}")
    
    if response.status_code == 302:
        print(f"   ℹ Redirigido a: {response.url}")
        print(f"   (Esperado: requiere autenticación)")
    elif response.status_code == 200:
        print(f"   ✓ Página cargada correctamente")
        # Verificar que contiene las notificaciones
        if 'Problemas de Entrega' in response.content.decode():
            print(f"   ✓ Sección 'Problemas de Entrega' encontrada")
        if 'Mensajes de Contacto' in response.content.decode():
            print(f"   ✓ Sección 'Mensajes de Contacto' encontrada")
    else:
        print(f"   ✗ Error: {response.status_code}")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "="*70)
print("FIN DEL TEST")
print("="*70 + "\n")
