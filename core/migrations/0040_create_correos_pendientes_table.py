from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_create_imagenes_tables'),
    ]

    def create_correos_table(apps, schema_editor):
        """Create correos_pendientes table - compatible with PostgreSQL and SQLite"""
        with schema_editor.connection.cursor() as cursor:
            db_vendor = schema_editor.connection.vendor
            
            if db_vendor == 'postgresql':
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS correos_pendientes (
                        id BIGSERIAL PRIMARY KEY,
                        id_pedido BIGINT NOT NULL,
                        destinatario VARCHAR(255) NOT NULL,
                        asunto VARCHAR(255) NOT NULL,
                        contenido_html TEXT NOT NULL,
                        contenido_texto TEXT NOT NULL,
                        enviado BOOLEAN DEFAULT FALSE,
                        intentos INTEGER DEFAULT 0,
                        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        fecha_envio TIMESTAMP NULL,
                        error TEXT NULL
                    );
                """)
            else:
                cursor.execute("""
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
                """)

    def drop_correos_table(apps, schema_editor):
        """Drop correos_pendientes table"""
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS correos_pendientes;")

    operations = [
        migrations.RunPython(create_correos_table, drop_correos_table),
    ]
