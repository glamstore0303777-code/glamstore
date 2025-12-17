from django.db import migrations
from django.db import connection


def add_column_if_not_exists(apps, schema_editor):
    """Add column to movimientos_lote if it doesn't exist"""
    with connection.cursor() as cursor:
        db_vendor = connection.vendor
        
        if db_vendor == 'postgresql':
            try:
                cursor.execute("""
                    ALTER TABLE movimientos_lote 
                    ADD COLUMN IF NOT EXISTS movimiento_producto_id INTEGER;
                """)
            except Exception as e:
                print(f"Column might already exist: {e}")
        
        elif db_vendor == 'sqlite':
            # SQLite approach - check if column exists first
            cursor.execute("PRAGMA table_info(movimientos_lote)")
            columns = {row[1] for row in cursor.fetchall()}
            
            if 'movimiento_producto_id' not in columns:
                try:
                    cursor.execute("""
                        ALTER TABLE movimientos_lote 
                        ADD COLUMN movimiento_producto_id INTEGER;
                    """)
                except Exception as e:
                    print(f"Error adding column: {e}")


def reverse_column(apps, schema_editor):
    """Reverse operation"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_ensure_mensajes_contacto_table'),
    ]

    operations = [
        migrations.RunPython(add_column_if_not_exists, reverse_column),
    ]
