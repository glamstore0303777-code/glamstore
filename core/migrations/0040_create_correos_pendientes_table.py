from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_create_imagenes_tables'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS correos_pendientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER NOT NULL,
                destinatario VARCHAR(255) NOT NULL,
                asunto VARCHAR(255) NOT NULL,
                contenido_html TEXT NOT NULL,
                contenido_texto TEXT NOT NULL,
                enviado BOOLEAN DEFAULT 0,
                intentos INTEGER DEFAULT 0,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_envio TIMESTAMP NULL,
                error TEXT NULL
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS correos_pendientes;"
        ),
    ]
