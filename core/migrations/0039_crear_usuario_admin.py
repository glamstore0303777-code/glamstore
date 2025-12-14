# Migración para crear usuario administrador de prueba

from django.db import migrations
from django.contrib.auth.hashers import make_password
from django.utils import timezone


def crear_admin(apps, schema_editor):
    """Crear usuario administrador de prueba usando SQL directo"""
    from django.db import connection
    from django.conf import settings

    # Detectar si es PostgreSQL o SQLite
    db_engine = settings.DATABASES['default']['ENGINE']

    with connection.cursor() as cursor:
        # Verificar si ya existe - usar el método correcto de Django
        try:
            if 'postgresql' in db_engine:
                cursor.execute(
                    "SELECT COUNT(*) FROM usuarios WHERE email = %s",
                    ['glamstore0303777@gmail.com']
                )
            else:
                # SQLite: usar qmark style
                cursor.execute(
                    "SELECT COUNT(*) FROM usuarios WHERE email = ?",
                    ('glamstore0303777@gmail.com',)
                )

            if cursor.fetchone()[0] > 0:
                return
        except:
            # Si la tabla no existe, continuar
            pass

        # Crear usuario admin con SQL directo
        password_hash = make_password('admin123')

        try:
            if 'postgresql' in db_engine:
                cursor.execute(
                    "INSERT INTO usuarios (email, password, nombre, id_rol, fechacreacion, ultimoacceso) VALUES (%s, %s, %s, %s, %s, %s)",
                    [
                        'glamstore0303777@gmail.com',
                        password_hash,
                        'Administrador',
                        1,
                        timezone.now(),
                        timezone.now()
                    ]
                )
            else:
                # SQLite: usar qmark style con tupla
                cursor.execute(
                    "INSERT INTO usuarios (email, password, nombre, id_rol, fechacreacion, ultimoacceso) VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        'glamstore0303777@gmail.com',
                        password_hash,
                        'Administrador',
                        1,
                        timezone.now(),
                        timezone.now()
                    )
                )
        except:
            # Si falla, ignorar (tabla podría no existir)
            pass


def revertir(apps, schema_editor):
    """Revertir la creación del usuario"""
    from django.db import connection
    from django.conf import settings

    db_engine = settings.DATABASES['default']['ENGINE']

    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                cursor.execute(
                    "DELETE FROM usuarios WHERE email = %s",
                    ['glamstore0303777@gmail.com']
                )
            else:
                cursor.execute(
                    "DELETE FROM usuarios WHERE email = ?",
                    ('glamstore0303777@gmail.com',)
                )
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_empty_migration'),
    ]

    operations = [
        migrations.RunPython(crear_admin, revertir),
    ]
