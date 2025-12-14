"""
Migration to create movimientos_producto table if it doesn't exist.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_add_fechacreacion_column'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                -- Create movimientos_producto table if not exists
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
                
                -- Create loteproducto table if not exists (referenced by movimientos)
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
            """,
            reverse_sql="DROP TABLE IF EXISTS movimientos_producto; DROP TABLE IF EXISTS loteproducto;",
        ),
    ]
