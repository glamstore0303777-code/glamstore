# Generated migration - final synchronization

from django.db import migrations


def final_sync(apps, schema_editor):
    """Final synchronization of all data"""
    # This is a no-op migration that ensures all previous migrations have run
    pass


def reverse_sync(apps, schema_editor):
    """Reverse - no-op"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_update_pedido_model'),
    ]

    operations = [
        migrations.RunPython(final_sync, reverse_sync),
    ]
