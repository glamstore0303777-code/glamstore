# Migration to fix column case sensitivity issues in PostgreSQL
# PostgreSQL stores unquoted identifiers in lowercase, but Django models use camelCase

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_fix_db_column_case'),
    ]

    operations = [
        # Update Producto model db_columns
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.BigAutoField(db_column='idproducto', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(db_column='nombreproducto', max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidadDisponible',
            field=models.IntegerField(db_column='cantidaddisponible', default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaIngreso',
            field=models.DateTimeField(blank=True, db_column='fechaingreso', null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaVencimiento',
            field=models.DateField(blank=True, db_column='fechavencimiento', null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idCategoria',
            field=models.ForeignKey(db_column='idcategoria', db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idSubcategoria',
            field=models.ForeignKey(db_column='idsubcategoria', db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.subcategoria'),
        ),
        
        # Update Pedido model db_columns
        migrations.AlterField(
            model_name='pedido',
            name='idPedido',
            field=models.AutoField(db_column='idpedido', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fechaCreacion',
            field=models.DateTimeField(blank=True, db_column='fechacreacion', null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='idCliente',
            field=models.ForeignKey(blank=True, db_column='idcliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='idRepartidor',
            field=models.ForeignKey(blank=True, db_column='idrepartidor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor'),
        ),
        
        # Update DetallePedido model db_columns
        migrations.AlterField(
            model_name='detallepedido',
            name='idDetallePedido',
            field=models.AutoField(db_column='iddetallepedido', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='idPedido',
            field=models.ForeignKey(blank=True, db_column='idpedido', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pedido'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='idProducto',
            field=models.ForeignKey(blank=True, db_column='idproducto', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='precio_unitario',
            field=models.DecimalField(db_column='preciounitario', decimal_places=2, max_digits=10),
        ),
        
        # Update PedidoProducto model db_columns
        migrations.AlterField(
            model_name='pedidoproducto',
            name='idPedido',
            field=models.ForeignKey(blank=True, db_column='idpedido', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pedido'),
        ),
        migrations.AlterField(
            model_name='pedidoproducto',
            name='idProducto',
            field=models.ForeignKey(blank=True, db_column='idproducto', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
        
        # Update Repartidor model db_columns
        migrations.AlterField(
            model_name='repartidor',
            name='idRepartidor',
            field=models.AutoField(db_column='idrepartidor', primary_key=True, serialize=False),
        ),
    ]
