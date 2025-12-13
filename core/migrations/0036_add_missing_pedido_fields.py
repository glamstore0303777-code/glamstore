# Generated migration - add missing Pedido fields

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_fix_producto_columns'),
    ]

    operations = [
        # Add missing fields to Pedido if they don't exist
        migrations.AddField(
            model_name='pedido',
            name='fechaCreacion',
            field=models.DateTimeField(blank=True, db_column='fechacreacion', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_pago',
            field=models.CharField(choices=[('Pago Completo', 'Pago Completo'), ('Pago Parcial', 'Pago Parcial')], db_column='estado_pago', default='Pago Completo', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('Pedido Recibido', 'Pedido Recibido'), ('Pago Confirmado', 'Pago Confirmado'), ('En Preparación', 'En Preparación'), ('En Camino', 'En Camino'), ('Entregado', 'Entregado'), ('Completado', 'Completado'), ('Problema en Entrega', 'Problema en Entrega')], db_column='estado_pedido', default='Pedido Recibido', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='idRepartidor',
            field=models.ForeignKey(blank=True, db_column='idrepartidor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, db_column='fecha_vencimiento', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='facturas_enviadas',
            field=models.PositiveIntegerField(db_column='facturas_enviadas', default=0),
            preserve_default=True,
        ),
    ]
