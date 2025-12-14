# Generated migration to fix notificaciones_problema.foto column on Render

from django.db import migrations
from django.conf import settings


def add_foto_column(apps, schema_editor):
    """Agregar columna foto a notificaciones_problema si no existe"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        if 'postgresql' in db_engine:
            # PostgreSQL - verificar si columna existe
            try:
                cursor.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name = 'notificaciones_problema' AND column_name = 'foto'
                """)
                if not cursor.fetchone():
                    # Columna no existe, agregarla
                    cursor.execute("""
                        ALTER TABLE notificaciones_problema
                        ADD COLUMN foto VARCHAR(255) NULL;
                    """)
            except Exception as e:
                print(f"Error adding foto column: {e}")
        else:
            # SQLite
            try:
                cursor.execute("PRAGMA table_info(notificaciones_problema);")
                columns = {row[1] for row in cursor.fetchall()}
                if 'foto' not in columns:
                    cursor.execute("""
                        ALTER TABLE notificaciones_problema
                        ADD COLUMN foto VARCHAR(255);
                    """)
            except Exception as e:
                print(f"Error adding foto column: {e}")


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_fix_missing_tables_and_columns'),
    ]

    operations = [
        migrations.RunPython(add_foto_column, migrations.RunPython.noop),
    ]
