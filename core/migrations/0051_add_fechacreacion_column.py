"""
Migration to add fechacreacion column to pedidos table if it doesn't exist.
"""
from django.db import migrations
from django.conf import settings


def add_fechacreacion_column(apps, schema_editor):
    """Add fechacreacion column - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                # PostgreSQL version
                cursor.execute("""
                    DO $
                    BEGIN
                        IF NOT EXISTS (
                            SELECT 1 FROM pg_attribute 
                            WHERE attrelid = 'pedidos'::regclass 
                            AND attnum > 0 
                            AND NOT attisdropped
                            AND lower(attname) = 'fechacreacion'
                        ) THEN
                            ALTER TABLE pedidos ADD COLUMN fechacreacion TIMESTAMP DEFAULT NOW();
                        END IF;
                    END $;
                """)
            else:
                # SQLite version
                cursor.execute("""
                    PRAGMA table_info(pedidos);
                """)
                columns = [row[1] for row in cursor.fetchall()]
                
                if 'fechacreacion' not in columns and 'fechaCreacion' not in columns:
                    cursor.execute("""
                        ALTER TABLE pedidos ADD COLUMN fechacreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
                    """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_ensure_configuracion_table'),
    ]

    operations = [
        migrations.RunPython(add_fechacreacion_column, migrations.RunPython.noop),
    ]
