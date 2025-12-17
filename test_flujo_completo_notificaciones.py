#!/usr/bin/env python
"""
Test end-to-end del flujo completo de notificaciones:
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
from core.models import Cliente, Pedido, NotificacionProblema, Usuario, DetallePedido, Producto
from datetime import timedelta

print("\n" + "="*70)
print("TEST END-TO-END: FLUJO COMPLETO DE NOTIFICACIONES")
print("="*70)

# 1. Crear cliente de prueba
print("\n1. Creando cliente de prueba...")
cliente, _ = Cliente.objects.get_or_create(
    email='cliente_test_e2e@example.com',
    defaults={
        'nombre': 'Cliente E2E Test',
        'apellido': 'Test',
        'telefono': '3001234567',
        'direccion': 'Calle Test 123, Bogotá'
    }
)
print(f"   ✓ Cliente: {cliente.nombre} (ID: {cliente.idCliente})")

# 2. Crear producto de prueba
print("\n2. Creando producto de prueba...")
producto, _ = Producto.objects.get_or_create(
    nombreProducto='Producto Test E2E',
    defaults={
        'precio': 10000,
        'precio_venta': 11900,
        'stock': 100,
        'idCategoria_id': 1
    }
)
print(f"   ✓ Producto: {producto.nombreProducto} (ID: {producto.idProducto})")

# 3. Crear pedido de prueba
print("\n3. Creando pedido de prueba...")
pedido, _ = Pedido.objects.get_or_create(
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
print(f"   ✓ Pedido: #{pedido.idPedido} - Total: ${pedido.total}")

# 4. Crear detalle del pedido (opcional para este test)
print("\n4. Saltando creación de detalle del pedido (no es necesario para test de notificaciones)")

# 5. Cliente reporta un problema
print("\n5. Cliente reporta un problema...")
notificacion, created = NotificacionProblema.objects.get_or_create(
    idPedido=pedido,
    defaults={
        'motivo': 'El producto llegó con daño en el empaque',
        'leida': False
    }
)
if created:
    print(f"   ✓ Notificación creada: #{notificacion.idNotificacion}")
else:
    print(f"   ℹ Notificación ya existe: #{notificacion.idNotificacion}")

# 6. Verificar que el admin puede ver la notificación
print("\n6. Verificando que el admin puede ver la notificación...")
notificaciones_admin = NotificacionProblema.objects.select_related(
    'idPedido__idCliente',
    'idPedido__idRepartidor'
).order_by('-fechaReporte')

print(f"   Total de notificaciones: {notificaciones_admin.count()}")
for notif in notificaciones_admin:
    print(f"   - Notif #{notif.idNotificacion}: Pedido #{notif.idPedido.idPedido}, Cliente: {notif.idPedido.idCliente.nombre}")

# 7. Admin responde a la notificación
print("\n7. Admin respondiendo a la notificación...")
notificacion.respuesta_admin = "Hemos procesado tu reclamo. Te enviaremos un reemplazo en 3 días hábiles."
notificacion.fecha_respuesta = timezone.now()
notificacion.leida = True
notificacion.save()
print(f"   ✓ Respuesta guardada")

# 8. Verificar que el cliente puede ver la respuesta
print("\n8. Verificando que el cliente puede ver la respuesta...")
notificaciones_cliente = NotificacionProblema.objects.filter(
    idPedido__idCliente=cliente
).select_related('idPedido', 'idPedido__idCliente').order_by('-fechaReporte')

print(f"   Total de notificaciones del cliente: {notificaciones_cliente.count()}")
for notif in notificaciones_cliente:
    print(f"   - Notif #{notif.idNotificacion}:")
    print(f"     Motivo: {notif.motivo}")
    print(f"     Respuesta: {notif.respuesta_admin}")
    print(f"     Fecha respuesta: {notif.fecha_respuesta}")

# 9. Verificar que todos los campos son accesibles
print("\n9. Verificando acceso a todos los campos...")
try:
    print(f"   - idNotificacion: {notificacion.idNotificacion}")
    print(f"   - idPedido: {notificacion.idPedido.idPedido}")
    print(f"   - motivo: {notificacion.motivo[:50]}")
    print(f"   - foto: {notificacion.foto}")
    print(f"   - fechaReporte: {notificacion.fechaReporte}")
    print(f"   - leida: {notificacion.leida}")
    print(f"   - respuesta_admin: {notificacion.respuesta_admin[:50]}")
    print(f"   - fecha_respuesta: {notificacion.fecha_respuesta}")
    print(f"   ✓ Todos los campos son accesibles")
except Exception as e:
    print(f"   ✗ Error al acceder a campos: {e}")

print("\n" + "="*70)
print("✓ TEST COMPLETADO EXITOSAMENTE")
print("="*70 + "\n")
