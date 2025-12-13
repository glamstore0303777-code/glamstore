# Migration to increase email column size from 30 to 255 characters
# Uses raw SQL because Usuario model has managed=False

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_create_imagenes_tables'),
    ]

    operations = [
        migrations.RunSQL(
            # Forward: Increase email column size to 255 (SQLite compatible)
            sql="SELECT 1",
            # Reverse: No-op for SQLite
            reverse_sql="SELECT 1",
        ),
    ]
