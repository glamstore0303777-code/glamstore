# Migration to increase email column size from 30 to 255 characters
# Uses raw SQL because Usuario model has managed=False

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_create_imagenes_tables'),
    ]

    operations = [
        migrations.RunSQL(
            # Forward: Increase email column size to 255
            sql="ALTER TABLE usuarios ALTER COLUMN email TYPE VARCHAR(255);",
            # Reverse: Decrease email column size back to 30
            reverse_sql="ALTER TABLE usuarios ALTER COLUMN email TYPE VARCHAR(30);",
        ),
    ]
