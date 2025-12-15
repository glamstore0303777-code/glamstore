# Generated migration to ensure notificaciones_problema table exists

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_add_cedula_to_cliente'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_problema (
                idnotificacion SERIAL PRIMARY KEY,
                idpedido INTEGER NOT NULL REFERENCES pedidos(idpedido) ON DELETE CASCADE,
                motivo TEXT,
                foto VARCHAR(100),
                fechareporte TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                leida BOOLEAN NOT NULL DEFAULT FALSE,
                respuesta_admin TEXT,
                fecha_respuesta TIMESTAMP
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS notificaciones_problema CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE INDEX IF NOT EXISTS idx_notificaciones_problema_idpedido 
            ON notificaciones_problema(idpedido);
            """,
            reverse_sql="DROP INDEX IF EXISTS idx_notificaciones_problema_idpedido;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE INDEX IF NOT EXISTS idx_notificaciones_problema_leida 
            ON notificaciones_problema(leida);
            """,
            reverse_sql="DROP INDEX IF EXISTS idx_notificaciones_problema_leida;",
        ),
    ]
