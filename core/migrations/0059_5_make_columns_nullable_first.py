# Generated migration to make columns nullable BEFORE renaming

from django.db import migrations
from django.conf import settings


def make_nullable_first(apps, schema_editor):
    """Hacer nullable las columnas ANTES de cualquier operación"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                # PostgreSQL - hacer nullable primero
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
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_add_repartidores_columns'),
    ]

    operations = [
        migrations.RunPython(make_nullable_first, migrations.RunPython.noop),
    ]
