# Generated migration to create all base tables

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_create_lotes_and_movimientos_lote_tables'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS repartidores (
                idrepartidor SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                telefono VARCHAR(20),
                email VARCHAR(100),
                estado VARCHAR(50) DEFAULT 'Activo'
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS repartidores CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS clientes (
                idcliente BIGSERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                cedula VARCHAR(20),
                telefono VARCHAR(20),
                direccion TEXT
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS clientes CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS categorias (
                idcategoria SERIAL PRIMARY KEY,
                nombrecategoria VARCHAR(20) NOT NULL,
                descripcion TEXT,
                imagen VARCHAR(100)
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS categorias CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS subcategorias (
                idsubcategoria SERIAL PRIMARY KEY,
                nombresubcategoria VARCHAR(50) NOT NULL,
                descripcion TEXT,
                idcategoria INTEGER REFERENCES categorias(idcategoria) ON DELETE CASCADE
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS subcategorias CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS productos (
                idproducto BIGSERIAL PRIMARY KEY,
                nombreproducto VARCHAR(50) NOT NULL,
                precio DECIMAL(10, 2) NOT NULL,
                stock INTEGER DEFAULT 0,
                descripcion TEXT,
                lote VARCHAR(100),
                cantidaddisponible INTEGER DEFAULT 0,
                fechaingreso TIMESTAMP,
                fechavencimiento DATE,
                idcategoria INTEGER REFERENCES categorias(idcategoria) ON DELETE SET NULL,
                idsubcategoria INTEGER REFERENCES subcategorias(idsubcategoria) ON DELETE SET NULL,
                imagen VARCHAR(100),
                precio_venta DECIMAL(10, 2) DEFAULT 0
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS productos CASCADE;",
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS pedidos (
                idpedido BIGSERIAL PRIMARY KEY,
                fechacreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                estado VARCHAR(50) DEFAULT 'En Preparacion',
                estado_pedido VARCHAR(50) DEFAULT 'En Preparacion',
                estado_pago VARCHAR(50) DEFAULT 'Pendiente',
                total DECIMAL(10, 2) DEFAULT 0,
                idcliente BIGINT NOT NULL REFERENCES clientes(idcliente) ON DELETE CASCADE,
                fechavencimiento DATE,
                idrepartidor INTEGER REFERENCES repartidores(idrepartidor) ON DELETE SET NULL,
                facturasEnviadas INTEGER DEFAULT 0
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS pedidos CASCADE;",
        ),
    ]
