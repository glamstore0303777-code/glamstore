# Migration to fix db_column case sensitivity issues

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_sync_models'),
    ]

    operations = [
    ]
