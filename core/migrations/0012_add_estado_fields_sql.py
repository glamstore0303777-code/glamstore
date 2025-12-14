# Generated migration - add estado fields to Pedido

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_notificacionproblema_fecha_respuesta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado_pago',
            field=models.CharField(choices=[('Pago Completo', 'Pago Completo'), ('Pago Parcial', 'Pago Parcial')], db_column='estado_pago', default='Pago Completo', max_length=20),
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('Pedido Recibido', 'Pedido Recibido'), ('Pago Confirmado', 'Pago Confirmado'), ('En Preparación', 'En Preparación'), ('En Camino', 'En Camino'), ('Entregado', 'Entregado'), ('Completado', 'Completado'), ('Problema en Entrega', 'Problema en Entrega')], db_column='estado_pedido', default='Pedido Recibido', max_length=20),
        ),
    ]
