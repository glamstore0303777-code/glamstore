# Generated migration to fix repartidores column names

from django.db import migrations
from django.conf import settings


def fix_repartidores_columns(apps, schema_editor):
    """Renombrar columnas incorrectas en repartidores"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                # PostgreSQL - renombrar columnas
                try:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        RENAME COLUMN "nomberepartidor" TO nombre;
                    """)
                except Exception as e:
                    # Columna ya existe o no existe, ignorar
                    pass
                
                try:
                    cursor.execute("""
                        ALTER TABLE repartidores
                        RENAME COLUMN "telefonoRepartidor" TO telefono;
                    """)
                except Exception as e:
                    # Columna ya existe o no existe, ignorar
                    pass
            else:
                # SQLite - copiar datos a las columnas correctas
                cursor.execute("""
                    PRAGMA table_info(repartidores);
                """)
                columns = {row[1]: row for row in cursor.fetchall()}
                
                # Si existen las columnas incorrectas, copiar datos a las correctas
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
            # Ignorar errores
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_add_repartidores_columns'),
    ]

    operations = [
        migrations.RunPython(fix_repartidores_columns, migrations.RunPython.noop),
    ]
