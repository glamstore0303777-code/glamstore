#!/usr/bin/env python
"""
Script para diagnosticar por qué el admin solo ve mensajes de contacto
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import NotificacionProblema, MensajeContacto
from django.db import connection

print("\n" + "="*70)
print("DIAGNÓSTICO: NOTIFICACIONES DEL ADMIN")
print("="*70)

# 1. Verificar tabla de notificaciones_problema
print("\n1. TABLA notificaciones_problema:")
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM notificaciones_problema")
    count = cursor.fetchone()[0]
    print(f"   Total de registros: {count}")

# 2. Obtener todas las notificaciones
print("\n2. NOTIFICACIONES EN ORM:")
notificaciones = NotificacionProblema.objects.select_related(
    'idPedido__idCliente',
    'idPedido__idRepartidor'
).order_by('-fechaReporte')

print(f"   Total: {notificaciones.count()}")
for notif in notificaciones:
    print(f"\n   Notificación #{notif.idNotificacion}:")
    print(f"     - Pedido: #{notif.idPedido.idPedido}")
    print(f"     - Cliente: {notif.idPedido.idCliente.nombre}")
    print(f"     - Motivo: {notif.motivo[:50] if notif.motivo else 'Sin motivo'}")
    print(f"     - Leída: {notif.leida}")
    print(f"     - Respuesta: {notif.respuesta_admin[:50] if notif.respuesta_admin else 'Sin respuesta'}")
    print(f"     - Fecha respuesta: {notif.fecha_respuesta}")

# 3. Verificar mensajes de contacto
print("\n3. MENSAJES DE CONTACTO:")
try:
    mensajes = MensajeContacto.objects.all().order_by('-fecha')
    print(f"   Total: {mensajes.count()}")
    for msg in mensajes[:3]:
        print(f"   - {msg.nombre}: {msg.mensaje[:50]}")
except Exception as e:
    print(f"   Error: {e}")

# 4. Verificar que los campos existen en la BD
print("\n4. CAMPOS EN notificaciones_problema:")
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'notificaciones_problema'
        ORDER BY ordinal_position
    """)
    columns = cursor.fetchall()
    for col_name, col_type in columns:
        print(f"   - {col_name}: {col_type}")

print("\n" + "="*70)
print("FIN DEL DIAGNÓSTICO")
print("="*70 + "\n")
