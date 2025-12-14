# Generated migration to add nombre column to repartidores table

from django.db import migrations
from django.conf import settings


def add_nombre_column(apps, schema_editor):
    """Agregar columna nombre a repartidores si no existe"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    ALTER TABLE repartidores
                    ADD COLUMN IF NOT EXISTS nombre VARCHAR(50);
                """)
            else:
                # SQLite
                cursor.execute("""
                    PRAGMA table_info(repartidores);
                """)
                columns = [col[1] for col in cursor.fetchall()]
                if 'nombre' not in columns:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ADD COLUMN nombre VARCHAR(50);
                    """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_add_missing_columns'),
    ]

    operations = [
        migrations.RunPython(add_nombre_column, migrations.RunPython.noop),
    ]
