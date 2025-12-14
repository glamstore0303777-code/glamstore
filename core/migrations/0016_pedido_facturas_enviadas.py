# Generated migration - add facturas_enviadas field to Pedido

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_repartidor_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='facturas_enviadas',
            field=models.PositiveIntegerField(db_column='facturas_enviadas', default=0),
        ),
    ]
