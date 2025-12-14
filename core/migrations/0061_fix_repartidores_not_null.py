# Generated migration to fix NOT NULL constraints in repartidores

from django.db import migrations
from django.conf import settings


def fix_not_null_constraints(apps, schema_editor):
    """Permitir NULL en columnas antiguas"""
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
            else:
                # SQLite - recrear tabla sin NOT NULL
                try:
                    cursor.execute("""
                        CREATE TABLE repartidores_temp AS
                        SELECT * FROM repartidores;
                    """)
                    
                    cursor.execute("""
                        DROP TABLE repartidores;
                    """)
                    
                    cursor.execute("""
                        CREATE TABLE repartidores (
                            idRepartidor INTEGER PRIMARY KEY AUTOINCREMENT,
                            nomberepartidor VARCHAR(100),
                            telefonoRepartidor VARCHAR(20),
                            email VARCHAR(100),
                            nombre VARCHAR(50),
                            telefono VARCHAR(20)
                        );
                    """)
                    
                    cursor.execute("""
                        INSERT INTO repartidores
                        SELECT * FROM repartidores_temp;
                    """)
                    
                    cursor.execute("""
                        DROP TABLE repartidores_temp;
                    """)
                except:
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
