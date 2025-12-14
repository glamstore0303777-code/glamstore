# Generated migration to add missing columns to repartidores table

from django.db import migrations
from django.conf import settings


def add_repartidores_columns(apps, schema_editor):
    """Agregar columnas faltantes a repartidores"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    ALTER TABLE repartidores
                    ADD COLUMN IF NOT EXISTS telefono VARCHAR(20);
                """)
                cursor.execute("""
                    ALTER TABLE repartidores
                    ADD COLUMN IF NOT EXISTS email VARCHAR(100);
                """)
            else:
                # SQLite
                cursor.execute("""
                    PRAGMA table_info(repartidores);
                """)
                columns = [col[1] for col in cursor.fetchall()]
                
                if 'telefono' not in columns:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ADD COLUMN telefono VARCHAR(20);
                    """)
                
                if 'email' not in columns:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ADD COLUMN email VARCHAR(100);
                    """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_add_nombre_to_repartidores'),
    ]

    operations = [
        migrations.RunPython(add_repartidores_columns, migrations.RunPython.noop),
    ]
