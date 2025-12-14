# Migración para crear usuario administrador de prueba

from django.db import migrations
from django.contrib.auth.hashers import make_password
from django.utils import timezone

def crear_admin(apps, schema_editor):
    """Crear usuario administrador de prueba"""
    Usuario = apps.get_model('core', 'Usuario')
    
    # Verificar si ya existe
    if Usuario.objects.filter(email='glamstore0303777@gmail.com').exists():
        return
    
    # Crear usuario admin
    Usuario.objects.create(
        email='glamstore0303777@gmail.com',
        password=make_password('admin123'),
        nombre='Administrador',
        id_rol=1,  # 1 = Administrador
        fechacreacion=timezone.now(),
        ultimoacceso=timezone.now()
    )

def revertir(apps, schema_editor):
    """Revertir la creación del usuario"""
    Usuario = apps.get_model('core', 'Usuario')
    Usuario.objects.filter(email='glamstore0303777@gmail.com').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_empty_migration'),
    ]

    operations = [
        migrations.RunPython(crear_admin, revertir),
    ]
