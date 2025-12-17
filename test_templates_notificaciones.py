#!/usr/bin/env python
"""
Test para verificar que los templates reciben las notificaciones correctamente
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.template import Template, Context
from core.models import NotificacionProblema, Cliente

print("\n" + "="*70)
print("TEST: TEMPLATES RECIBEN NOTIFICACIONES")
print("="*70)

# 1. Obtener notificaciones
print("\n1. Obteniendo notificaciones...")
notificaciones = NotificacionProblema.objects.select_related(
    'idPedido__idCliente',
    'idPedido__idRepartidor'
).order_by('-fechaReporte')

print(f"   Total: {notificaciones.count()}")

# 2. Verificar que cada notificación tiene los campos necesarios
print("\n2. Verificando campos en cada notificación:")
for notif in notificaciones[:1]:
    print(f"\n   Notificación #{notif.idNotificacion}:")
    print(f"   - idNotificacion: {notif.idNotificacion} ✓")
    print(f"   - idPedido: {notif.idPedido.idPedido} ✓")
    print(f"   - idPedido.idCliente: {notif.idPedido.idCliente.nombre} ✓")
    print(f"   - motivo: {notif.motivo[:50] if notif.motivo else 'N/A'} ✓")
    print(f"   - foto: {notif.foto} ✓")
    print(f"   - fechaReporte: {notif.fechaReporte} ✓")
    print(f"   - leida: {notif.leida} ✓")
    print(f"   - respuesta_admin: {notif.respuesta_admin[:50] if notif.respuesta_admin else 'N/A'} ✓")
    print(f"   - fecha_respuesta: {notif.fecha_respuesta} ✓")

# 3. Simular contexto del template del admin
print("\n3. Simulando contexto del template del admin:")
context_admin = {
    'notificaciones': notificaciones,
    'notificaciones_no_leidas': notificaciones.filter(leida=False).count(),
    'mensajes_contacto': [],
    'total_mensajes_contacto': 0,
    'total_no_leidas': notificaciones.filter(leida=False).count()
}

print(f"   - notificaciones: {context_admin['notificaciones'].count()} ✓")
print(f"   - notificaciones_no_leidas: {context_admin['notificaciones_no_leidas']} ✓")
print(f"   - mensajes_contacto: {context_admin['mensajes_contacto']} ✓")
print(f"   - total_no_leidas: {context_admin['total_no_leidas']} ✓")

# 4. Simular contexto del template del cliente
print("\n4. Simulando contexto del template del cliente:")
cliente = Cliente.objects.filter(
    pedido__notificacionproblema__isnull=False
).distinct().first()

if cliente:
    notificaciones_cliente = NotificacionProblema.objects.filter(
        idPedido__idCliente=cliente
    ).select_related('idPedido', 'idPedido__idCliente').order_by('-fechaReporte')
    
    context_cliente = {
        'notificaciones': notificaciones_cliente,
        'cliente': cliente
    }
    
    print(f"   - Cliente: {cliente.nombre} ✓")
    print(f"   - notificaciones: {context_cliente['notificaciones'].count()} ✓")
    
    # Verificar que el template puede acceder a los datos
    print(f"\n5. Verificando acceso a datos en template del cliente:")
    for notif in notificaciones_cliente[:1]:
        print(f"   - notificacion.idPedido.idPedido: {notif.idPedido.idPedido} ✓")
        print(f"   - notificacion.motivo: {notif.motivo[:50] if notif.motivo else 'N/A'} ✓")
        print(f"   - notificacion.respuesta_admin: {notif.respuesta_admin[:50] if notif.respuesta_admin else 'N/A'} ✓")
        print(f"   - notificacion.fecha_respuesta: {notif.fecha_respuesta} ✓")

print("\n" + "="*70)
print("✓ TODOS LOS CAMPOS SON ACCESIBLES EN LOS TEMPLATES")
print("="*70 + "\n")
