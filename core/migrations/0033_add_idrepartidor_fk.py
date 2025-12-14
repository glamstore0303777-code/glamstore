# Generated migration - add ForeignKey constraint to idRepartidor

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_final_cleanup'),
    ]

    operations = [
        # Alter the idRepartidor field to add ForeignKey constraint
        migrations.AlterField(
            model_name='pedido',
            name='idRepartidor',
            field=models.ForeignKey(blank=True, db_column='idrepartidor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor'),
        ),
    ]
