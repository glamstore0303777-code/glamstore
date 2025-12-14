# Generated migration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_add_fecha_vencimiento_to_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacionproblema',
            name='motivo',
            field=models.TextField(null=True, blank=True, db_column='motivo'),
        ),
    ]
