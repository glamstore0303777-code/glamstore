# Generated migration - alter Repartidor telefono field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_detallepedido_options_alter_pedido_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartidor',
            name='telefonoRepartidor',
            field=models.CharField(db_column='telefonoRepartidor', max_length=20, verbose_name='Teléfono'),
        ),
    ]
