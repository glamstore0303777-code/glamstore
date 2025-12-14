# Generated migration to add precio_venta field to LoteProducto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_add_fecha_vencimiento_to_movimientos'),
    ]

    operations = [
        migrations.AddField(
            model_name='loteproducto',
            name='precio_venta',
            field=models.DecimalField(db_column='precio_venta', decimal_places=2, default=0, max_digits=10),
        ),
    ]
