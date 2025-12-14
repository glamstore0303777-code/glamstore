"""
Migration to fix column case sensitivity in detallepedido table.
PostgreSQL stores quoted identifiers with their original case.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_drop_subcategoria_fk'),
    ]

    operations = [
        # Try to rename columns directly - PostgreSQL will ignore if column doesn't exist with that exact case
        migrations.RunSQL(
            sql='ALTER TABLE detallepedido RENAME COLUMN "precioUnitario" TO preciounitario;',
            reverse_sql='SELECT 1;',
        ),
    ]
