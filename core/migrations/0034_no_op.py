# Generated migration - no-op to clear migration state

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_add_idrepartidor_fk'),
    ]

    operations = [
        # No-op migration to clear Django's migration state
        migrations.RunPython(lambda apps, schema_editor: None, migrations.RunPython.noop),
    ]
