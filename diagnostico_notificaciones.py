#!/usr/bin/env python
"""
Script para diagnosticar por qué no se ven las notificaciones en el admin
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import NotificacionProblema, MensajeContacto, Pedido, Cliente
from django.db import connection

print("\n" + "="*70)
print("DIAGNÓSTICO: Notificaciones en el Admin")
print("="*70)

# 1. Verificar tabla
print("\n[1] Verificando tabla notificaciones_problema...")
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public' 
        AND table_name = 'notificaciones_problema'
    """)
    result = cursor.fetchone()
    if result:
        print("    ✓ Tabla existe")
    else:
        print("    ✗ Tabla NO existe")

# 2. Verificar columnas
print("\n[2] Verificando columnas...")
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'notificaciones_problema'
        ORDER BY ordinal_position
    """)
    columns = cursor.fetchall()
    if columns:
        print("    ✓ Columnas encontradas:")
        for col_name, col_type in columns:
            print(f"      - {col_name}: {col_type}")
    else:
        print("    ✗ No hay columnas")

# 3. Contar registros
print("\n[3] Contando registros...")
try:
    total = NotificacionProblema.objects.count()
    print(f"    ✓ Total de notificaciones: {total}")
    
    if total > 0:
        # Mostrar últimas 3
        print("\n    Últimas notificaciones:")
        for notif in NotificacionProblema.objects.order_by('-fechaReporte')[:3]:
            print(f"      - ID: {notif.idNotificacion}")
            print(f"        Pedido: #{notif.idPedido.idPedido}")
            print(f"        Motivo: {notif.motivo[:50]}...")
            print(f"        Fecha: {notif.fechaReporte}")
            print(f"        Leída: {notif.leida}")
except Exception as e:
    print(f"    ✗ Error: {str(e)}")

# 4. Verificar query del admin
print("\n[4] Probando query del admin...")
try:
    notificaciones = NotificacionProblema.objects.select_related(
        'idPedido__idCliente',
        'idPedido__idRepartidor'
    ).order_by('-fechaReporte')
    
    print(f"    ✓ Query ejecutada correctamente")
    print(f"    ✓ Total de notificaciones: {notificaciones.count()}")
    
    if notificaciones.count() > 0:
        notif = notificaciones.first()
        print(f"\n    Primera notificación:")
        print(f"      - ID: {notif.idNotificacion}")
        print(f"      - Pedido: #{notif.idPedido.idPedido}")
        print(f"      - Cliente: {notif.idPedido.idCliente.nombre}")
        print(f"      - Motivo: {notif.motivo}")
except Exception as e:
    print(f"    ✗ Error: {str(e)}")
    import traceback
    traceback.print_exc()

# 5. Verificar mensajes de contacto
print("\n[5] Verificando mensajes de contacto...")
try:
    total_mensajes = MensajeContacto.objects.count()
    print(f"    ✓ Total de mensajes: {total_mensajes}")
except Exception as e:
    print(f"    ✗ Error: {str(e)}")

# 6. Verificar pedidos
print("\n[6] Verificando pedidos...")
try:
    total_pedidos = Pedido.objects.count()
    print(f"    ✓ Total de pedidos: {total_pedidos}")
except Exception as e:
    print(f"    ✗ Error: {str(e)}")

# 7. Verificar clientes
print("\n[7] Verificando clientes...")
try:
    total_clientes = Cliente.objects.count()
    print(f"    ✓ Total de clientes: {total_clientes}")
except Exception as e:
    print(f"    ✗ Error: {str(e)}")

print("\n" + "="*70 + "\n")
