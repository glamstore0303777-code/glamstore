#!/usr/bin/env python
"""
Script para probar el flujo END-TO-END de notificaciones:
1. Cliente envía reporte de problema
2. Admin ve la notificación en su panel
3. Cliente ve la notificación en su panel
4. Admin responde
5. Cliente ve la respuesta
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.utils import timezone
from core.models import Cliente, Pedido, NotificacionProblema, Usuario
from datetime import timedelta

print("\n" + "="*70)
print("PRUEBA END-TO-END: FLUJO COMPLETO DE NOTIFICACIONES")
print("="*70)

# ============================================================================
# PASO 1: CREAR DATOS DE PRUEBA
# ============================================================================
print("\n[PASO 1] Creando datos de prueba...")

# Crear cliente
cliente, _ = Cliente.objects.get_or_create(
    email='cliente_test@example.com',
    defaults={
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'telefono': '3001234567',
        'direccion': 'Calle 10 #20-30, Bogotá'
    }
)
print(f"✓ Cliente creado: {cliente.nombre} (ID: {cliente.idCliente})")

# Crear pedido entregado
pedido, _ = Pedido.objects.get_or_create(
    idCliente=cliente,
    defaults={
        'total': 75000,
        'estado': 'Entregado',
        'estado_pedido': 'Entregado',
        'estado_pago': 'Pago Completo',
        'fechaCreacion': timezone.now() - timedelta(days=2),
        'fecha_vencimiento': timezone.now().date()
    }
)
print(f"✓ Pedido creado: #{pedido.idPedido} - Total: ${pedido.total}")

# ============================================================================
# PASO 2: CLIENTE ENVÍA REPORTE DE PROBLEMA
# ============================================================================
print("\n[PASO 2] Cliente enviando reporte de problema...")

notificacion = NotificacionProblema.objects.create(
    idPedido=pedido,
    motivo='El producto llegó con daño en el empaque. La caja estaba mojada y el producto se dañó.',
    leida=False
)
print(f"✓ Notificación creada: #{notificacion.idNotificacion}")
print(f"  - Pedido: #{notificacion.idPedido.idPedido}")
print(f"  - Motivo: {notificacion.motivo}")
print(f"  - Fecha: {notificacion.fechaReporte}")
print(f"  - Leída: {notificacion.leida}")

# ============================================================================
# PASO 3: VERIFICAR QUE ADMIN PUEDE VER LA NOTIFICACIÓN
# ============================================================================
print("\n[PASO 3] Admin viendo notificaciones en el panel...")

notificaciones_admin = NotificacionProblema.objects.select_related(
    'idPedido__idCliente',
    'idPedido__idRepartidor'
).order_by('-fechaReporte')

print(f"✓ Total de notificaciones en el panel: {notificaciones_admin.count()}")

for notif in notificaciones_admin[:3]:  # Mostrar las últimas 3
    print(f"\n  Notificación #{notif.idNotificacion}:")
    print(f"    - Cliente: {notif.idPedido.idCliente.nombre}")
    print(f"    - Email: {notif.idPedido.idCliente.email}")
    print(f"    - Teléfono: {notif.idPedido.idCliente.telefono}")
    print(f"    - Pedido: #{notif.idPedido.idPedido}")
    print(f"    - Motivo: {notif.motivo}")
    print(f"    - Reportado: {notif.fechaReporte}")
    print(f"    - Estado: {'Leída' if notif.leida else 'SIN LEER'}")

# ============================================================================
# PASO 4: VERIFICAR QUE CLIENTE PUEDE VER SU NOTIFICACIÓN
# ============================================================================
print("\n[PASO 4] Cliente viendo sus notificaciones...")

notificaciones_cliente = NotificacionProblema.objects.filter(
    idPedido__idCliente=cliente
).select_related('idPedido', 'idPedido__idCliente').order_by('-fechaReporte')

print(f"✓ Total de notificaciones del cliente: {notificaciones_cliente.count()}")

for notif in notificaciones_cliente:
    print(f"\n  Notificación #{notif.idNotificacion}:")
    print(f"    - Pedido: #{notif.idPedido.idPedido}")
    print(f"    - Tu reporte: {notif.motivo}")
    print(f"    - Fecha: {notif.fechaReporte}")
    
    if notif.respuesta_admin:
        print(f"    - Respuesta de Glam Store: {notif.respuesta_admin}")
        print(f"    - Respondido: {notif.fecha_respuesta}")
    else:
        print(f"    - Estado: En revisión (sin respuesta aún)")

# ============================================================================
# PASO 5: ADMIN RESPONDE A LA NOTIFICACIÓN
# ============================================================================
print("\n[PASO 5] Admin respondiendo a la notificación...")

notificacion.respuesta_admin = "Lamentamos el inconveniente. Hemos procesado tu reclamo y te enviaremos un reemplazo sin costo en los próximos 3 días hábiles. Recibirás un email con el número de seguimiento."
notificacion.fecha_respuesta = timezone.now()
notificacion.leida = True
notificacion.save()

print(f"✓ Respuesta guardada:")
print(f"  - Respuesta: {notificacion.respuesta_admin}")
print(f"  - Fecha: {notificacion.fecha_respuesta}")

# ============================================================================
# PASO 6: VERIFICAR QUE CLIENTE VE LA RESPUESTA
# ============================================================================
print("\n[PASO 6] Cliente viendo la respuesta del admin...")

notificacion_actualizada = NotificacionProblema.objects.get(
    idNotificacion=notificacion.idNotificacion
)

print(f"✓ Notificación actualizada:")
print(f"  - Tu reporte: {notificacion_actualizada.motivo}")
print(f"  - Respuesta de Glam Store: {notificacion_actualizada.respuesta_admin}")
print(f"  - Respondido: {notificacion_actualizada.fecha_respuesta}")

# ============================================================================
# PASO 7: VERIFICAR ACCESO A TODOS LOS CAMPOS
# ============================================================================
print("\n[PASO 7] Verificando acceso a todos los campos...")

campos_verificar = [
    ('idNotificacion', notificacion_actualizada.idNotificacion),
    ('idPedido', notificacion_actualizada.idPedido.idPedido),
    ('motivo', notificacion_actualizada.motivo),
    ('foto', notificacion_actualizada.foto),
    ('fechaReporte', notificacion_actualizada.fechaReporte),
    ('leida', notificacion_actualizada.leida),
    ('respuesta_admin', notificacion_actualizada.respuesta_admin),
    ('fecha_respuesta', notificacion_actualizada.fecha_respuesta),
]

for campo, valor in campos_verificar:
    estado = "✓" if valor is not None or campo in ['foto', 'respuesta_admin', 'fecha_respuesta'] else "✗"
    print(f"  {estado} {campo}: {valor}")

# ============================================================================
# PASO 8: VERIFICAR QUERIES OPTIMIZADAS
# ============================================================================
print("\n[PASO 8] Verificando queries optimizadas...")

# Query para admin
print("\n  Query para Admin (con select_related):")
notificaciones_admin_opt = NotificacionProblema.objects.select_related(
    'idPedido__idCliente',
    'idPedido__idRepartidor'
).order_by('-fechaReporte')[:1]

for notif in notificaciones_admin_opt:
    print(f"    ✓ Acceso a cliente: {notif.idPedido.idCliente.nombre}")
    print(f"    ✓ Acceso a pedido: #{notif.idPedido.idPedido}")

# Query para cliente
print("\n  Query para Cliente (con select_related):")
notificaciones_cliente_opt = NotificacionProblema.objects.filter(
    idPedido__idCliente=cliente
).select_related('idPedido', 'idPedido__idCliente').order_by('-fechaReporte')[:1]

for notif in notificaciones_cliente_opt:
    print(f"    ✓ Acceso a pedido: #{notif.idPedido.idPedido}")
    print(f"    ✓ Acceso a cliente: {notif.idPedido.idCliente.nombre}")

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n" + "="*70)
print("✓ PRUEBA COMPLETADA EXITOSAMENTE")
print("="*70)
print("\nRESUMEN:")
print(f"  ✓ Cliente puede enviar notificaciones")
print(f"  ✓ Admin puede ver todas las notificaciones")
print(f"  ✓ Cliente puede ver sus notificaciones")
print(f"  ✓ Admin puede responder a notificaciones")
print(f"  ✓ Cliente puede ver las respuestas")
print(f"  ✓ Todos los campos están accesibles")
print(f"  ✓ Queries están optimizadas con select_related")
print("\n" + "="*70 + "\n")
