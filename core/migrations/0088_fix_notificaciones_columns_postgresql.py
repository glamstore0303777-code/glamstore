# Generated migration to fix notificaciones_problema columns for PostgreSQL and SQLite

from django.db import migrations, models
from django.db import connection


def add_columns_if_not_exist(apps, schema_editor):
    """Add columns to notificaciones_problema if they don't exist"""
    with connection.cursor() as cursor:
        # Get database type
        db_vendor = connection.vendor
        
        if db_vendor == 'postgresql':
            # PostgreSQL approach
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
            # SQLite approach - check if columns exist first
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
    """Reverse operation - drop columns if they exist"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0087_ensure_notificaciones_columns'),
    ]

    operations = [
        migrations.RunPython(add_columns_if_not_exist, reverse_columns),
    ]
