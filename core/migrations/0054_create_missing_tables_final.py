from django.db import migrations

def create_tables(apps, schema_editor):
    """Crear todas las tablas faltantes en PostgreSQL"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        # Crear tabla notificaciones_problema si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notificaciones_problema (
                idnotificacion SERIAL PRIMARY KEY,
                idpedido INTEGER NOT NULL,
                descripcion TEXT,
                leida BOOLEAN DEFAULT FALSE,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_respuesta TIMESTAMP,
                respuesta TEXT,
                FOREIGN KEY (idpedido) REFERENCES pedidos(idpedido) ON DELETE CASCADE
            )
        """)
        
        # Crear tabla lotes_producto si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lotes_producto (
                idlote SERIAL PRIMARY KEY,
                idproducto INTEGER NOT NULL,
                numero_lote VARCHAR(100),
                fecha_entrada DATE,
                fecha_vencimiento DATE,
                cantidad_inicial INTEGER,
                cantidad_disponible INTEGER,
                costo_unitario DECIMAL(10, 2),
                FOREIGN KEY (idproducto) REFERENCES productos(idproducto) ON DELETE CASCADE
            )
        """)
        
        # Crear tabla repartidores si no existe (con columna nombre)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS repartidores (
                idrepartidor SERIAL PRIMARY KEY,
                nombre VARCHAR(255),
                nombrerepartidor VARCHAR(255),
                telefono VARCHAR(20),
                email VARCHAR(255),
                estado VARCHAR(50) DEFAULT 'activo',
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Crear tabla confirmaciones_entrega si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS confirmaciones_entrega (
                idconfirmacion SERIAL PRIMARY KEY,
                idpedido INTEGER NOT NULL,
                idrepartidor INTEGER,
                fecha_confirmacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                calificacion INTEGER,
                comentario TEXT,
                FOREIGN KEY (idpedido) REFERENCES pedidos(idpedido) ON DELETE CASCADE,
                FOREIGN KEY (idrepartidor) REFERENCES repartidores(idrepartidor) ON DELETE SET NULL
            )
        """)
        
        # Crear tabla movimientos_lote si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movimientos_lote (
                idmovimiento SERIAL PRIMARY KEY,
                idlote INTEGER NOT NULL,
                tipo_movimiento VARCHAR(50),
                cantidad INTEGER,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                descripcion TEXT,
                FOREIGN KEY (idlote) REFERENCES lotes_producto(idlote) ON DELETE CASCADE
            )
        """)

def reverse_tables(apps, schema_editor):
    """Revertir la creación de tablas"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS movimientos_lote CASCADE")
        cursor.execute("DROP TABLE IF EXISTS confirmaciones_entrega CASCADE")
        cursor.execute("DROP TABLE IF EXISTS lotes_producto CASCADE")
        cursor.execute("DROP TABLE IF EXISTS notificaciones_problema CASCADE")
        cursor.execute("DROP TABLE IF EXISTS repartidores CASCADE")

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_create_all_missing_tables'),
    ]

    operations = [
        migrations.RunPython(create_tables, reverse_tables),
    ]
