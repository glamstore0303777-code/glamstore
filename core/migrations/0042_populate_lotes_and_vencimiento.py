# Generated migration to populate lotes and fechaVencimiento for products

from django.db import migrations
from datetime import datetime, timedelta


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_create_distribuidores_table'),
    ]

    def populate_lotes_and_vencimiento(apps, schema_editor):
        """Populate lotes and fechavencimiento - compatible with PostgreSQL and SQLite"""
        with schema_editor.connection.cursor() as cursor:
            db_vendor = schema_editor.connection.vendor
            
            # Update lote
            cursor.execute("""
                UPDATE productos 
                SET lote = 'L2025-12' 
                WHERE lote IS NULL OR lote = '';
            """)
            
            # Update fechavencimiento
            if db_vendor == 'postgresql':
                cursor.execute("""
                    UPDATE productos 
                    SET fechavencimiento = CURRENT_DATE + INTERVAL '730 days'
                    WHERE fechavencimiento IS NULL;
                """)
            else:
                cursor.execute("""
                    UPDATE productos 
                    SET fechavencimiento = date('now', '+730 days')
                    WHERE fechavencimiento IS NULL;
                """)

    def reverse_populate(apps, schema_editor):
        """Reverse - no-op"""
        pass

    operations = [
        migrations.RunPython(populate_lotes_and_vencimiento, reverse_populate),
    ]
