from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_detallepedido_margen_ganancia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=20)),
                ('descripcion', models.TextField(null=True)),
            ],
            options={
                'db_table': 'categorias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('idSubcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreSubcategoria', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'subcategorias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('lote', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidadDisponible', models.IntegerField(default=0)),
                ('fechaIngreso', models.DateTimeField(auto_now_add=True)),
                ('fechaVencimiento', models.DateField(blank=True, null=True)),
                ('imagen', models.CharField(blank=True, max_length=255, null=True)),
                ('precio_venta', models.DecimalField(decimal_places=2, default=0, help_text='Precio de venta calculado automáticamente', max_digits=10)),
                ('margen_ganancia', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'db_table': 'productos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('estado', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'pedidos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('idDetalle', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'detallepedido',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pedidoproducto',
                'managed': True,
            },
        ),
    ]
