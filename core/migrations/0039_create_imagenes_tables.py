from django.db import migrations, models
from django.db import connection


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_create_all_base_tables'),
    ]

    def create_imagenes_tables(apps, schema_editor):
        """Create imagenes tables compatible with both PostgreSQL and SQLite"""
        with schema_editor.connection.cursor() as cursor:
            db_vendor = schema_editor.connection.vendor
            
            if db_vendor == 'postgresql':
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS imagenes_productos (
                        id BIGSERIAL PRIMARY KEY,
                        id_producto BIGINT NOT NULL,
                        nombre_archivo VARCHAR(255) NOT NULL,
                        ruta VARCHAR(255) NOT NULL,
                        contenido BYTEA NOT NULL,
                        fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS imagenes_categorias (
                        id BIGSERIAL PRIMARY KEY,
                        id_categoria INTEGER NOT NULL,
                        nombre_archivo VARCHAR(255) NOT NULL,
                        ruta VARCHAR(255) NOT NULL,
                        contenido BYTEA NOT NULL,
                        fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
            else:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS imagenes_productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_producto INTEGER NOT NULL,
                        nombre_archivo VARCHAR(255) NOT NULL,
                        ruta VARCHAR(255) NOT NULL,
                        contenido BLOB NOT NULL,
                        fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS imagenes_categorias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_categoria INTEGER NOT NULL,
                        nombre_archivo VARCHAR(255) NOT NULL,
                        ruta VARCHAR(255) NOT NULL,
                        contenido BLOB NOT NULL,
                        fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

    def drop_imagenes_tables(apps, schema_editor):
        """Drop imagenes tables"""
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS imagenes_productos;")
            cursor.execute("DROP TABLE IF EXISTS imagenes_categorias;")

    operations = [
        migrations.RunPython(create_imagenes_tables, drop_imagenes_tables),
    ]
