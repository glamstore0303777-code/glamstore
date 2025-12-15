#!/usr/bin/env python
"""
Script de diagnóstico para verificar que los fixes están aplicados correctamente
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection
from core.models import CorreoPendiente, NotificacionProblema, Pedido
from django.conf import settings

print("=" * 60)
print("🔍 DIAGNÓSTICO DE FIXES - GLAMSTORE")
print("=" * 60)
print()

# 1. Verificar tabla de correos pendientes
print("1️⃣  Verificando tabla correos_pendientes...")
try:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables 
                WHERE table_name = 'correos_pendientes'
            );
        """)
        existe = cursor.fetchone()[0]
    
    if existe:
        count = CorreoPendiente.objects.count()
        pendientes = CorreoPendiente.objects.filter(enviado=False).count()
        print(f"   ✅ Tabla existe")
        print(f"   📊 Total de registros: {count}")
        print(f"   ⏳ Pendientes de envío: {pendientes}")
    else:
        print(f"   ❌ Tabla NO existe - Ejecuta: python manage.py migrate")
except Exception as e:
    print(f"   ❌ Error: {e}")

print()

# 2. Verificar tabla de notificaciones
print("2️⃣  Verificando tabla notificaciones_problema...")
try:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables 
                WHERE table_name = 'notificaciones_problema'
            );
        """)
        existe = cursor.fetchone()[0]
    
    if existe:
        count = NotificacionProblema.objects.count()
        no_leidas = NotificacionProblema.objects.filter(leida=False).count()
        print(f"   ✅ Tabla existe")
        print(f"   📊 Total de notificaciones: {count}")
        print(f"   🔔 No leídas: {no_leidas}")
    else:
        print(f"   ❌ Tabla NO existe - Ejecuta: python manage.py migrate")
except Exception as e:
    print(f"   ❌ Error: {e}")

print()

# 3. Verificar configuración de Brevo
print("3️⃣  Verificando configuración de Brevo...")
try:
    brevo_key = settings.BREVO_API_KEY
    if brevo_key and len(brevo_key) > 10:
        print(f"   ✅ BREVO_API_KEY configurado")
        print(f"   🔑 Primeros 10 caracteres: {brevo_key[:10]}...")
    else:
        print(f"   ❌ BREVO_API_KEY no configurado o inválido")
except Exception as e:
    print(f"   ❌ Error: {e}")

print()

# 4. Verificar función generar_html_factura
print("4️⃣  Verificando función generar_html_factura...")
try:
    from core.services.brevo_service import generar_html_factura
    print(f"   ✅ Función generar_html_factura existe")
except ImportError:
    print(f"   ❌ Función generar_html_factura NO existe")

print()

# 5. Verificar función enviar_correos_pendientes
print("5️⃣  Verificando función enviar_correos_pendientes...")
try:
    from core.services.correos_service import enviar_correos_pendientes
    print(f"   ✅ Función enviar_correos_pendientes existe")
except ImportError:
    print(f"   ❌ Función enviar_correos_pendientes NO existe")

print()

# 6. Verificar pedidos sin asignar
print("6️⃣  Verificando pedidos sin asignar...")
try:
    sin_asignar = Pedido.objects.filter(idRepartidor__isnull=True).exclude(
        estado_pedido__in=['Entregado', 'Completado', 'Cancelado']
    ).count()
    print(f"   📦 Pedidos sin repartidor: {sin_asignar}")
except Exception as e:
    print(f"   ❌ Error: {e}")

print()

# 7. Resumen
print("=" * 60)
print("📋 RESUMEN")
print("=" * 60)
print()
print("✅ Si todos los checks están en verde, los fixes están aplicados")
print()
print("⚠️  Próximos pasos:")
print("   1. Ejecuta: python manage.py migrate")
print("   2. Configura un cron job para: python manage.py enviar_correos_pendientes")
print("   3. Prueba la asignación de repartidores")
print()
