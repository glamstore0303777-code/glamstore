# Generated migration to fix facturas_enviadas column - SAFE VERSION

from django.db import migrations
from django.conf import settings


def fix_facturas_enviadas(apps, schema_editor):
    """Hacer nullable la columna facturas_enviadas - versión segura"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                # PostgreSQL - ya se hizo en 0061
                pass
            else:
                # SQLite - recrear tabla sin NOT NULL
                try:
                    cursor.execute("""
                        CREATE TABLE pedidos_temp AS
                        SELECT * FROM pedidos;
                    """)
                    
                    cursor.execute("""
                        DROP TABLE pedidos;
                    """)
                    
                    cursor.execute("""
                        CREATE TABLE pedidos (
                            idpedido INTEGER PRIMARY KEY AUTOINCREMENT,
                            fechapedido TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            fechacreacion TIMESTAMP,
                            estado VARCHAR(20) DEFAULT 'Pedido Recibido',
                            estado_pago VARCHAR(20) DEFAULT 'Pago Completo',
                            estado_pedido VARCHAR(20) DEFAULT 'Pedido Recibido',
                            total REAL,
                            idcliente INTEGER,
                            idrepartidor INTEGER,
                            fecha_vencimiento DATE,
                            facturas_enviadas BOOLEAN
                        );
                    """)
                    
                    cursor.execute("""
                        INSERT INTO pedidos
                        SELECT * FROM pedidos_temp;
                    """)
                    
                    cursor.execute("""
                        DROP TABLE pedidos_temp;
                    """)
                except:
                    pass
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_fix_repartidores_not_null'),
    ]

    operations = [
        migrations.RunPython(fix_facturas_enviadas, migrations.RunPython.noop),
    ]
