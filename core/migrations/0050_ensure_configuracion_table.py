"""
Migration to ensure configuracion_global table exists and fix any remaining column issues.
"""
from django.db import migrations
from django.conf import settings


def ensure_configuracion_table(apps, schema_editor):
    """Ensure configuracion_global table exists - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS configuracion_global (
                        id BIGSERIAL PRIMARY KEY,
                        margen_ganancia DECIMAL(5,2) DEFAULT 10,
                        fecha_actualizacion TIMESTAMP DEFAULT NOW()
                    );
                    
                    INSERT INTO configuracion_global (id, margen_ganancia, fecha_actualizacion)
                    VALUES (1, 10, NOW())
                    ON CONFLICT (id) DO NOTHING;
                """)
            else:
                # SQLite
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS configuracion_global (
                        id INTEGER PRIMARY KEY,
                        margen_ganancia REAL DEFAULT 10,
                        fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                
                cursor.execute("""
                    INSERT OR IGNORE INTO configuracion_global (id, margen_ganancia, fecha_actualizacion)
                    VALUES (1, 10, CURRENT_TIMESTAMP);
                """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_fix_all_tables_columns'),
    ]

    operations = [
        migrations.RunPython(ensure_configuracion_table, migrations.RunPython.noop),
    ]
