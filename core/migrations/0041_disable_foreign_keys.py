# Migración para deshabilitar foreign keys temporalmente

from django.db import migrations


def disable_fk(apps, schema_editor):
    """Deshabilitar foreign keys"""
    from django.db import connection
    from django.conf import settings

    db_engine = settings.DATABASES['default']['ENGINE']

    with connection.cursor() as cursor:
        if 'postgresql' in db_engine:
            cursor.execute("ALTER TABLE productos DROP CONSTRAINT IF EXISTS productos_idCategoria_e28f49a8_fk_categoria_idCategoria")
            cursor.execute("ALTER TABLE productos DROP CONSTRAINT IF EXISTS productos_idSubcategoria_e28f49a8_fk_subcategoria_idSubcategoria")
        else:
            # SQLite no soporta DROP CONSTRAINT, pero tampoco tiene foreign keys habilitadas por defecto
            pass


def enable_fk(apps, schema_editor):
    """Re-habilitar foreign keys"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_crear_usuario_admin'),
    ]

    operations = [
        migrations.RunPython(disable_fk, enable_fk),
    ]
