# Generated migration - create MovimientoProducto model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_categoria_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoProducto',
            fields=[
                ('idMovimiento', models.AutoField(db_column='idmovimiento', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True, db_column='fecha')),
                ('tipo_movimiento', models.CharField(choices=[('ENTRADA_INICIAL', 'Entrada Inicial'), ('AJUSTE_MANUAL_ENTRADA', 'Ajuste Manual (Entrada)'), ('AJUSTE_MANUAL_SALIDA', 'Ajuste Manual (Salida)'), ('SALIDA_VENTA', 'Salida por Venta'), ('EN_PREPARACION_SALIDA', 'En Preparación (Apartado)'), ('PERDIDA_VENCIMIENTO', 'Pérdida por Vencimiento')], db_column='tipo_movimiento', max_length=50)),
                ('cantidad', models.IntegerField(db_column='cantidad')),
                ('precio_unitario', models.DecimalField(db_column='precio_unitario', decimal_places=2, default=0, max_digits=10)),
                ('costo_unitario', models.DecimalField(db_column='costo_unitario', decimal_places=2, default=0, help_text='Costo por unidad para movimientos de entrada.', max_digits=10)),
                ('stock_anterior', models.IntegerField(db_column='stock_anterior')),
                ('stock_nuevo', models.IntegerField(db_column='stock_nuevo')),
                ('descripcion', models.CharField(blank=True, db_column='descripcion', max_length=255, null=True)),
                ('id_pedido', models.ForeignKey(blank=True, db_column='idpedido', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pedido')),
                ('producto', models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='core.producto')),
            ],
            options={
                'db_table': 'movimientos_producto',
                'app_label': 'core',
                'ordering': ['-fecha'],
            },
        ),
    ]
