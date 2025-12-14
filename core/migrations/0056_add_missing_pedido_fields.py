# Generated migration - add missing fields to pedidos table

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_add_fecha_vencimiento_to_movimientos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True, db_column='fecha_vencimiento'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='facturas_enviadas',
            field=models.PositiveIntegerField(default=0, db_column='facturas_enviadas'),
        ),
    ]
