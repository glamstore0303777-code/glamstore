#!/usr/bin/env python
import os
import django
from django.conf import settings
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

# Datos de ejemplo para categorias
CATEGORIAS = [
    (1, 'Maquillaje', 'Productos de maquillaje profesional', None),
    (2, 'Skincare', 'Cuidado de la piel', None),
    (3, 'Accesorios', 'Accesorios de belleza', None),
]

# Datos de ejemplo para subcategorias
SUBCATEGORIAS = [
    (1, 'Base', 1),
    (2, 'Labios', 1),
    (3, 'Ojos', 1),
    (4, 'Limpieza', 2),
    (5, 'Hidratacion', 2),
]

# Datos de ejemplo para productos
PRODUCTOS = [
    (1, 'Base Liquida', 25000, 50, 'Base liquida de larga duracion', None, 50, None, None, 1, 1, None, 29750),
    (2, 'Labial Rojo', 15000, 100, 'Labial rojo intenso', None, 100, None, None, 1, 2, None, 17850),
    (3, 'Sombra Dorada', 12000, 75, 'Sombra dorada brillante', None, 75, None, None, 1, 3, None, 14280),
    (4, 'Limpiador Facial', 18000, 60, 'Limpiador facial suave', None, 60, None, None, 2, 4, None, 21420),
    (5, 'Crema Hidratante', 22000, 40, 'Crema hidratante intensiva', None, 40, None, None, 2, 5, None, 26180),
]

try:
    with connection.cursor() as cursor:
        # Insertar categorias
        for cat in CATEGORIAS:
            cursor.execute(
                'INSERT INTO categorias ("idCategoria", "nombreCategoria", "descripcion", "imagen") VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING',
                cat
            )
        
        # Insertar subcategorias
        for subcat in SUBCATEGORIAS:
            cursor.execute(
                'INSERT INTO subcategorias ("idSubcategoria", "nombreSubcategoria", "idCategoria") VALUES (%s, %s, %s) ON CONFLICT DO NOTHING',
                subcat
            )
        
        # Insertar productos
        for prod in PRODUCTOS:
            cursor.execute(
                '''INSERT INTO productos 
                ("idProducto", "nombreProducto", "precio", "stock", "descripcion", "lote", "cantidadDisponible", 
                "fechaIngreso", "fechaVencimiento", "idCategoria", "idSubcategoria", "imagen", "precio_venta") 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING''',
                prod
            )
    
    print("Datos restaurados exitosamente")
except Exception as e:
    print(f"Error al restaurar datos: {e}")
