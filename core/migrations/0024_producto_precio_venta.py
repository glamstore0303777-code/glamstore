# Generated migration - add precio_venta field to Producto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_movimientoproducto_tipo_movimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_venta',
            field=models.DecimalField(db_column='precio_venta', decimal_places=2, default=0, help_text='Precio de venta calculado automáticamente', max_digits=10),
        ),
    ]
