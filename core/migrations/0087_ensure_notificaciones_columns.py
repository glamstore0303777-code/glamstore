# Generated migration to ensure notificaciones_problema columns exist

from django.db import migrations, models
from django.db import connection


def ensure_columns_exist(apps, schema_editor):
    """Ensure columns exist in notificaciones_problema"""
    with connection.cursor() as cursor:
        db_vendor = connection.vendor
        
        if db_vendor == 'postgresql':
            try:
                cursor.execute("""
                    ALTER TABLE notificaciones_problema 
                    ADD COLUMN IF NOT EXISTS respuesta_admin TEXT;
                """)
            except Exception as e:
                print(f"Column respuesta_admin might already exist: {e}")
            
            try:
                cursor.execute("""
                    ALTER TABLE notificaciones_problema 
                    ADD COLUMN IF NOT EXISTS fecha_respuesta TIMESTAMP;
                """)
            except Exception as e:
                print(f"Column fecha_respuesta might already exist: {e}")
        
        elif db_vendor == 'sqlite':
            # SQLite approach
            cursor.execute("PRAGMA table_info(notificaciones_problema)")
            columns = {row[1] for row in cursor.fetchall()}
            
            if 'respuesta_admin' not in columns:
                try:
                    cursor.execute("""
                        ALTER TABLE notificaciones_problema 
                        ADD COLUMN respuesta_admin TEXT;
                    """)
                except Exception as e:
                    print(f"Error adding respuesta_admin: {e}")
            
            if 'fecha_respuesta' not in columns:
                try:
                    cursor.execute("""
                        ALTER TABLE notificaciones_problema 
                        ADD COLUMN fecha_respuesta DATETIME;
                    """)
                except Exception as e:
                    print(f"Error adding fecha_respuesta: {e}")


def reverse_columns(apps, schema_editor):
    """Reverse operation"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_add_telefono_to_mensajes_contacto'),
    ]

    operations = [
        migrations.RunPython(ensure_columns_exist, reverse_columns),
    ]
