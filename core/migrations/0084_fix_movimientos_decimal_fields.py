from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_fix_movimientos_lote_column'),
    ]

    operations = [
        # Cambiar campos de movimientos_producto a tipos más grandes
        migrations.RunSQL(
            sql="""
            ALTER TABLE movimientos_producto 
            ALTER COLUMN precio_unitario TYPE NUMERIC(15, 2),
            ALTER COLUMN costo_unitario TYPE NUMERIC(15, 2),
            ALTER COLUMN iva TYPE NUMERIC(15, 2),
            ALTER COLUMN total_con_iva TYPE NUMERIC(15, 2);
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        
        # Cambiar campos de lotes_producto a tipos más grandes
        migrations.RunSQL(
            sql="""
            ALTER TABLE lotes_producto 
            ALTER COLUMN costo_unitario TYPE NUMERIC(15, 2),
            ALTER COLUMN precio_venta TYPE NUMERIC(15, 2),
            ALTER COLUMN total_con_iva TYPE NUMERIC(15, 2),
            ALTER COLUMN iva TYPE NUMERIC(15, 2);
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
