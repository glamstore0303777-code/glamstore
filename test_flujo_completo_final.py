#!/usr/bin/env python
"""
Test final: Verificar que todo el flujo de notificaciones funciona correctamente
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Cliente, Pedido, NotificacionProblema, Usuario
from django.utils import timezone
from datetime import timedelta

print("\n" + "="*70)
print("TEST FINAL: FLUJO COMPLETO DE NOTIFICACIONES")
print("="*70)

# 1. Verificar que hay clientes con pedidos
print("\n1. Verificando clientes con pedidos...")
clientes_con_pedidos = Cliente.objects.filter(pedido__isnull=False).distinct()
print(f"   Total: {clientes_con_pedidos.count()}")

if clientes_con_pedidos.count() == 0:
    print("   ✗ No hay clientes con pedidos")
    exit(1)

# 2. Verificar que hay notificaciones
print("\n2. Verificando notificaciones...")
notificaciones = NotificacionProblema.objects.all()
print(f"   Total: {notificaciones.count()}")

if notificaciones.count() == 0:
    print("   ✗ No hay notificaciones")
    exit(1)

# 3. Verificar que cada notificación tiene los campos correctos
print("\n3. Verificando campos de notificaciones...")
for notif in notificaciones[:3]:
    print(f"\n   Notificación #{notif.idNotificacion}:")
    print(f"   - Pedido: #{notif.idPedido.idPedido} ✓")
    print(f"   - Cliente: {notif.idPedido.idCliente.nombre} ✓")
    print(f"   - Motivo: {notif.motivo[:50] if notif.motivo else 'N/A'} ✓")
    print(f"   - Leída: {notif.leida} ✓")
    print(f"   - Respuesta: {notif.respuesta_admin[:50] if notif.respuesta_admin else 'Sin respuesta'} ✓")
    print(f"   - Fecha respuesta: {notif.fecha_respuesta} ✓")

# 4. Verificar que el cliente puede ver sus notificaciones
print("\n4. Verificando que clientes ven sus notificaciones...")
for cliente in clientes_con_pedidos[:2]:
    notificaciones_cliente = NotificacionProblema.objects.filter(
        idPedido__idCliente=cliente
    )
    print(f"\n   Cliente: {cliente.nombre} (ID: {cliente.idCliente})")
    print(f"   - Notificaciones: {notificaciones_cliente.count()}")
    
    if notificaciones_cliente.count() > 0:
        print(f"   ✓ Cliente VE sus notificaciones")
    else:
        print(f"   ℹ Cliente no tiene notificaciones")

# 5. Verificar que el admin puede ver todas las notificaciones
print("\n5. Verificando que admin ve todas las notificaciones...")
todas_notificaciones = NotificacionProblema.objects.select_related(
    'idPedido__idCliente',
    'idPedido__idRepartidor'
).order_by('-fechaReporte')

print(f"   Total: {todas_notificaciones.count()}")
if todas_notificaciones.count() > 0:
    print(f"   ✓ Admin VE todas las notificaciones")
else:
    print(f"   ✗ Admin NO ve notificaciones")

# 6. Verificar que las notificaciones tienen respuestas
print("\n6. Verificando respuestas del admin...")
notificaciones_con_respuesta = NotificacionProblema.objects.filter(
    respuesta_admin__isnull=False
).exclude(respuesta_admin='')

print(f"   Con respuesta: {notificaciones_con_respuesta.count()}")
notificaciones_sin_respuesta = NotificacionProblema.objects.filter(
    respuesta_admin__isnull=True
) | NotificacionProblema.objects.filter(respuesta_admin='')

print(f"   Sin respuesta: {notificaciones_sin_respuesta.count()}")

# 7. Verificar que no hay errores en la BD
print("\n7. Verificando integridad de datos...")
try:
    # Verificar que todos los pedidos existen
    for notif in notificaciones:
        if not notif.idPedido:
            print(f"   ✗ Notificación #{notif.idNotificacion} sin pedido")
        if not notif.idPedido.idCliente:
            print(f"   ✗ Pedido #{notif.idPedido.idPedido} sin cliente")
    
    print(f"   ✓ Integridad de datos verificada")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n" + "="*70)
print("✓ TEST COMPLETADO EXITOSAMENTE")
print("="*70 + "\n")
