#!/usr/bin/env python
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models.clientes import Cliente
from core.models.pedidos import Pedido

# Datos reales de clientes (del backup mas reciente)
CLIENTES = [
    {'idcliente': 2, 'cedula': '10002', 'nombre': 'Laura Gómez', 'email': 'laura.gomez@gmail.com', 'direccion': 'Carrera 45 #12-34 Montería', 'telefono': '2147483647'},
    {'idcliente': 13, 'cedula': '7410852', 'nombre': 'william fontecha', 'email': 'carlos@gmail.com', 'direccion': '58bis, Rafael Uribe Uribe, Bogotá, Bogotá D.C. (9-49)', 'telefono': '3115176388'},
    {'idcliente': 15, 'cedula': '441515', 'nombre': 'lalaa ortega ', 'email': 'lala@gmail.com', 'direccion': 'carrera 19a 11, Teusaquillo, Bogotá, Bogotá D.C. - conjunto albarosa', 'telefono': '3024892804'},
    {'idcliente': 17, 'cedula': '441515', 'nombre': 'laura torres', 'email': 'lauratorres@gmail.com', 'direccion': 'carrera 19a 11a 67, Engativá, Bogotá, Bogotá D.C. (9-49)', 'telefono': '3024892804'},
    {'idcliente': 18, 'cedula': '458527', 'nombre': 'laura tibaque', 'email': 'lauratibaque@gmail.com', 'direccion': 'carrera 19a 11a 67, Comuna 4 - Cazucá, Soacha, Cundinamarca (9-49)', 'telefono': '3025458285'},
    {'idcliente': 20, 'cedula': '1234567', 'nombre': 'lauren ortiz', 'email': 'laurensamanta0.r@gmail.com', 'direccion': 'carrera 19a 11a 67, Barrios Unidos, Bogotá, Bogotá D.C. - 9-49', 'telefono': '3024892804'},
]

