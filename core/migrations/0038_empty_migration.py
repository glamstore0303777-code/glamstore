# Migración vacía para resolver conflictos de estado

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_fix_column_names_case'),
    ]

    operations = [
    ]
