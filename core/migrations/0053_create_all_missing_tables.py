"""
Migration to create ALL missing tables at once.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_create_movimientos_producto_table'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                -- Create confirmaciones_entrega table
                CREATE TABLE IF NOT EXISTS confirmaciones_entrega (
                    idconfirmacion SERIAL PRIMARY KEY,
                    pedido_id INTEGER UNIQUE,
                    repartidor_id INTEGER,
                    foto_entrega VARCHAR(255),
                    calificacion INTEGER DEFAULT 5,
                    comentario TEXT,
                    fecha_confirmacion TIMESTAMP DEFAULT NOW()
                );
                
                -- Create notificacionproblema table
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
                
                -- Create movimientolote table
                CREATE TABLE IF NOT EXISTS movimientolote (
                    id SERIAL PRIMARY KEY,
                    lote_id INTEGER,
                    tipo_movimiento VARCHAR(50),
                    cantidad INTEGER,
                    fecha TIMESTAMP DEFAULT NOW(),
                    pedido_id INTEGER,
                    descripcion VARCHAR(255)
                );
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
