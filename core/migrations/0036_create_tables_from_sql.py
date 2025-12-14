# Generated migration - Create all tables from SQL

from django.db import migrations

def create_tables(apps, schema_editor):
    """Crear todas las tablas necesarias"""
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        idcategoria SERIAL PRIMARY KEY,
        nombrecategoria VARCHAR(20) NOT NULL,
        descripcion TEXT,
        imagen VARCHAR(100)
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS subcategorias (
        idsubcategoria SERIAL PRIMARY KEY,
        nombresubcategoria VARCHAR(50) NOT NULL,
        idcategoria INTEGER NOT NULL REFERENCES categorias(idcategoria)
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        idproducto BIGSERIAL PRIMARY KEY,
        nombreproducto VARCHAR(50) NOT NULL,
        precio NUMERIC(10, 2),
        stock INTEGER DEFAULT 0,
        descripcion TEXT,
        lote VARCHAR(100),
        cantidaddisponible INTEGER DEFAULT 0,
        fechaingreso TIMESTAMP,
        fechavencimiento DATE,
        idcategoria INTEGER REFERENCES categorias(idcategoria),
        idsubcategoria INTEGER REFERENCES subcategorias(idsubcategoria),
        imagen VARCHAR(100),
        precio_venta NUMERIC(10, 2) DEFAULT 0
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        idcliente SERIAL PRIMARY KEY,
        cedula VARCHAR(20),
        nombre VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        direccion VARCHAR(200),
        telefono VARCHAR(20)
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS repartidores (
        idrepartidor SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        telefono VARCHAR(20),
        email VARCHAR(100),
        estado VARCHAR(50)
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        idpedido SERIAL PRIMARY KEY,
        idcliente INTEGER REFERENCES clientes(idcliente),
        total NUMERIC(10, 2),
        estado VARCHAR(50),
        estado_pago VARCHAR(50),
        estado_pedido VARCHAR(50),
        fechacreacion TIMESTAMP,
        fecha_vencimiento DATE,
        facturas_enviadas BOOLEAN DEFAULT FALSE,
        idrepartidor INTEGER
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS detallepedido (
        iddetallepedido SERIAL PRIMARY KEY,
        idpedido INTEGER REFERENCES pedidos(idpedido),
        idproducto BIGINT REFERENCES productos(idproducto),
        cantidad INTEGER,
        precio_unitario NUMERIC(10, 2),
        subtotal NUMERIC(10, 2),
        margen_ganancia NUMERIC(5, 2)
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS movimientoproducto (
        idmovimiento SERIAL PRIMARY KEY,
        idproducto BIGINT,
        tipo_movimiento VARCHAR(50),
        cantidad INTEGER,
        precio_unitario INTEGER,
        costo_unitario INTEGER,
        stock_anterior INTEGER,
        stock_nuevo INTEGER,
        id_pedido INTEGER,
        lote VARCHAR(100),
        fecha_vencimiento DATE,
        total_con_iva INTEGER,
        iva INTEGER,
        descripcion TEXT,
        fecha_movimiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (idproducto) REFERENCES productos(idproducto),
        FOREIGN KEY (id_pedido) REFERENCES pedidos(idpedido)
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS loteproducto (
        idlote SERIAL PRIMARY KEY,
        idproducto BIGINT REFERENCES productos(idproducto),
        codigo_lote VARCHAR(100),
        cantidad_total INTEGER,
        cantidad_disponible INTEGER,
        costo_unitario NUMERIC(10, 2),
        fecha_entrada DATE,
        fecha_vencimiento DATE
    );
    """)
    
    schema_editor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        idusuario SERIAL PRIMARY KEY,
        email VARCHAR(255) UNIQUE,
        password VARCHAR(255),
        id_rol INTEGER,
        idcliente INTEGER,
        fechacreacion TIMESTAMP,
        nombre VARCHAR(50),
        telefono VARCHAR(20),
        direccion VARCHAR(50),
        reset_token VARCHAR(255),
        reset_token_expires TIMESTAMP,
        ultimoacceso TIMESTAMP
    );
    """)

def drop_tables(apps, schema_editor):
    """Eliminar tablas si es necesario"""
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_sync_models'),
    ]

    operations = [
        migrations.RunPython(create_tables, drop_tables),
    ]
