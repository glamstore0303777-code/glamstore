# Generated migration - add margen_ganancia field to Producto (temporary)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_cliente_distribuidor_distribuidorproducto_repartidor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='margen_ganancia',
            field=models.DecimalField(db_column='margen_ganancia', decimal_places=2, default=10, help_text='Margen de ganancia para este producto', max_digits=5),
        ),
    ]
