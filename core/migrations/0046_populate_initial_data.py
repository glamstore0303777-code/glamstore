# Generated migration to create usuarios table and populate initial data

from django.db import migrations
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta


def populate_data(apps, schema_editor):
    """Create usuarios table and populate initial data"""
    
    with schema_editor.connection.cursor() as cursor:
        # Create usuarios table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255),
                id_rol INTEGER NOT NULL,
                idcliente INTEGER,
                fechacreacion TIMESTAMP,
                nombre VARCHAR(50),
                telefono VARCHAR(20),
                direccion VARCHAR(50),
                reset_token VARCHAR(255),
                reset_token_expires TIMESTAMP,
                ultimoacceso TIMESTAMP
            )
        """)
        
        # Insert admin user
        hashed_password = make_password('admin123')
        cursor.execute("""
            INSERT OR IGNORE INTO usuarios (email, password, id_rol, nombre, fechacreacion)
            VALUES (?, ?, ?, ?, ?)
        """, ['admin@glamstore.com', hashed_password, 1, 'Administrador', datetime.now()])
        
        # Create categoria table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categoria (
                idcategoria INTEGER PRIMARY KEY AUTOINCREMENT,
                nombrecategoria VARCHAR(50),
                descripcion TEXT,
                imagen VARCHAR(100)
            )
        """)
        
        # Insert categories if they don't exist
        cursor.execute("SELECT COUNT(*) FROM categoria")
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO categoria (nombrecategoria, descripcion)
                VALUES (?, ?)
            """, ['Maquillaje', 'Productos de maquillaje'])
            
            cursor.execute("""
                INSERT INTO categoria (nombrecategoria, descripcion)
                VALUES (?, ?)
            """, ['Skincare', 'Productos para el cuidado de la piel'])
            
            cursor.execute("""
                INSERT INTO categoria (nombrecategoria, descripcion)
                VALUES (?, ?)
            """, ['Accesorios', 'Accesorios de belleza'])
        
        # Create producto table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS producto (
                idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombreproducto VARCHAR(100),
                descripcion TEXT,
                precio INTEGER,
                stock INTEGER,
                idcategoria INTEGER,
                precio_venta INTEGER,
                lote VARCHAR(50),
                fechavencimiento DATE
            )
        """)
        
        # Insert sample products if they don't exist
        cursor.execute("SELECT COUNT(*) FROM producto")
        if cursor.fetchone()[0] == 0:
            # Get category ID for Maquillaje
            cursor.execute("SELECT idcategoria FROM categoria WHERE nombrecategoria = ?", ['Maquillaje'])
            result = cursor.fetchone()
            if result:
                cat_id = result[0]
                
                cursor.execute("""
                    INSERT INTO producto (nombreproducto, descripcion, precio, stock, idcategoria, precio_venta, lote, fechavencimiento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, ['Labial Rojo', 'Labial de larga duración', 25000, 50, cat_id, 29750, 'L2025-01', (datetime.now() + timedelta(days=365)).date()])
                
                cursor.execute("""
                    INSERT INTO producto (nombreproducto, descripcion, precio, stock, idcategoria, precio_venta, lote, fechavencimiento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, ['Base de Maquillaje', 'Base líquida profesional', 35000, 30, cat_id, 41650, 'L2025-01', (datetime.now() + timedelta(days=365)).date()])
                
                cursor.execute("""
                    INSERT INTO producto (nombreproducto, descripcion, precio, stock, idcategoria, precio_venta, lote, fechavencimiento)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, ['Sombra de Ojos', 'Paleta de sombras 12 colores', 45000, 25, cat_id, 53550, 'L2025-01', (datetime.now() + timedelta(days=365)).date()])


def reverse_populate(apps, schema_editor):
    """Reverse the population"""
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE email = ?", ['admin@glamstore.com'])
        cursor.execute("DELETE FROM producto WHERE nombreproducto IN (?, ?, ?)", 
                      ['Labial Rojo', 'Base de Maquillaje', 'Sombra de Ojos'])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_merge_20251213_1701'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_populate),
    ]
