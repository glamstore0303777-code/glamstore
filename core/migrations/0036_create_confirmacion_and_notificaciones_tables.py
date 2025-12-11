# Generated migration to create confirmaciones_entrega and notificaciones tables

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_create_lotes_and_movimientos_lote_tables'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS confirmaciones_entrega (
                idconfirmacion SERIAL PRIMARY KEY,
                pedido_id BIGINT NOT NULL UNIQUE REFERENCES pedidos(idpedido) ON DELETE CASCADE,
                repartidor_id INTEGER REFERENCES repartidores(idrepartidor) ON DELETE SET NULL,
                foto_entrega VARCHAR(100),
                calificacion INTEGER DEFAULT 5,
                comentario TEXT,
                fecha_confirmacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS confirmaciones_entrega CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_problema (
                idnotificacion SERIAL PRIMARY KEY,
                idpedido BIGINT NOT NULL REFERENCES pedidos(idpedido) ON DELETE CASCADE,
                motivo TEXT NOT NULL,
                foto VARCHAR(100),
                fechareporte TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                leida BOOLEAN DEFAULT FALSE,
                respuesta_admin TEXT,
                fecha_respuesta TIMESTAMP
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS notificaciones_problema CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_reporte (
                idnotificacion SERIAL PRIMARY KEY,
                titulo VARCHAR(255) NOT NULL,
                contenido_html TEXT NOT NULL,
                tipo VARCHAR(50) DEFAULT 'DASHBOARD',
                fechacreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                leida BOOLEAN DEFAULT FALSE
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS notificaciones_reporte CASCADE;",
        ),
    ]
