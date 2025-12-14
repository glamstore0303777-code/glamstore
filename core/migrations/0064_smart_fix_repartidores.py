# Generated migration to intelligently fix repartidores columns

from django.db import migrations
from django.conf import settings


def smart_fix_repartidores(apps, schema_editor):
    """Arreglar repartidores de forma inteligente"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    if 'postgresql' in db_engine:
        # PostgreSQL - verificar qué columnas existen
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = 'repartidores'
            """)
            columns = {row[0] for row in cursor.fetchall()}
        
        # Si nomberepartidor existe y nombre no, renombrar
        if 'nomberepartidor' in columns and 'nombre' not in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        RENAME COLUMN nomberepartidor TO nombre;
                    """)
            except Exception:
                pass
        
        # Si telefonoRepartidor existe y telefono no, renombrar
        if 'telefonoRepartidor' in columns and 'telefono' not in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        RENAME COLUMN "telefonoRepartidor" TO telefono;
                    """)
            except Exception:
                pass
        
        # Si ambas columnas existen, copiar datos de las antiguas a las nuevas
        if 'nomberepartidor' in columns and 'nombre' in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE repartidores
                        SET nombre = nomberepartidor
                        WHERE nombre IS NULL AND nomberepartidor IS NOT NULL;
                    """)
            except Exception:
                pass
        
        if 'telefonoRepartidor' in columns and 'telefono' in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE repartidores
                        SET telefono = "telefonoRepartidor"
                        WHERE telefono IS NULL AND "telefonoRepartidor" IS NOT NULL;
                    """)
            except Exception:
                pass
    else:
        # SQLite
        with connection.cursor() as cursor:
            cursor.execute("""
                PRAGMA table_info(repartidores);
            """)
            columns = {row[1] for row in cursor.fetchall()}
        
        if 'nomberepartidor' in columns and 'nombre' in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE repartidores
                        SET nombre = nomberepartidor
                        WHERE nombre IS NULL;
                    """)
            except Exception:
                pass
        
        if 'telefonoRepartidor' in columns and 'telefono' in columns:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE repartidores
                        SET telefono = telefonoRepartidor
                        WHERE telefono IS NULL;
                    """)
            except Exception:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_make_repartidores_columns_nullable'),
    ]

    operations = [
        migrations.RunPython(smart_fix_repartidores, migrations.RunPython.noop),
    ]
