#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models.clientes import Cliente
from core.models.pedidos import Pedido

print(f"Total de clientes: {Cliente.objects.count()}")
print(f"Total de pedidos: {Pedido.objects.count()}")

print("\nClientes:")
for c in Cliente.objects.all():
    print(f"  - {c.nombre} ({c.email})")

print("\nPrimeros 5 pedidos:")
for p in Pedido.objects.all()[:5]:
    cliente_nombre = p.idCliente.nombre if p.idCliente else "Sin cliente"
    print(f"  - Pedido #{p.idPedido} - Cliente: {cliente_nombre} - Total: ${p.total}")