# Datos reales de pedidos (del backup mas reciente)
PEDIDOS = [
    {'idpedido': 20, 'idcliente': 13, 'fechacreacion': '2025-11-20 13:14:00', 'estado': 'Pago Parcial', 'total': 21420.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 21, 'idcliente': 13, 'fechacreacion': '2025-11-20 13:27:44', 'estado': 'Pago Parcial', 'total': 38080.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 22, 'idcliente': 13, 'fechacreacion': '2025-11-20 13:30:46', 'estado': 'Pago Parcial', 'total': 38080.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 23, 'idcliente': 13, 'fechacreacion': '2025-11-20 15:26:57', 'estado': 'Pago Parcial', 'total': 17850.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 24, 'idcliente': 13, 'fechacreacion': '2025-11-20 15:28:42', 'estado': 'Pago Parcial', 'total': 16660.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 25, 'idcliente': 13, 'fechacreacion': '2025-11-20 15:53:40', 'estado': 'Pago Parcial', 'total': 38080.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 26, 'idcliente': 13, 'fechacreacion': '2025-11-20 16:13:31', 'estado': 'Pago Parcial', 'total': 45220.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 27, 'idcliente': 13, 'fechacreacion': '2025-11-20 18:59:45', 'estado': 'Pago Parcial', 'total': 38080.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 28, 'idcliente': 13, 'fechacreacion': '2025-11-20 19:03:10', 'estado': 'Pago Parcial', 'total': 16660.00, 'idrepartidor': 16, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 33, 'idcliente': 15, 'fechacreacion': '2025-11-20 19:54:00', 'estado': 'Pago Parcial', 'total': 74970.00, 'idrepartidor': 19, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 34, 'idcliente': 15, 'fechacreacion': '2025-11-20 20:05:09', 'estado': 'Pago Parcial', 'total': 21420.00, 'idrepartidor': 19, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 35, 'idcliente': 15, 'fechacreacion': '2025-11-20 20:12:06', 'estado': 'Pago Parcial', 'total': 40460.00, 'idrepartidor': 19, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 36, 'idcliente': 15, 'fechacreacion': '2025-11-20 20:20:36', 'estado': 'Pago Parcial', 'total': 21420.00, 'idrepartidor': 19, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 37, 'idcliente': 17, 'fechacreacion': '2025-11-21 00:32:13', 'estado': 'Pago Parcial', 'total': 65450.00, 'idrepartidor': 19, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 38, 'idcliente': 17, 'fechacreacion': '2025-11-21 01:06:53', 'estado': 'En Camino', 'total': 57600.00, 'idrepartidor': 19, 'estado_pago': 'Pago Completo', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 39, 'idcliente': 18, 'fechacreacion': '2025-11-21 01:08:27', 'estado': 'Pago Parcial', 'total': 40460.00, 'idrepartidor': 15, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 40, 'idcliente': 18, 'fechacreacion': '2025-11-21 01:13:13', 'estado': 'Problema en Entrega', 'total': 49980.00, 'idrepartidor': 15, 'estado_pago': 'Pago Completo', 'estado_pedido': 'Completado', 'fecha_vencimiento': '2025-11-25', 'facturas_enviadas': 1},
    {'idpedido': 43, 'idcliente': 20, 'fechacreacion': '2025-11-22 00:53:43', 'estado': 'Entregado', 'total': 141610.00, 'idrepartidor': 15, 'estado_pago': 'Pago Completo', 'estado_pedido': 'Completado', 'fecha_vencimiento': '2025-11-26', 'facturas_enviadas': 1},
    {'idpedido': 44, 'idcliente': 20, 'fechacreacion': '2025-11-22 00:58:29', 'estado': 'Entregado', 'total': 42840.00, 'idrepartidor': 15, 'estado_pago': 'Pago Completo', 'estado_pedido': 'Completado', 'fecha_vencimiento': '2025-11-26', 'facturas_enviadas': 1},
    {'idpedido': 45, 'idcliente': 20, 'fechacreacion': '2025-11-22 01:12:30', 'estado': 'Pago Parcial', 'total': 61880.00, 'idrepartidor': 15, 'estado_pago': 'Pago Parcial', 'estado_pedido': 'Entregado', 'fecha_vencimiento': '2025-11-26', 'facturas_enviadas': 1},
]

try:
    # Insertar clientes usando Django ORM
    for cliente_data in CLIENTES:
        cliente, created = Cliente.objects.get_or_create(
            idCliente=cliente_data['idcliente'],
            defaults={
                'cedula': cliente_data['cedula'],
                'nombre': cliente_data['nombre'],
                'email': cliente_data['email'],
                'direccion': cliente_data['direccion'],
                'telefono': cliente_data['telefono'],
            }
        )
        if created:
            print(f"Cliente creado: {cliente.nombre}")
    
    # Insertar pedidos usando Django ORM
    for pedido_data in PEDIDOS:
        try:
            cliente = Cliente.objects.get(idCliente=pedido_data['idcliente'])
            pedido, created = Pedido.objects.get_or_create(
                idPedido=pedido_data['idpedido'],
                defaults={
                    'idCliente': cliente,
                    'fechaCreacion': pedido_data['fechacreacion'],
                    'estado': pedido_data['estado'],
                    'total': pedido_data['total'],
                    'idRepartidor_id': pedido_data['idrepartidor'],
                    'estado_pago': pedido_data['estado_pago'],
                    'estado_pedido': pedido_data['estado_pedido'],
                    'fecha_vencimiento': pedido_data['fecha_vencimiento'],
                    'facturas_enviadas': pedido_data['facturas_enviadas'],
                }
            )
            if created:
                print(f"Pedido creado: #{pedido.idPedido} - Cliente: {cliente.nombre}")
        except Cliente.DoesNotExist:
            print(f"Cliente {pedido_data['idcliente']} no encontrado para pedido {pedido_data['idpedido']}")
    
    print("\nDatos restaurados exitosamente")
except Exception as e:
    print(f"Error al restaurar datos: {e}")
    import traceback
    traceback.print_exc()
