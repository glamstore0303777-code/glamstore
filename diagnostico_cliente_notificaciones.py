#!/usr/bin/env python
"""
Diagnóstico: Por qué el cliente no ve sus notificaciones
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Cliente, Pedido, NotificacionProblema, Usuario

print("\n" + "="*70)
print("DIAGNÓSTICO: CLIENTE NO VE NOTIFICACIONES")
print("="*70)

# 1. Listar todos los clientes
print("\n1. CLIENTES EN LA BD:")
clientes = Cliente.objects.all()
print(f"   Total: {clientes.count()}")
for cliente in clientes:
    print(f"   - {cliente.nombre} (ID: {cliente.idCliente}, Email: {cliente.email})")

# 2. Listar todos los pedidos
print("\n2. PEDIDOS EN LA BD:")
pedidos = Pedido.objects.all()
print(f"   Total: {pedidos.count()}")
for pedido in pedidos:
    print(f"   - Pedido #{pedido.idPedido}: Cliente {pedido.idCliente.nombre if pedido.idCliente else 'Sin cliente'}, Estado: {pedido.estado_pedido}")

# 3. Listar todas las notificaciones
print("\n3. NOTIFICACIONES EN LA BD:")
notificaciones = NotificacionProblema.objects.all()
print(f"   Total: {notificaciones.count()}")
for notif in notificaciones:
    print(f"   - Notif #{notif.idNotificacion}: Pedido #{notif.idPedido.idPedido}, Cliente: {notif.idPedido.idCliente.nombre if notif.idPedido.idCliente else 'Sin cliente'}")

# 4. Para cada cliente, verificar si tiene notificaciones
print("\n4. NOTIFICACIONES POR CLIENTE:")
for cliente in clientes:
    notificaciones_cliente = NotificacionProblema.objects.filter(
        idPedido__idCliente=cliente
    )
    print(f"\n   Cliente: {cliente.nombre} (ID: {cliente.idCliente})")
    print(f"   - Pedidos: {Pedido.objects.filter(idCliente=cliente).count()}")
    print(f"   - Notificaciones: {notificaciones_cliente.count()}")
    
    if notificaciones_cliente.exists():
        for notif in notificaciones_cliente:
            print(f"     * Notif #{notif.idNotificacion}: {notif.motivo[:50]}")

# 5. Verificar si hay usuarios sin cliente asociado
print("\n5. USUARIOS EN LA BD:")
usuarios = Usuario.objects.all()
print(f"   Total: {usuarios.count()}")
for usuario in usuarios:
    print(f"   - {usuario.nombre} (ID: {usuario.idUsuario}, Cliente: {usuario.idCliente_id if usuario.idCliente_id else 'Sin cliente'})")

print("\n" + "="*70)
print("FIN DEL DIAGNÓSTICO")
print("="*70 + "\n")
