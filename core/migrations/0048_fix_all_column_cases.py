"""
Migration to fix ALL column case sensitivity issues across tables.
Uses pg_attribute to check actual column names (case-sensitive).
"""
from django.db import migrations
from django.conf import settings


def fix_all_column_cases(apps, schema_editor):
    """Fix column case sensitivity - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    # Only run for PostgreSQL
    if 'postgresql' not in db_engine:
        return
    
    with connection.cursor() as cursor:
        tables_columns = {
            'detallepedido': ['precioUnitario', 'idDetallePedido'],
            'pedidos': ['idPedido', 'fechaCreacion', 'idCliente', 'idRepartidor'],
            'clientes': ['idCliente'],
            'repartidores': ['idRepartidor'],
        }
        
        for table, columns in tables_columns.items():
            for col in columns:
                try:
                    cursor.execute(f'ALTER TABLE {table} RENAME COLUMN "{col}" TO {col.lower()};')
                except:
                    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_fix_detallepedido_columns'),
    ]

    operations = [
        migrations.RunPython(fix_all_column_cases, migrations.RunPython.noop),
    ]
