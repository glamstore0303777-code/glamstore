# Generated migration - update Pedido model with new fields

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_detallepedido_margen_ganancia'),
    ]

    operations = [
        # Add idRepartidor field to Pedido
        migrations.AddField(
            model_name='pedido',
            name='idRepartidor',
            field=models.ForeignKey(blank=True, db_column='idrepartidor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor'),
        ),
    ]
