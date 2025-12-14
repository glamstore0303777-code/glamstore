"""
Migration to fix column case sensitivity in detallepedido table.
PostgreSQL stores quoted identifiers with their original case.
"""
from django.db import migrations
from django.conf import settings


def fix_detallepedido_columns(apps, schema_editor):
    """Fix column case sensitivity - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    # Only run for PostgreSQL
    if 'postgresql' not in db_engine:
        return
    
    with connection.cursor() as cursor:
        try:
            # Try to rename columns
            cursor.execute('ALTER TABLE detallepedido RENAME COLUMN "precioUnitario" TO preciounitario;')
        except:
            pass
        
        try:
            cursor.execute('ALTER TABLE detallepedido RENAME COLUMN "idDetallePedido" TO iddetallepedido;')
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_drop_subcategoria_fk'),
    ]

    operations = [
        migrations.RunPython(fix_detallepedido_columns, migrations.RunPython.noop),
    ]
