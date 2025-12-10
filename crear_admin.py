#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Usuario
from django.contrib.auth.hashers import make_password
from django.db import connection

# Verificar si existe un admin
print("Verificando usuarios en la base de datos...")

with connection.cursor() as cursor:
    cursor.execute("SELECT idUsuario, email, nombre, id_rol FROM usuarios LIMIT 10")
    usuarios = cursor.fetchall()
    print(f"\nTotal de usuarios: {len(usuarios)}")
    for u in usuarios:
        print(f"  ID: {u[0]}, Email: {u[1]}, Nombre: {u[2]}, Rol ID: {u[3]}")

# Crear un admin
print("\n" + "="*50)
print("Creando usuario administrador...")
print("="*50)

try:
    # Verificar si ya existe
    admin_existente = Usuario.objects.filter(email='admin@glamstore.com').first()
    if admin_existente:
        print("✓ Admin ya existe: admin@glamstore.com")
        print(f"  ID: {admin_existente.idUsuario}")
        print(f"  Nombre: {admin_existente.nombre}")
        print(f"  Rol ID: {admin_existente.id_rol}")
    else:
        # Crear nuevo admin
        admin = Usuario.objects.create(
            nombre='Administrador',
            email='admin@glamstore.com',
            password=make_password('admin123'),
            id_rol=1,  # Rol de Administrador
            idCliente=None
        )
        print(f"✓ Admin creado exitosamente")
        print(f"  Email: admin@glamstore.com")
        print(f"  Contraseña: admin123")
        print(f"  ID: {admin.idUsuario}")
        
except Exception as e:
    print(f"✗ Error al crear admin: {str(e)}")

print("\n" + "="*50)
print("Listo. Puedes iniciar sesión con:")
print("  Email: admin@glamstore.com")
print("  Contraseña: admin123")
print("="*50)
