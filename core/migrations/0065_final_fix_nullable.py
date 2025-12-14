# Generated migration to ensure all columns are nullable

from django.db import migrations
from django.conf import settings


def final_fix_nullable(apps, schema_editor):
    """Asegurar que todas las columnas problemáticas sean nullable"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    if 'postgresql' in db_engine:
        # PostgreSQL - hacer nullable todas las columnas problemáticas
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    ALTER TABLE repartidores
                    ALTER COLUMN nomberepartidor DROP NOT NULL;
                """)
        except Exception:
            pass
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    ALTER TABLE repartidores
                    ALTER COLUMN "telefonoRepartidor" DROP NOT NULL;
                """)
        except Exception:
            pass
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    ALTER TABLE pedidos
                    ALTER COLUMN facturas_enviadas DROP NOT NULL;
                """)
        except Exception:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_smart_fix_repartidores'),
    ]

    operations = [
        migrations.RunPython(final_fix_nullable, migrations.RunPython.noop),
    ]
