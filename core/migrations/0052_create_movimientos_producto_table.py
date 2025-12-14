"""
Migration to create movimientos_producto table if it doesn't exist.
"""
from django.db import migrations
from django.conf import settings


def create_movimientos_producto_table(apps, schema_editor):
    """Create movimientos_producto table - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS movimientos_producto (
                        idmovimiento SERIAL PRIMARY KEY,
                        producto_id BIGINT REFERENCES productos(idproducto) ON DELETE CASCADE,
                        fecha TIMESTAMP DEFAULT NOW(),
                        tipo_movimiento VARCHAR(50),
                        cantidad INTEGER,
                        precio_unitario DECIMAL(10,2) DEFAULT 0,
                        costo_unitario DECIMAL(10,2) DEFAULT 0,
                        stock_anterior INTEGER,
                        stock_nuevo INTEGER,
                        idpedido INTEGER NULL,
                        descripcion VARCHAR(255),
                        lote VARCHAR(100),
                        fecha_vencimiento DATE,
                        total_con_iva DECIMAL(10,2),
                        iva DECIMAL(10,2),
                        lote_origen_id INTEGER NULL
                    );
                    
                    CREATE TABLE IF NOT EXISTS loteproducto (
                        id SERIAL PRIMARY KEY,
                        producto_id BIGINT REFERENCES productos(idproducto) ON DELETE CASCADE,
                        codigo_lote VARCHAR(100),
                        cantidad_inicial INTEGER DEFAULT 0,
                        cantidad_disponible INTEGER DEFAULT 0,
                        costo_unitario DECIMAL(10,2) DEFAULT 0,
                        fecha_ingreso TIMESTAMP DEFAULT NOW(),
                        fecha_vencimiento DATE,
                        activo BOOLEAN DEFAULT TRUE
                    );
                """)
            else:
                # SQLite version
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS movimientos_producto (
                        idmovimiento INTEGER PRIMARY KEY AUTOINCREMENT,
                        producto_id INTEGER REFERENCES productos(idproducto) ON DELETE CASCADE,
                        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        tipo_movimiento VARCHAR(50),
                        cantidad INTEGER,
                        precio_unitario REAL DEFAULT 0,
                        costo_unitario REAL DEFAULT 0,
                        stock_anterior INTEGER,
                        stock_nuevo INTEGER,
                        idpedido INTEGER NULL,
                        descripcion VARCHAR(255),
                        lote VARCHAR(100),
                        fecha_vencimiento DATE,
                        total_con_iva REAL,
                        iva REAL,
                        lote_origen_id INTEGER NULL
                    );
                """)
                
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS loteproducto (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        producto_id INTEGER REFERENCES productos(idproducto) ON DELETE CASCADE,
                        codigo_lote VARCHAR(100),
                        cantidad_inicial INTEGER DEFAULT 0,
                        cantidad_disponible INTEGER DEFAULT 0,
                        costo_unitario REAL DEFAULT 0,
                        fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        fecha_vencimiento DATE,
                        activo BOOLEAN DEFAULT 1
                    );
                """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_add_fechacreacion_column'),
    ]

    operations = [
        migrations.RunPython(create_movimientos_producto_table, migrations.RunPython.noop),
    ]
