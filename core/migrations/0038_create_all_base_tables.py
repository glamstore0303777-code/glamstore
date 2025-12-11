# Generated migration to fix fecha_vencimiento column name in pedidos table

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_fix_pedidos_fecha_vencimiento_column'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            ALTER TABLE pedidos RENAME COLUMN IF EXISTS fecha_vencimiento TO fechavencimiento;
            """,
            reverse_sql="""
            ALTER TABLE pedidos RENAME COLUMN IF EXISTS fechavencimiento TO fecha_vencimiento;
            """,
        ),
    ]
