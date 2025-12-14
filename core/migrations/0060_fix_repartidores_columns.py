# Generated migration to fix repartidores column names - SAFE VERSION

from django.db import migrations
from django.conf import settings


def fix_repartidores_columns(apps, schema_editor):
    """Renombrar columnas incorrectas en repartidores - versión segura"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                # PostgreSQL - verificar qué columnas existen PRIMERO
                cursor.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name = 'repartidores'
                    AND column_name IN ('nomberepartidor', 'nombre', 'telefonoRepartidor', 'telefono')
                """)
                existing_columns = {row[0] for row in cursor.fetchall()}
                
                # Solo hacer operaciones si es necesario
                if 'nomberepartidor' in existing_columns and 'nombre' not in existing_columns:
                    try:
                        cursor.execute("""
                            ALTER TABLE repartidores
                            RENAME COLUMN nomberepartidor TO nombre;
                        """)
                    except Exception as e:
                        # Ignorar si falla
                        pass
                
                if 'telefonoRepartidor' in existing_columns and 'telefono' not in existing_columns:
                    try:
                        cursor.execute("""
                            ALTER TABLE repartidores
                            RENAME COLUMN "telefonoRepartidor" TO telefono;
                        """)
                    except Exception as e:
                        # Ignorar si falla
                        pass
            else:
                # SQLite - copiar datos a las columnas correctas
                cursor.execute("""
                    PRAGMA table_info(repartidores);
                """)
                columns = {row[1] for row in cursor.fetchall()}
                
                if 'nomberepartidor' in columns and 'nombre' in columns:
                    try:
                        cursor.execute("""
                            UPDATE repartidores
                            SET nombre = nomberepartidor
                            WHERE nombre IS NULL;
                        """)
                    except:
                        pass
                
                if 'telefonoRepartidor' in columns and 'telefono' in columns:
                    try:
                        cursor.execute("""
                            UPDATE repartidores
                            SET telefono = telefonoRepartidor
                            WHERE telefono IS NULL;
                        """)
                    except:
                        pass
        except Exception as e:
            # Ignorar todos los errores
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_5_make_columns_nullable_first'),
    ]

    operations = [
        migrations.RunPython(fix_repartidores_columns, migrations.RunPython.noop),
    ]
