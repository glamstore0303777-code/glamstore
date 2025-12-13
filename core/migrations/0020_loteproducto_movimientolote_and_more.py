# Generated migration - create lotes_producto and movimientos_lote tables

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_confirmacionentrega'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoteProducto',
            fields=[
                ('idLote', models.AutoField(db_column='idlote', primary_key=True, serialize=False)),
                ('codigo_lote', models.CharField(db_column='codigo_lote', help_text='Código único del lote', max_length=100)),
                ('fecha_entrada', models.DateTimeField(auto_now_add=True, db_column='fecha_entrada')),
                ('fecha_vencimiento', models.DateField(blank=True, db_column='fecha_vencimiento', null=True)),
                ('cantidad_inicial', models.IntegerField(db_column='cantidad_inicial', help_text='Cantidad inicial del lote')),
                ('cantidad_disponible', models.IntegerField(db_column='cantidad_disponible', help_text='Cantidad disponible actual')),
                ('costo_unitario', models.DecimalField(db_column='costo_unitario', decimal_places=2, default=0, max_digits=10)),
                ('precio_venta', models.DecimalField(db_column='precio_venta', decimal_places=2, default=0, max_digits=10)),
                ('total_con_iva', models.DecimalField(blank=True, db_column='total_con_iva', decimal_places=2, max_digits=10, null=True)),
                ('iva', models.DecimalField(blank=True, db_column='iva', decimal_places=2, max_digits=10, null=True)),
                ('proveedor', models.CharField(blank=True, db_column='proveedor', max_length=200, null=True)),
                ('producto', models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='core.producto')),
            ],
            options={
                'db_table': 'lotes_producto',
                'app_label': 'core',
                'ordering': ['fecha_entrada'],
            },
        ),
        migrations.CreateModel(
            name='MovimientoLote',
            fields=[
                ('idMovimientoLote', models.AutoField(db_column='idmovimientolote', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(db_column='cantidad', help_text='Cantidad tomada de este lote')),
                ('fecha', models.DateTimeField(auto_now_add=True, db_column='fecha')),
                ('lote', models.ForeignKey(db_column='lote_id', on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='core.loteproducto')),
                ('movimiento_producto', models.ForeignKey(db_column='movimiento_producto_id', on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_lote', to='core.movimientoproducto')),
            ],
            options={
                'db_table': 'movimientos_lote',
                'app_label': 'core',
                'ordering': ['-fecha'],
            },
        ),
        migrations.AddConstraint(
            model_name='loteproducto',
            constraint=models.UniqueConstraint(fields=['producto', 'codigo_lote'], name='unique_producto_codigo_lote'),
        ),
    ]
