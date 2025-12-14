# Generated migration - sync models state

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_no_op'),
    ]

    operations = [
        # Sync models state - no actual database changes needed
        migrations.RunPython(lambda apps, schema_editor: None, migrations.RunPython.noop),
    ]
