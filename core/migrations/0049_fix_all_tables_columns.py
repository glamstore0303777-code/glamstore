"""
Migration to fix ALL column case sensitivity issues across ALL tables.
"""
from django.db import migrations
from django.conf import settings


def fix_all_tables_columns(apps, schema_editor):
    """Fix column case sensitivity - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    # Only run for PostgreSQL
    if 'postgresql' not in db_engine:
        return
    
    with connection.cursor() as cursor:
        tables = ['productos', 'categorias', 'subcategorias', 
                  'pedidos', 'detallepedido', 'clientes', 
                  'repartidores', 'usuarios', 'distribuidores',
                  'pedidoproducto', 'movimientoproducto']
        
        for table in tables:
            try:
                # Get all columns with uppercase letters
                cursor.execute(f"""
                    SELECT attname 
                    FROM pg_attribute 
                    WHERE attrelid = '{table}'::regclass 
                    AND attnum > 0 
                    AND NOT attisdropped
                    AND attname ~ '[A-Z]'
                """)
                
                columns = cursor.fetchall()
                for (col,) in columns:
                    try:
                        cursor.execute(f'ALTER TABLE {table} RENAME COLUMN "{col}" TO {col.lower()};')
                    except:
                        pass
            except:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_fix_all_column_cases'),
    ]

    operations = [
        migrations.RunPython(fix_all_tables_columns, migrations.RunPython.noop),
    ]
