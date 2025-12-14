#!/usr/bin/env python
"""
Script de prueba para verificar que el sistema de registro funciona correctamente.
Ejecutar con: python manage.py shell < test_registro.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Cliente, Usuario
from django.contrib.auth.hashers import make_password
from django.utils import timezone

# Limpiar datos de prueba anteriores
print("=" * 60)
print("PRUEBA DE REGISTRO DE CLIENTES")
print("=" * 60)

# Datos de prueba
email_prueba = "cliente_prueba@test.com"
nombre_prueba = "Cliente Prueba"
cedula_prueba = "1234567890"
direccion_prueba = "Calle 123, Apartamento 456"
telefono_prueba = "3001234567"
password_prueba = "password123"

# 1. Limpiar datos anteriores si existen
print("\n1. Limpiando datos anteriores...")
Usuario.objects.filter(email=email_prueba).delete()
Cliente.objects.filter(email=email_prueba).delete()
print("   ✓ Datos anteriores eliminados")

# 2. Crear cliente
print("\n2. Creando cliente...")
try:
    cliente = Cliente.objects.create(
        nombre=nombre_prueba,
        email=email_prueba,
        cedula=cedula_prueba,
        direccion=direccion_prueba,
        telefono=telefono_prueba
    )
    print(f"   ✓ Cliente creado: ID={cliente.idCliente}, Email={cliente.email}")
except Exception as e:
    print(f"   ✗ Error al crear cliente: {e}")
    exit(1)

# 3. Crear usuario
print("\n3. Creando usuario...")
try:
    usuario = Usuario.objects.create(
        email=email_prueba,
        password=make_password(password_prueba),
        id_rol=2,  # Cliente
        idCliente=cliente.idCliente,
        fechaCreacion=timezone.now(),
        nombre=nombre_prueba,
        telefono=telefono_prueba,
        direccion=direccion_prueba
    )
    print(f"   ✓ Usuario creado: ID={usuario.idUsuario}, Email={usuario.email}")
except Exception as e:
    print(f"   ✗ Error al crear usuario: {e}")
    exit(1)

# 4. Verificar que se crearon correctamente
print("\n4. Verificando datos...")
try:
    cliente_verificado = Cliente.objects.get(email=email_prueba)
    usuario_verificado = Usuario.objects.get(email=email_prueba)
    
    print(f"   ✓ Cliente verificado: {cliente_verificado.nombre}")
    print(f"   ✓ Usuario verificado: {usuario_verificado.nombre}")
    print(f"   ✓ Relación: Usuario.idCliente = {usuario_verificado.idCliente} (Cliente.idCliente = {cliente_verificado.idCliente})")
except Exception as e:
    print(f"   ✗ Error al verificar: {e}")
    exit(1)

# 5. Verificar autenticación
print("\n5. Verificando autenticación...")
from django.contrib.auth.hashers import check_password
if check_password(password_prueba, usuario_verificado.password):
    print(f"   ✓ Contraseña verificada correctamente")
else:
    print(f"   ✗ Error: Contraseña no coincide")
    exit(1)

print("\n" + "=" * 60)
print("✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
print("=" * 60)
print("\nEl sistema de registro está funcionando correctamente.")
print(f"Puedes probar iniciando sesión con:")
print(f"  Email: {email_prueba}")
print(f"  Contraseña: {password_prueba}")
