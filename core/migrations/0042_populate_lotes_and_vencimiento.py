# Generated migration to populate lotes and fechaVencimiento for products

from django.db import migrations
from datetime import datetime, timedelta


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_create_distribuidores_table'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            UPDATE productos 
            SET lote = 'L2025-12' 
            WHERE lote IS NULL OR lote = '';
            """,
            reverse_sql="UPDATE productos SET lote = NULL WHERE lote = 'L2025-12';",
            state_operations=[]
        ),
        migrations.RunSQL(
            sql="""
            UPDATE productos 
            SET fechavencimiento = CURRENT_DATE + INTERVAL '730 days'
            WHERE fechavencimiento IS NULL;
            """,
            reverse_sql="UPDATE productos SET fechavencimiento = NULL WHERE fechavencimiento > CURRENT_DATE;",
            state_operations=[]
        ),
    ]
