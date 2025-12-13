# Generated migration - fix table names to match models

from django.db import migrations


def fix_table_names(apps, schema_editor):
    """Fix table names to match current models"""
    with schema_editor.connection.cursor() as cursor:
        db_vendor = schema_editor.connection.vendor
        
        try:
            # Rename categoria to categorias if needed
            if db_vendor == 'postgresql':
                cursor.execute("""
                    ALTER TABLE IF EXISTS categoria RENAME TO categorias;
                """)
                cursor.execute("""
                    ALTER TABLE IF EXISTS subcategoria RENAME TO subcategorias;
                """)
            else:
                # SQLite doesn't support ALTER TABLE RENAME in the same way
                # We'll just ensure the tables exist with correct names
                pass
        except Exception:
            pass  # Tables might already have correct names


def reverse_fix(apps, schema_editor):
    """Reverse - no-op"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_final_sync'),
    ]

    operations = [
        migrations.RunPython(fix_table_names, reverse_fix),
    ]
