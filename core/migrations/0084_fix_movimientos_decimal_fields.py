from django.db import migrations, models
from django.db import connection


def fix_decimal_fields(apps, schema_editor):
    """Fix decimal fields for both SQLite and PostgreSQL"""
    with connection.cursor() as cursor:
        db_vendor = connection.vendor
        
        if db_vendor == 'postgresql':
            # PostgreSQL approach
            try:
                cursor.execute("""
                    ALTER TABLE movimientos_producto 
                    ALTER COLUMN precio_unitario TYPE NUMERIC(15, 2),
                    ALTER COLUMN costo_unitario TYPE NUMERIC(15, 2),
                    ALTER COLUMN iva TYPE NUMERIC(15, 2),
                    ALTER COLUMN total_con_iva TYPE NUMERIC(15, 2);
                """)
            except Exception as e:
                print(f"Error altering movimientos_producto: {e}")
            
            try:
                cursor.execute("""
                    ALTER TABLE lotes_producto 
                    ALTER COLUMN costo_unitario TYPE NUMERIC(15, 2),
                    ALTER COLUMN precio_venta TYPE NUMERIC(15, 2),
                    ALTER COLUMN total_con_iva TYPE NUMERIC(15, 2),
                    ALTER COLUMN iva TYPE NUMERIC(15, 2);
                """)
            except Exception as e:
                print(f"Error altering lotes_producto: {e}")
        
        elif db_vendor == 'sqlite':
            # SQLite doesn't support ALTER COLUMN TYPE, so we skip this
            # SQLite uses dynamic typing anyway
            print("SQLite doesn't require decimal field type changes")


def reverse_fix(apps, schema_editor):
    """Reverse operation"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_fix_movimientos_lote_column'),
    ]

    operations = [
        migrations.RunPython(fix_decimal_fields, reverse_fix),
    ]
