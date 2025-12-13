# Migration to increase email column size from 30 to 255 characters
# Uses raw SQL because Usuario model has managed=False

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_create_imagenes_tables'),
    ]

    def alter_email_column(apps, schema_editor):
        """Alter email column size - compatible with PostgreSQL and SQLite"""
        with schema_editor.connection.cursor() as cursor:
            db_vendor = schema_editor.connection.vendor
            
            try:
                if db_vendor == 'postgresql':
                    cursor.execute("""
                        ALTER TABLE usuarios 
                        ALTER COLUMN email TYPE VARCHAR(255);
                    """)
                # SQLite doesn't support ALTER COLUMN, so we skip it
            except Exception:
                pass  # Column might already be correct size

    def reverse_alter_email(apps, schema_editor):
        """Reverse - no-op for both databases"""
        pass

    operations = [
        migrations.RunPython(alter_email_column, reverse_alter_email),
    ]
