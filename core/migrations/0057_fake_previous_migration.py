# Fake the previous migration since the column already exists

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_mark_migration_as_fake'),
    ]

    operations = [
        # No operations - this just marks the migration history
    ]
