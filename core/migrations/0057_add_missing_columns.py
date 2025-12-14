# Generated migration to add missing columns

from django.db import migrations, models
from django.conf import settings


def add_missing_columns(apps, schema_editor):
    """Agregar columnas faltantes si no existen"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                # PostgreSQL
                cursor.execute("""
                    ALTER TABLE notificacionproblema
                    ADD COLUMN IF NOT EXISTS foto VARCHAR(255);
                """)
                
                cursor.execute("""
                    ALTER TABLE loteproducto
                    ADD COLUMN IF NOT EXISTS codigo_lote VARCHAR(100);
                """)
            else:
                # SQLite
                cursor.execute("""
                    PRAGMA table_info(notificacionproblema);
                """)
                columns = [col[1] for col in cursor.fetchall()]
                if 'foto' not in columns:
                    cursor.execute("""
                        ALTER TABLE notificacionproblema
                        ADD COLUMN foto VARCHAR(255);
                    """)
                
                cursor.execute("""
                    PRAGMA table_info(loteproducto);
                """)
                columns = [col[1] for col in cursor.fetchall()]
                if 'codigo_lote' not in columns:
                    cursor.execute("""
                        ALTER TABLE loteproducto
                        ADD COLUMN codigo_lote VARCHAR(100);
                    """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_add_motivo_to_notificacionproblema'),
    ]

    operations = [
        migrations.RunPython(add_missing_columns, migrations.RunPython.noop),
    ]
