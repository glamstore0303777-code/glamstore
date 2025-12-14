# Generated migration - add costo_unitario field to MovimientoProducto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_movimientoproducto_precio_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientoproducto',
            name='costo_unitario',
            field=models.DecimalField(db_column='costo_unitario', decimal_places=2, default=0, help_text='Costo por unidad para movimientos de entrada.', max_digits=10, verbose_name='Costo Unitario'),
        ),
    ]
