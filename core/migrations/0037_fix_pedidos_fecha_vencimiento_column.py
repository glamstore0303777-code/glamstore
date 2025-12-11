# Generated migration to fix fecha_vencimiento column name in pedidos table

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_create_confirmacion_and_notificaciones_tables'),
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
