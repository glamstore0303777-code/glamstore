#!/usr/bin/env python
"""
Script de diagnóstico para verificar el estado de los correos encolados
Uso: python diagnostico_correos.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models.correos_pendientes import CorreoPendiente
from django.conf import settings
from datetime import datetime

def diagnostico():
    print("\n" + "=" * 70)
    print("DIAGNÓSTICO DE CORREOS - GLAM STORE")
    print("=" * 70)
    
    # 1. Verificar configuración
    print("\n1. CONFIGURACIÓN DE CORREOS:")
    print(f"   EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    print(f"   EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"   EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"   EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    print(f"   EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"   PASSWORD configurado: {'Sí' if settings.EMAIL_HOST_PASSWORD else 'NO ❌'}")
    
    # 2. Contar correos encolados
    print("\n2. ESTADO DE CORREOS ENCOLADOS:")
    total = CorreoPendiente.objects.count()
    enviados = CorreoPendiente.objects.filter(enviado=True).count()
    pendientes = CorreoPendiente.objects.filter(enviado=False).count()
    con_error = CorreoPendiente.objects.filter(enviado=False, intentos__gte=3).count()
    
    print(f"   Total de correos: {total}")
    print(f"   Enviados: {enviados} ✓")
    print(f"   Pendientes: {pendientes}")
    print(f"   Con error (3+ intentos): {con_error} ❌")
    
    # 3. Mostrar correos pendientes
    if pendientes > 0:
        print("\n3. CORREOS PENDIENTES:")
        correos_pendientes = CorreoPendiente.objects.filter(enviado=False).order_by('fecha_creacion')[:5]
        for correo in correos_pendientes:
            print(f"\n   ID: {correo.id}")
            print(f"   Pedido: {correo.idPedido}")
            print(f"   Destinatario: {correo.destinatario}")
            print(f"   Asunto: {correo.asunto[:50]}...")
            print(f"   Intentos: {correo.intentos}/3")
            print(f"   Creado: {correo.fecha_creacion}")
            if correo.error:
                print(f"   Error: {correo.error[:100]}...")
    
    # 4. Mostrar correos enviados recientemente
    print("\n4. CORREOS ENVIADOS RECIENTEMENTE:")
    enviados_recientes = CorreoPendiente.objects.filter(enviado=True).order_by('-fecha_envio')[:5]
    if enviados_recientes.exists():
        for correo in enviados_recientes:
            print(f"\n   ID: {correo.id}")
            print(f"   Pedido: {correo.idPedido}")
            print(f"   Destinatario: {correo.destinatario}")
            print(f"   Enviado: {correo.fecha_envio}")
    else:
        print("   No hay correos enviados aún")
    
    # 5. Recomendaciones
    print("\n5. RECOMENDACIONES:")
    if not settings.EMAIL_HOST_PASSWORD:
        print("   ❌ EMAIL_HOST_PASSWORD no está configurado en .env")
    elif pendientes > 0:
        print("   ℹ️  Hay correos pendientes. Ejecuta:")
        print("      python manage.py enviar_correos_pendientes")
    else:
        print("   ✓ Todo parece estar en orden")
    
    print("\n" + "=" * 70 + "\n")

if __name__ == '__main__':
    diagnostico()
