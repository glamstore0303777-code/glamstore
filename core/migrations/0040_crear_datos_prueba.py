# Migración para crear datos de prueba (categorías, subcategorías y productos)

from django.db import migrations
from django.utils import timezone
from datetime import timedelta

def crear_datos_prueba(apps, schema_editor):
    """Crear datos de prueba para la tienda usando SQL directo"""
    from django.db import connection
    from django.conf import settings
    
    db_engine = settings.DATABASES['default']['ENGINE']
    fecha_vencimiento = (timezone.now() + timedelta(days=365)).date()
    
    with connection.cursor() as cursor:
        # Crear categorías
        if 'postgresql' in db_engine:
            cursor.execute("SELECT COUNT(*) FROM categorias WHERE idcategoria = 1")
        else:
            cursor.execute("SELECT COUNT(*) FROM categorias WHERE idcategoria = 1")
        
        if cursor.fetchone()[0] == 0:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    INSERT INTO categorias (idcategoria, nombrecategoria, descripcion)
                    VALUES (1, %s, %s)
                """, ['Belleza', 'Productos de belleza y cuidado personal'])
                cursor.execute("""
                    INSERT INTO categorias (idcategoria, nombrecategoria, descripcion)
                    VALUES (2, %s, %s)
                """, ['Cuidado', 'Productos de cuidado de la piel'])
            else:
                cursor.execute("""
                    INSERT INTO categorias (idcategoria, nombrecategoria, descripcion)
                    VALUES (1, ?, ?)
                """, ['Belleza', 'Productos de belleza y cuidado personal'])
                cursor.execute("""
                    INSERT INTO categorias (idcategoria, nombrecategoria, descripcion)
                    VALUES (2, ?, ?)
                """, ['Cuidado', 'Productos de cuidado de la piel'])
        
        # Crear subcategorías
        if 'postgresql' in db_engine:
            cursor.execute("SELECT COUNT(*) FROM subcategorias WHERE idsubcategoria = 1")
        else:
            cursor.execute("SELECT COUNT(*) FROM subcategorias WHERE idsubcategoria = 1")
        
        if cursor.fetchone()[0] == 0:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    INSERT INTO subcategorias (idsubcategoria, nombresubcategoria, idcategoria)
                    VALUES (1, %s, 1)
                """, ['Maquillaje'])
                cursor.execute("""
                    INSERT INTO subcategorias (idsubcategoria, nombresubcategoria, idcategoria)
                    VALUES (2, %s, 2)
                """, ['Skincare'])
            else:
                cursor.execute("""
                    INSERT INTO subcategorias (idsubcategoria, nombresubcategoria, idcategoria)
                    VALUES (1, ?, 1)
                """, ['Maquillaje'])
                cursor.execute("""
                    INSERT INTO subcategorias (idsubcategoria, nombresubcategoria, idcategoria)
                    VALUES (2, ?, 2)
                """, ['Skincare'])
        
        # Crear productos
        productos_prueba = [
            ('Labial Rojo', 15000, 50, 'Labial de larga duración color rojo intenso', 1, 1),
            ('Crema Facial', 25000, 30, 'Crema hidratante para todo tipo de piel', 2, 2),
            ('Base de Maquillaje', 35000, 40, 'Base líquida de cobertura media', 1, 1),
            ('Sérum Vitamina C', 45000, 25, 'Sérum antioxidante con vitamina C', 2, 2),
        ]
        
        for nombre, precio, stock, desc, cat_id, subcat_id in productos_prueba:
            precio_venta = int(precio * 1.19 * 1.1 / 50) * 50
            
            if 'postgresql' in db_engine:
                cursor.execute("""
                    INSERT INTO productos (nombreproducto, precio, stock, descripcion, 
                                          cantidaddisponible, fechaingreso, fechavencimiento, 
                                          idcategoria, idsubcategoria, precio_venta)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT DO NOTHING
                """, [nombre, precio, stock, desc, stock, timezone.now(), fecha_vencimiento, cat_id, subcat_id, precio_venta])
            else:
                cursor.execute("""
                    INSERT OR IGNORE INTO productos (nombreproducto, precio, stock, descripcion, 
                                                     cantidaddisponible, fechaingreso, fechavencimiento, 
                                                     idcategoria, idsubcategoria, precio_venta)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, [nombre, precio, stock, desc, stock, timezone.now(), fecha_vencimiento, cat_id, subcat_id, precio_venta])

def revertir(apps, schema_editor):
    """Revertir la creación de datos de prueba"""
    from django.db import connection
    from django.conf import settings

    db_engine = settings.DATABASES['default']['ENGINE']

    with connection.cursor() as cursor:
        # Eliminar en orden inverso por dependencias
        if 'postgresql' in db_engine:
            cursor.execute(
                "DELETE FROM productos WHERE nombreproducto IN (%s, %s, %s, %s)",
                ['Labial Rojo', 'Crema Facial', 'Base de Maquillaje', 'Sérum Vitamina C']
            )
            cursor.execute("DELETE FROM subcategorias WHERE idsubcategoria IN (1, 2)")
            cursor.execute("DELETE FROM categorias WHERE idcategoria IN (1, 2)")
        else:
            cursor.execute(
                "DELETE FROM productos WHERE nombreproducto IN (?, ?, ?, ?)",
                ['Labial Rojo', 'Crema Facial', 'Base de Maquillaje', 'Sérum Vitamina C']
            )
            cursor.execute("DELETE FROM subcategorias WHERE idsubcategoria IN (1, 2)")
            cursor.execute("DELETE FROM categorias WHERE idcategoria IN (1, 2)")

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_crear_usuario_admin'),
    ]

    operations = [
        migrations.RunPython(crear_datos_prueba, revertir),
    ]
