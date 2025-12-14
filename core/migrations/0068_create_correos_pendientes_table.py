# Generated migration to create correos_pendientes table

from django.db import migrations
from django.conf import settings


def create_correos_pendientes_table(apps, schema_editor):
    """Crear tabla correos_pendientes si no existe"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        if 'postgresql' in db_engine:
            # PostgreSQL
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS correos_pendientes (
                        id SERIAL PRIMARY KEY,
                        id_pedido INTEGER NOT NULL,
                        destinatario VARCHAR(255) NOT NULL,
                        asunto VARCHAR(255) NOT NULL,
                        contenido_html TEXT NOT NULL,
                        contenido_texto TEXT,
                        enviado BOOLEAN DEFAULT FALSE,
                        intentos INTEGER DEFAULT 0,
                        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        fecha_envio TIMESTAMP NULL,
                        error TEXT NULL
                    );
                """)
            except Exception as e:
                print(f"Error creating correos_pendientes table: {e}")
        else:
            # SQLite
            try:
                cursor.execute("PRAGMA table_info(correos_pendientes);")
                if not cursor.fetchall():
                    cursor.execute("""
                        CREATE TABLE correos_pendientes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_pedido INTEGER NOT NULL,
                            destinatario VARCHAR(255) NOT NULL,
                            asunto VARCHAR(255) NOT NULL,
                            contenido_html TEXT NOT NULL,
                            contenido_texto TEXT,
                            enviado BOOLEAN DEFAULT 0,
                            intentos INTEGER DEFAULT 0,
                            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            fecha_envio TIMESTAMP NULL,
                            error TEXT NULL
                        );
                    """)
            except Exception as e:
                print(f"Error creating correos_pendientes table: {e}")


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_fix_notificaciones_foto_column'),
    ]

    operations = [
        migrations.RunPython(create_correos_pendientes_table, migrations.RunPython.noop),
    ]
