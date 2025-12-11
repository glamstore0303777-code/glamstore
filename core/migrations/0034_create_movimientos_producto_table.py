# Generated migration to create movimientos_producto table

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_create_configuracion_global_table'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS movimientos_producto (
                idmovimiento SERIAL PRIMARY KEY,
                producto_id BIGINT NOT NULL REFERENCES productos(idproducto) ON DELETE CASCADE,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                tipo_movimiento VARCHAR(50) NOT NULL,
                cantidad INTEGER NOT NULL,
                precio_unitario DECIMAL(10, 2) DEFAULT 0,
                costo_unitario DECIMAL(10, 2) DEFAULT 0,
                stock_anterior INTEGER NOT NULL,
                stock_nuevo INTEGER NOT NULL,
                idpedido BIGINT REFERENCES pedidos(idpedido) ON DELETE SET NULL,
                descripcion VARCHAR(255),
                lote VARCHAR(100),
                fecha_vencimiento DATE,
                total_con_iva DECIMAL(10, 2),
                iva DECIMAL(10, 2),
                lote_origen_id INTEGER REFERENCES lotes_producto(idlote) ON DELETE SET NULL
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS movimientos_producto CASCADE;",
        ),
    ]
