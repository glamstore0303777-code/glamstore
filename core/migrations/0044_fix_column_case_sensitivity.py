# Migration to fix column case sensitivity issues in PostgreSQL
# PostgreSQL stores unquoted identifiers in lowercase, but Django models use camelCase
# This migration is a no-op because the database already has lowercase columns

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_fix_db_column_case'),
    ]

    operations = [
        # This is a no-op migration. The database already has lowercase columns.
        # The model definitions have been updated to use lowercase db_column values.
    ]
