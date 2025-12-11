# Generated migration to create lotes_producto and movimientos_lote tables

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_create_movimientos_producto_table'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS lotes_producto (
                idlote SERIAL PRIMARY KEY,
                producto_id BIGINT NOT NULL REFERENCES productos(idproducto) ON DELETE CASCADE,
                codigo_lote VARCHAR(100) NOT NULL,
                fecha_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_vencimiento DATE,
                cantidad_inicial INTEGER NOT NULL,
                cantidad_disponible INTEGER NOT NULL,
                costo_unitario DECIMAL(10, 2) DEFAULT 0,
                precio_venta DECIMAL(10, 2) DEFAULT 0,
                total_con_iva DECIMAL(10, 2),
                iva DECIMAL(10, 2),
                proveedor VARCHAR(200),
                UNIQUE(producto_id, codigo_lote)
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS lotes_producto CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS movimientos_lote (
                idmovimientolote SERIAL PRIMARY KEY,
                lote_id INTEGER NOT NULL REFERENCES lotes_producto(idlote) ON DELETE CASCADE,
                movimiento_producto_id INTEGER NOT NULL REFERENCES movimientos_producto(idmovimiento) ON DELETE CASCADE,
                cantidad INTEGER NOT NULL,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS movimientos_lote CASCADE;",
        ),
    ]
