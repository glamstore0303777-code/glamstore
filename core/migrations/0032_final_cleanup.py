# Generated migration - final cleanup and placeholder migrations

from django.db import migrations


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_update_pedido_model'),
    ]

    operations = [
        # Placeholder for 0014 and 0023 that were removed
        migrations.RunPython(noop, migrations.RunPython.noop),
    ]
