"""
Migration to create ALL missing tables at once.
"""
from django.db import migrations
from django.conf import settings


def create_all_missing_tables(apps, schema_editor):
    """Create all missing tables - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS confirmaciones_entrega (
                        idconfirmacion SERIAL PRIMARY KEY,
                        pedido_id INTEGER UNIQUE,
                        repartidor_id INTEGER,
                        foto_entrega VARCHAR(255),
                        calificacion INTEGER DEFAULT 5,
                        comentario TEXT,
                        fecha_confirmacion TIMESTAMP DEFAULT NOW()
                    );
                    
                    CREATE TABLE IF NOT EXISTS notificacionproblema (
                        id SERIAL PRIMARY KEY,
                        pedido_id INTEGER,
                        cliente_id INTEGER,
                        tipo_problema VARCHAR(100),
                        descripcion TEXT,
                        estado VARCHAR(50) DEFAULT 'Pendiente',
                        fecha_reporte TIMESTAMP DEFAULT NOW(),
                        fecha_respuesta TIMESTAMP,
                        respuesta TEXT
                    );
                    
                    CREATE TABLE IF NOT EXISTS movimientolote (
                        id SERIAL PRIMARY KEY,
                        lote_id INTEGER,
                        tipo_movimiento VARCHAR(50),
                        cantidad INTEGER,
                        fecha TIMESTAMP DEFAULT NOW(),
                        pedido_id INTEGER,
                        descripcion VARCHAR(255)
                    );
                """)
            else:
                # SQLite version
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS confirmaciones_entrega (
                        idconfirmacion INTEGER PRIMARY KEY AUTOINCREMENT,
                        pedido_id INTEGER UNIQUE,
                        repartidor_id INTEGER,
                        foto_entrega VARCHAR(255),
                        calificacion INTEGER DEFAULT 5,
                        comentario TEXT,
                        fecha_confirmacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS notificacionproblema (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        pedido_id INTEGER,
                        cliente_id INTEGER,
                        tipo_problema VARCHAR(100),
                        descripcion TEXT,
                        estado VARCHAR(50) DEFAULT 'Pendiente',
                        fecha_reporte TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        fecha_respuesta TIMESTAMP,
                        respuesta TEXT
                    );
                """)
                
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS movimientolote (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        lote_id INTEGER,
                        tipo_movimiento VARCHAR(50),
                        cantidad INTEGER,
                        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        pedido_id INTEGER,
                        descripcion VARCHAR(255)
                    );
                """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_create_movimientos_producto_table'),
    ]

    operations = [
        migrations.RunPython(create_all_missing_tables, migrations.RunPython.noop),
    ]
