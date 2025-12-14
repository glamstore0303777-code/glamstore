# Generated migration - alter Repartidor telefono field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cliente_distribuidor_distribuidorproducto_repartidor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartidor',
            name='telefonoRepartidor',
            field=models.CharField(db_column='telefonoRepartidor', max_length=20, verbose_name='Teléfono'),
        ),
    ]
