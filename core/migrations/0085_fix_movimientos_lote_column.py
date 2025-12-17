# Generated migration to fix movimientos_lote.lote_id column

from django.db import migrations, models
from django.db import connection
import django.db.models.deletion


def fix_lote_id_column(apps, schema_editor):
    """Fix lote_id column for both SQLite and PostgreSQL"""
    with connection.cursor() as cursor:
        db_vendor = connection.vendor
        
        if db_vendor == 'postgresql':
            # PostgreSQL approach
            try:
                cursor.execute("""
                    ALTER TABLE movimientos_lote 
                    ADD COLUMN IF NOT EXISTS lote_id INTEGER;
                """)
            except Exception as e:
                print(f"Column lote_id might already exist: {e}")
            
            try:
                cursor.execute("""
                    UPDATE movimientos_lote 
                    SET lote_id = idlote 
                    WHERE lote_id IS NULL AND idlote IS NOT NULL;
                """)
            except Exception as e:
                print(f"Error updating lote_id: {e}")
        
        elif db_vendor == 'sqlite':
            # SQLite approach
            cursor.execute("PRAGMA table_info(movimientos_lote)")
            columns = {row[1] for row in cursor.fetchall()}
            
            if 'lote_id' not in columns:
                try:
                    cursor.execute("""
                        ALTER TABLE movimientos_lote 
                        ADD COLUMN lote_id INTEGER;
                    """)
                except Exception as e:
                    print(f"Error adding lote_id: {e}")
            
            try:
                cursor.execute("""
                    UPDATE movimientos_lote 
                    SET lote_id = idlote 
                    WHERE lote_id IS NULL AND idlote IS NOT NULL;
                """)
            except Exception as e:
                print(f"Error updating lote_id: {e}")


def reverse_fix(apps, schema_editor):
    """Reverse operation"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_fix_movimientos_decimal_fields'),
    ]

    operations = [
        migrations.RunPython(fix_lote_id_column, reverse_fix),
    ]
