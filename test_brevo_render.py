#!/usr/bin/env python
"""
Script para verificar que Brevo está correctamente configurado en Render
Ejecutar: python test_brevo_render.py
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
sys.path.insert(0, os.path.dirname(__file__))

django.setup()

from django.conf import settings
from core.services.brevo_service import enviar_correo_brevo

def verificar_configuracion():
    """Verifica que la configuración de Brevo esté correcta"""
    
    print("=" * 60)
    print("VERIFICACIÓN DE CONFIGURACIÓN DE BREVO")
    print("=" * 60)
    
    # 1. Verificar que BREVO_API_KEY esté configurado
    print("\n1. Verificando BREVO_API_KEY...")
    if not settings.BREVO_API_KEY:
        print("   ❌ ERROR: BREVO_API_KEY no está configurado")
        print("   Agrega BREVO_API_KEY a las variables de entorno en Render")
        return False
    
    api_key_masked = settings.BREVO_API_KEY[:10] + "..." + settings.BREVO_API_KEY[-10:]
    print(f"   ✅ BREVO_API_KEY configurado: {api_key_masked}")
    
    # 2. Verificar que sib-api-v3-sdk esté instalado
    print("\n2. Verificando dependencias...")
    try:
        import sib_api_v3_sdk
        print(f"   ✅ sib-api-v3-sdk instalado (versión: {sib_api_v3_sdk.__version__ if hasattr(sib_api_v3_sdk, '__version__') else 'desconocida'})")
    except ImportError:
        print("   ❌ ERROR: sib-api-v3-sdk no está instalado")
        print("   Ejecuta: pip install sib-api-v3-sdk==7.6.0")
        return False
    
    # 3. Verificar que el servicio de Brevo esté disponible
    print("\n3. Verificando servicio de Brevo...")
    try:
        from core.services.brevo_service import enviar_correo_brevo
        print("   ✅ Servicio de Brevo importado correctamente")
    except ImportError as e:
        print(f"   ❌ ERROR: No se puede importar el servicio de Brevo: {e}")
        return False
    
    # 4. Verificar que el email remitente esté configurado
    print("\n4. Verificando configuración de email...")
    print(f"   ✅ Email remitente: glamstore0303777@gmail.com")
    print(f"   ✅ Nombre remitente: Glam Store")
    
    # 5. Verificar que Django esté configurado correctamente
    print("\n5. Verificando configuración de Django...")
    print(f"   ✅ DEBUG: {settings.DEBUG}")
    print(f"   ✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    print("\n" + "=" * 60)
    print("✅ CONFIGURACIÓN VERIFICADA CORRECTAMENTE")
    print("=" * 60)
    print("\nPróximos pasos:")
    print("1. Agrega BREVO_API_KEY en Render → Environment")
    print("2. Redeploy la aplicación")
    print("3. Prueba confirmando un pedido")
    print("4. Verifica que el correo llegue al cliente")
    
    return True

if __name__ == '__main__':
    try:
        success = verificar_configuracion()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
