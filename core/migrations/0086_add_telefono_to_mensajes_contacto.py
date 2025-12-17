# Generated migration to add telefono column to mensajes_contacto

from django.db import migrations, models
from django.db import connection


def add_telefono_column(apps, schema_editor):
    """Add telefono column to mensajes_contacto if it doesn't exist"""
    with connection.cursor() as cursor:
        db_vendor = connection.vendor
        
        if db_vendor == 'postgresql':
            try:
                cursor.execute("""
                    ALTER TABLE mensajes_contacto 
                    ADD COLUMN IF NOT EXISTS telefono VARCHAR(20);
                """)
            except Exception as e:
                print(f"Column telefono might already exist: {e}")
        
        elif db_vendor == 'sqlite':
            # SQLite approach
            cursor.execute("PRAGMA table_info(mensajes_contacto)")
            columns = {row[1] for row in cursor.fetchall()}
            
            if 'telefono' not in columns:
                try:
                    cursor.execute("""
                        ALTER TABLE mensajes_contacto 
                        ADD COLUMN telefono VARCHAR(20);
                    """)
                except Exception as e:
                    print(f"Error adding telefono: {e}")


def reverse_column(apps, schema_editor):
    """Reverse operation"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0085_fix_movimientos_lote_column'),
    ]

    operations = [
        migrations.RunPython(add_telefono_column, reverse_column),
    ]
