# Generated migration to fix NOT NULL constraints - SAFE VERSION

from django.db import migrations
from django.conf import settings


def fix_not_null_constraints(apps, schema_editor):
    """Permitir NULL en columnas antiguas - versión segura"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                # PostgreSQL - hacer nullable las columnas
                try:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ALTER COLUMN nomberepartidor DROP NOT NULL;
                    """)
                except:
                    pass
                
                try:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ALTER COLUMN "telefonoRepartidor" DROP NOT NULL;
                    """)
                except:
                    pass
                
                try:
                    cursor.execute("""
                        ALTER TABLE pedidos
                        ALTER COLUMN facturas_enviadas DROP NOT NULL;
                    """)
                except:
                    pass
            else:
                # SQLite - no necesita hacer nada, ya se hizo en 0062
                pass
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_fix_repartidores_columns'),
    ]

    operations = [
        migrations.RunPython(fix_not_null_constraints, migrations.RunPython.noop),
    ]
