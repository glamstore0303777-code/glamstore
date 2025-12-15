# Generated migration to ensure correos_pendientes table exists

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_fix_distribuidor_columns'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS correos_pendientes (
                id SERIAL PRIMARY KEY,
                id_pedido INTEGER,
                destinatario VARCHAR(255) NOT NULL,
                asunto VARCHAR(255) NOT NULL,
                contenido_html TEXT NOT NULL,
                contenido_texto TEXT,
                enviado BOOLEAN NOT NULL DEFAULT FALSE,
                intentos INTEGER NOT NULL DEFAULT 0,
                fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                fecha_envio TIMESTAMP,
                error TEXT
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS correos_pendientes CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE INDEX IF NOT EXISTS idx_correos_pendientes_enviado 
            ON correos_pendientes(enviado);
            """,
            reverse_sql="DROP INDEX IF EXISTS idx_correos_pendientes_enviado;",
        ),
    ]
