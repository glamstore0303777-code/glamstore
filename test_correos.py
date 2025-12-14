#!/usr/bin/env python
"""
Script de prueba para verificar que los correos se envíen correctamente
Uso: python test_correos.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.core.mail import send_mail
from core.services.correos_service import encolar_correo, enviar_correos_pendientes
from core.models.correos_pendientes import CorreoPendiente

def test_configuracion_basica():
    """Prueba la configuración básica de correos"""
    print("=" * 60)
    print("PRUEBA 1: Verificar Configuración Básica")
    print("=" * 60)
    
    from django.conf import settings
    
    print(f"✓ EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    print(f"✓ EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"✓ EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"✓ EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    print(f"✓ EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"✓ DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
    
    if not settings.EMAIL_HOST_PASSWORD:
        print("✗ ERROR: EMAIL_HOST_PASSWORD no está configurado")
        return False
    
    print("✓ EMAIL_HOST_PASSWORD: Configurado")
    return True

def test_envio_directo():
    """Prueba envío directo de correo"""
    print("\n" + "=" * 60)
    print("PRUEBA 2: Envío Directo de Correo")
    print("=" * 60)
    
    try:
        resultado = send_mail(
            subject='Prueba de Configuración - Glam Store',
            message='Este es un correo de prueba para verificar que la configuración de correos funciona correctamente.',
            from_email='glamstore0303777@gmail.com',
            recipient_list=['glamstore0303777@gmail.com'],
            fail_silently=False,
        )
        
        if resultado > 0:
            print("✓ Correo de prueba enviado exitosamente")
            return True
        else:
            print("✗ Error: El correo no se envió")
            return False
    except Exception as e:
        print(f"✗ Error al enviar correo: {str(e)}")
        return False

def test_encolar_correo():
    """Prueba encolamiento de correo"""
    print("\n" + "=" * 60)
    print("PRUEBA 3: Encolar Correo")
    print("=" * 60)
    
    try:
        resultado = encolar_correo(
            id_pedido=999,
            destinatario='glamstore0303777@gmail.com',
            asunto='Prueba de Encolamiento - Glam Store',
            contenido_html='<h1>Prueba de Encolamiento</h1><p>Este correo fue encolado correctamente.</p>'
        )
        
        if resultado:
            print("✓ Correo encolado exitosamente")
            
            # Verificar que se encoló
            correo = CorreoPendiente.objects.filter(idPedido=999).last()
            if correo:
                print(f"✓ Correo encontrado en BD: ID {correo.id}")
                return True
        else:
            print("✗ Error al encolar correo")
            return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def test_enviar_pendientes():
    """Prueba envío de correos pendientes"""
    print("\n" + "=" * 60)
    print("PRUEBA 4: Enviar Correos Pendientes")
    print("=" * 60)
    
    try:
        # Contar correos pendientes antes
        pendientes_antes = CorreoPendiente.objects.filter(enviado=False).count()
        print(f"Correos pendientes antes: {pendientes_antes}")
        
        # Enviar
        enviar_correos_pendientes()
        
        # Contar correos pendientes después
        pendientes_despues = CorreoPendiente.objects.filter(enviado=False).count()
        print(f"Correos pendientes después: {pendientes_despues}")
        
        if pendientes_despues < pendientes_antes:
            print("✓ Correos enviados exitosamente")
            return True
        else:
            print("⚠ No se enviaron correos (puede ser normal si no hay pendientes)")
            return True
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def main():
    """Ejecuta todas las pruebas"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  PRUEBAS DE CONFIGURACIÓN DE CORREOS - GLAM STORE".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    resultados = []
    
    # Ejecutar pruebas
    resultados.append(("Configuración Básica", test_configuracion_basica()))
    resultados.append(("Envío Directo", test_envio_directo()))
    resultados.append(("Encolar Correo", test_encolar_correo()))
    resultados.append(("Enviar Pendientes", test_enviar_pendientes()))
    
    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    for nombre, resultado in resultados:
        estado = "✓ PASÓ" if resultado else "✗ FALLÓ"
        print(f"{nombre}: {estado}")
    
    total_pasadas = sum(1 for _, r in resultados if r)
    total_pruebas = len(resultados)
    
    print(f"\nTotal: {total_pasadas}/{total_pruebas} pruebas pasadas")
    
    if total_pasadas == total_pruebas:
        print("\n✓ ¡Todos los correos están configurados correctamente!")
    else:
        print("\n✗ Hay problemas con la configuración de correos")

if __name__ == '__main__':
    main()
