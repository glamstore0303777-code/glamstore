# Generated migration - add precio_unitario field to MovimientoProducto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_movimientoproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientoproducto',
            name='precio_unitario',
            field=models.DecimalField(db_column='precio_unitario', decimal_places=2, default=0, max_digits=10, verbose_name='Precio Unitario'),
        ),
    ]
