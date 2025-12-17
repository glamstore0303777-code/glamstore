#!/usr/bin/env python
"""
Script para probar el flujo completo de notificaciones:
1. Cliente reporta un problema
2. Admin ve la notificación
3. Admin responde
4. Cliente ve la respuesta
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.utils import timezone
from core.models import Cliente, Pedido, NotificacionProblema, Usuario
from datetime import timedelta

print("\n" + "="*60)
print("PRUEBA COMPLETA DE NOTIFICACIONES")
print("="*60)

# 1. Crear un cliente de prueba
print("\n1. Creando cliente de prueba...")
cliente, created = Cliente.objects.get_or_create(
    email='test_notificaciones@example.com',
    defaults={
        'nombre': 'Cliente Test Notificaciones',
        'apellido': 'Test',
        'telefono': '3001234567',
        'direccion': 'Calle Test 123, Bogotá'
    }
)
print(f"   Cliente: {cliente.nombre} (ID: {cliente.idCliente})")

# 2. Crear un pedido de prueba
print("\n2. Creando pedido de prueba...")
pedido, created = Pedido.objects.get_or_create(
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
print(f"   Pedido: #{pedido.idPedido} - Total: ${pedido.total}")

# 3. Crear una notificación de problema
print("\n3. Creando notificación de problema...")
notificacion, created = NotificacionProblema.objects.get_or_create(
    idPedido=pedido,
    defaults={
        'motivo': 'El producto llegó dañado',
        'leida': False
    }
)
print(f"   Notificación: #{notificacion.idNotificacion}")
print(f"   Motivo: {notificacion.motivo}")
print(f"   Leída: {notificacion.leida}")

# 4. Verificar que se pueden acceder los campos
print("\n4. Verificando acceso a campos...")
try:
    print(f"   - respuesta_admin: {notificacion.respuesta_admin}")
    print(f"   - fecha_respuesta: {notificacion.fecha_respuesta}")
    print("   ✓ Campos accesibles correctamente")
except Exception as e:
    print(f"   ✗ Error al acceder a campos: {e}")

# 5. Admin responde a la notificación
print("\n5. Admin respondiendo a la notificación...")
notificacion.respuesta_admin = "Hemos procesado tu reclamo. Te enviaremos un reemplazo en 3 días hábiles."
notificacion.fecha_respuesta = timezone.now()
notificacion.leida = True
notificacion.save()
print(f"   Respuesta guardada: {notificacion.respuesta_admin}")
print(f"   Fecha respuesta: {notificacion.fecha_respuesta}")

# 6. Verificar que se puede recuperar la notificación con la respuesta
print("\n6. Recuperando notificación con respuesta...")
notificacion_recuperada = NotificacionProblema.objects.get(idNotificacion=notificacion.idNotificacion)
print(f"   Respuesta: {notificacion_recuperada.respuesta_admin}")
print(f"   Fecha: {notificacion_recuperada.fecha_respuesta}")
print(f"   Leída: {notificacion_recuperada.leida}")

# 7. Verificar que el cliente puede ver sus notificaciones
print("\n7. Verificando notificaciones del cliente...")
notificaciones_cliente = NotificacionProblema.objects.filter(
    idPedido__idCliente=cliente
).select_related('idPedido', 'idPedido__idCliente')

print(f"   Total de notificaciones: {notificaciones_cliente.count()}")
for notif in notificaciones_cliente:
    print(f"   - Pedido #{notif.idPedido.idPedido}: {notif.motivo}")
    if notif.respuesta_admin:
        print(f"     Respuesta: {notif.respuesta_admin}")

print("\n" + "="*60)
print("✓ PRUEBA COMPLETADA EXITOSAMENTE")
print("="*60 + "\n")
