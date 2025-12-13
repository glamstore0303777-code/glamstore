# Generated migration to populate distribuidores table

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_populate_lotes_and_vencimiento'),
    ]

    def populate_distribuidores(apps, schema_editor):
        """Populate distribuidores - compatible with PostgreSQL and SQLite"""
        with schema_editor.connection.cursor() as cursor:
            db_vendor = schema_editor.connection.vendor
            
            if db_vendor == 'postgresql':
                cursor.execute("""
                    INSERT INTO distribuidores ("idDistribuidor", "nombreDistribuidor", "contacto") 
                    VALUES 
                    (1, 'Proveedor Central', '214748364'),
                    (7, 'Proveedor Central tt', '214748364755')
                    ON CONFLICT ("idDistribuidor") DO NOTHING;
                """)
            else:
                cursor.execute("""
                    INSERT OR IGNORE INTO distribuidores ("idDistribuidor", "nombreDistribuidor", "contacto") 
                    VALUES 
                    (1, 'Proveedor Central', '214748364'),
                    (7, 'Proveedor Central tt', '214748364755');
                """)

    def reverse_populate(apps, schema_editor):
        """Reverse - delete inserted rows"""
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM distribuidores WHERE "idDistribuidor" IN (1, 7);
            """)

    operations = [
        migrations.RunPython(populate_distribuidores, reverse_populate),
    ]
