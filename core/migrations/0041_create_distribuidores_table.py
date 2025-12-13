# Generated migration to create distribuidores table using raw SQL

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_create_correos_pendientes_table'),
    ]

    def create_distribuidores_tables(apps, schema_editor):
        """Create distribuidores tables - compatible with PostgreSQL and SQLite"""
        with schema_editor.connection.cursor() as cursor:
            db_vendor = schema_editor.connection.vendor
            
            if db_vendor == 'postgresql':
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS distribuidores (
                        "idDistribuidor" BIGSERIAL PRIMARY KEY,
                        "nombreDistribuidor" varchar(30) NULL,
                        "contacto" varchar(100) NULL,
                        "telefono" varchar(20) NULL,
                        "email" varchar(254) NULL,
                        "direccion" varchar(255) NULL
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS distribuidor_producto (
                        "id" BIGSERIAL PRIMARY KEY,
                        "idDistribuidor" BIGINT NOT NULL,
                        "idProducto" BIGINT NOT NULL,
                        "precioCompra" numeric(10, 2) NOT NULL
                    );
                """)
            else:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS distribuidores (
                        "idDistribuidor" INTEGER PRIMARY KEY AUTOINCREMENT,
                        "nombreDistribuidor" varchar(30) NULL,
                        "contacto" varchar(100) NULL,
                        "telefono" varchar(20) NULL,
                        "email" varchar(254) NULL,
                        "direccion" varchar(255) NULL
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS distribuidor_producto (
                        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                        "idDistribuidor" integer NOT NULL,
                        "idProducto" integer NOT NULL,
                        "precioCompra" numeric(10, 2) NOT NULL
                    );
                """)

    def drop_distribuidores_tables(apps, schema_editor):
        """Drop distribuidores tables"""
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS distribuidor_producto;")
            cursor.execute("DROP TABLE IF EXISTS distribuidores;")

    operations = [
        migrations.RunPython(create_distribuidores_tables, drop_distribuidores_tables),
    ]
