# Generated migration to populate initial data for testing

from django.db import migrations
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta


def populate_data(apps, schema_editor):
    """Populate initial data for testing"""
    
    # Insert admin user
    with schema_editor.connection.cursor() as cursor:
        # Check if admin user already exists
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = ?", ['admin@glamstore.com'])
        if cursor.fetchone()[0] == 0:
            # Insert admin user
            hashed_password = make_password('admin123')
            cursor.execute("""
                INSERT INTO usuarios (email, password, id_rol, nombre, fechacreacion)
                VALUES (?, ?, ?, ?, ?)
            """, ['admin@glamstore.com', hashed_password, 1, 'Administrador', datetime.now()])
        
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
        
        # Insert sample products if they don't exist
        cursor.execute("SELECT COUNT(*) FROM producto")
        if cursor.fetchone()[0] == 0:
            # Get category IDs
            cursor.execute("SELECT idcategoria FROM categoria WHERE nombrecategoria = ?", ['Maquillaje'])
            cat_id = cursor.fetchone()[0]
            
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
