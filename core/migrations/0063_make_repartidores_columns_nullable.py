# Generated migration to make repartidores columns nullable before renaming

from django.db import migrations
from django.conf import settings


def make_nullable(apps, schema_editor):
    """Hacer nullable las columnas antes de renombrar"""
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
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_fix_pedidos_facturas_enviadas'),
    ]

    operations = [
        migrations.RunPython(make_nullable, migrations.RunPython.noop),
    ]
