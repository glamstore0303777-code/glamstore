# Generated migration to add precio_venta column

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_movimientoproducto_tipo_movimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_venta',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Precio de venta calculado automáticamente', max_digits=10),
        ),
    ]
