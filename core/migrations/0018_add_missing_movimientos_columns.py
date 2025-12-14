# Generated migration - add missing columns to MovimientoProducto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_pedido_fecha_detallepedido_idpedido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientoproducto',
            name='lote',
            field=models.CharField(blank=True, db_column='lote', help_text='Código del lote del producto', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movimientoproducto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, db_column='fecha_vencimiento', help_text='Fecha de vencimiento del producto', null=True),
        ),
        migrations.AddField(
            model_name='movimientoproducto',
            name='total_con_iva',
            field=models.DecimalField(blank=True, db_column='total_con_iva', decimal_places=2, help_text='Total incluyendo IVA', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='movimientoproducto',
            name='iva',
            field=models.DecimalField(blank=True, db_column='iva', decimal_places=2, help_text='Valor del IVA (19%)', max_digits=10, null=True),
        ),
    ]
