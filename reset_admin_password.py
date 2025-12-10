#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import Usuario
from django.contrib.auth.hashers import make_password

print("Reseteando contraseña del admin...")

try:
    admin = Usuario.objects.get(email='admin@glamstore.com')
    admin.password = make_password('admin123')
    admin.save()
    
    print("✓ Contraseña actualizada exitosamente")
    print(f"  Email: admin@glamstore.com")
    print(f"  Nueva contraseña: admin123")
    
except Usuario.DoesNotExist:
    print("✗ Admin no encontrado")
except Exception as e:
    print(f"✗ Error: {str(e)}")
