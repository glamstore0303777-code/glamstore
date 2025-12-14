# Generated migration - alter model options

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_add_estado_fields_sql'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallepedido',
            options={'ordering': ['idPedido'], 'verbose_name': 'Detalle Pedido', 'verbose_name_plural': 'Detalles Pedido'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-fechaPedido'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
    ]
