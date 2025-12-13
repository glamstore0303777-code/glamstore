# Generated migration - fix DetallePedido column names

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_fix_cliente_model'),
    ]

    operations = [
        # Rename precioUnitario to precio_unitario
        migrations.AlterField(
            model_name='detallepedido',
            name='precioUnitario',
            field=models.DecimalField(db_column='precio_unitario', decimal_places=2, max_digits=10),
        ),
        # Rename idPedido to use correct db_column
        migrations.AlterField(
            model_name='detallepedido',
            name='idPedido',
            field=models.ForeignKey(db_column='idpedido', on_delete=django.db.models.deletion.CASCADE, to='core.pedido', null=True, blank=True),
        ),
        # Rename idProducto to use correct db_column
        migrations.AlterField(
            model_name='detallepedido',
            name='idProducto',
            field=models.ForeignKey(db_column='idproducto', on_delete=django.db.models.deletion.CASCADE, to='core.producto', null=True, blank=True),
        ),
    ]
