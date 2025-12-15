# Generated migration to fix distribuidor table columns for PostgreSQL

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_ensure_notificaciones_table'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Asegurar que la tabla distribuidores tiene la estructura correcta
            CREATE TABLE IF NOT EXISTS distribuidores (
                idDistribuidor SERIAL PRIMARY KEY,
                nombreDistribuidor VARCHAR(30),
                contacto VARCHAR(20)
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS distribuidores CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            -- Asegurar que la tabla distribuidor_producto existe
            CREATE TABLE IF NOT EXISTS distribuidor_producto (
                id SERIAL PRIMARY KEY,
                idDistribuidor INTEGER NOT NULL REFERENCES distribuidores(idDistribuidor) ON DELETE CASCADE,
                idProducto VARCHAR(30)
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS distribuidor_producto CASCADE;",
        ),
    ]
