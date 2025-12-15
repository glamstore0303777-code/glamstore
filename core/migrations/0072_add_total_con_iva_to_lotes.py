# Generated migration to add total_con_iva column to lotes_producto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_add_precio_venta_to_lotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='loteproducto',
            name='total_con_iva',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='loteproducto',
            name='iva',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
