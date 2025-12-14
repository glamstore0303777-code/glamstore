# Generated migration to make repartidores columns nullable before renaming

from django.db import migrations
from django.conf import settings


def make_nullable(apps, schema_editor):
    """Hacer nullable las columnas antes de renombrar"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    if 'postgresql' in db_engine:
        # PostgreSQL - hacer nullable primero
        with connection.cursor() as cursor:
            # Verificar qué columnas existen
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = 'repartidores'
            """)
            columns = {row[0] for row in cursor.fetchall()}
        
        # Hacer cada operación en su propia transacción
        if 'nomberepartidor' in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ALTER COLUMN nomberepartidor DROP NOT NULL;
                    """)
            except Exception:
                pass
        
        if 'telefonoRepartidor' in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        ALTER COLUMN "telefonoRepartidor" DROP NOT NULL;
                    """)
            except Exception:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_add_repartidores_columns'),
    ]

    operations = [
        migrations.RunPython(make_nullable, migrations.RunPython.noop),
    ]
