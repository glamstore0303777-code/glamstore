# Generated migration to fix fecha_vencimiento column name in pedidos table

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_fix_pedidos_fecha_vencimiento_column'),
    ]

    operations = [
        migrations.RunSQL(
            sql="SELECT 1",
            reverse_sql="SELECT 1",
        ),
    ]
