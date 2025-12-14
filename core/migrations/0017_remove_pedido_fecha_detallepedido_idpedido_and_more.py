# Generated migration - remove and add fields

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_pedido_facturas_enviadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fechaCreacion',
            field=models.DateTimeField(blank=True, db_column='fechacreacion', null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, db_column='fecha_vencimiento', null=True),
        ),
    ]
