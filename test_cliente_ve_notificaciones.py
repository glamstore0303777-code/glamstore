#!/usr/bin/env python
"""
Test para verificar que el cliente puede ver sus notificaciones
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import NotificacionProblema, Cliente, Pedido

print("\n" + "="*70)
print("TEST: CLIENTE VE SUS NOTIFICACIONES")
print("="*70)

# 1. Obtener un cliente con notificaciones
print("\n1. Buscando clientes con notificaciones...")
clientes_con_notificaciones = Cliente.objects.filter(
    pedido__notificacionproblema__isnull=False
).distinct()

print(f"   Total de clientes con notificaciones: {clientes_con_notificaciones.count()}")

for cliente in clientes_con_notificaciones:
    print(f"\n   Cliente: {cliente.nombre} (ID: {cliente.idCliente})")
    
    # Obtener notificaciones del cliente
    notificaciones = NotificacionProblema.objects.filter(
        idPedido__idCliente=cliente
    ).select_related('idPedido', 'idPedido__idCliente').order_by('-fechaReporte')
    
    print(f"   Total de notificaciones: {notificaciones.count()}")
    
    for notif in notificaciones:
        print(f"\n     Notificación #{notif.idNotificacion}:")
        print(f"       - Pedido: #{notif.idPedido.idPedido}")
        print(f"       - Motivo: {notif.motivo[:50] if notif.motivo else 'Sin motivo'}")
        print(f"       - Leída: {notif.leida}")
        print(f"       - Respuesta: {notif.respuesta_admin[:50] if notif.respuesta_admin else 'Sin respuesta'}")
        print(f"       - Fecha respuesta: {notif.fecha_respuesta}")

print("\n" + "="*70)
print("FIN DEL TEST")
print("="*70 + "\n")
