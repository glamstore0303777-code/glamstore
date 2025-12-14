# Generated migration - update Pedido model with new fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_detallepedido_margen_ganancia'),
    ]

    operations = [
        # Add idRepartidor field to Pedido as integer first (no FK constraint yet)
        migrations.AddField(
            model_name='pedido',
            name='idRepartidor',
            field=models.IntegerField(blank=True, db_column='idrepartidor', null=True),
        ),
    ]
