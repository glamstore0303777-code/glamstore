# Generated migration to add missing columns to repartidores table

from django.db import migrations
from django.conf import settings


def add_repartidores_columns(apps, schema_editor):
    """Agregar columnas faltantes a repartidores"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    if 'postgresql' in db_engine:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    ALTER TABLE repartidores
                    ADD COLUMN IF NOT EXISTS telefono VARCHAR(20);
                """)
        except Exception:
            pass
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    ALTER TABLE repartidores
                    ADD COLUMN IF NOT EXISTS email VARCHAR(100);
                """)
        except Exception:
            pass
    else:
        # SQLite
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    PRAGMA table_info(repartidores);
                """)
                columns = [col[1] for col in cursor.fetchall()]
                
                if 'telefono' not in columns:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ADD COLUMN telefono VARCHAR(20);
                    """)
        except Exception:
            pass
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    PRAGMA table_info(repartidores);
                """)
                columns = [col[1] for col in cursor.fetchall()]
                
                if 'email' not in columns:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ADD COLUMN email VARCHAR(100);
                    """)
        except Exception:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_add_nombre_to_repartidores'),
    ]

    operations = [
        migrations.RunPython(add_repartidores_columns, migrations.RunPython.noop),
    ]
