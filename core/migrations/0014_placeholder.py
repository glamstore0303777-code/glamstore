# Generated migration - placeholder for migration sequence
# This migration is a no-op to maintain migration history consistency

from django.db import migrations


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_detallepedido_options_alter_pedido_options_and_more'),
    ]

    operations = [
        migrations.RunPython(noop, migrations.RunPython.noop),
    ]
