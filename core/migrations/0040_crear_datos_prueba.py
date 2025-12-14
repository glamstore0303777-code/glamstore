# Migración para crear datos de prueba (categorías, subcategorías y productos)

from django.db import migrations
from django.utils import timezone
from datetime import timedelta

def crear_datos_prueba(apps, schema_editor):
    """Crear datos de prueba para la tienda"""
    Categoria = apps.get_model('core', 'Categoria')
    Subcategoria = apps.get_model('core', 'Subcategoria')
    Producto = apps.get_model('core', 'Producto')
    
    # Crear categorías si no existen
    cat_belleza, _ = Categoria.objects.get_or_create(
        idCategoria=1,
        defaults={
            'nombreCategoria': 'Belleza',
            'descripcion': 'Productos de belleza y cuidado personal'
        }
    )
    
    cat_cuidado, _ = Categoria.objects.get_or_create(
        idCategoria=2,
        defaults={
            'nombreCategoria': 'Cuidado',
            'descripcion': 'Productos de cuidado de la piel'
        }
    )
    
    # Crear subcategorías si no existen
    subcat_maquillaje, _ = Subcategoria.objects.get_or_create(
        idSubcategoria=1,
        defaults={
            'nombreSubcategoria': 'Maquillaje',
            'idCategoria': cat_belleza
        }
    )
    
    subcat_skincare, _ = Subcategoria.objects.get_or_create(
        idSubcategoria=2,
        defaults={
            'nombreSubcategoria': 'Skincare',
            'idCategoria': cat_cuidado
        }
    )
    
    # Crear productos de prueba si no existen
    fecha_vencimiento = timezone.now().date() + timedelta(days=365)
    
    productos_prueba = [
        {
            'nombreProducto': 'Labial Rojo',
            'precio': 15000,
            'stock': 50,
            'descripcion': 'Labial de larga duración color rojo intenso',
            'idCategoria': cat_belleza,
            'idSubcategoria': subcat_maquillaje,
        },
        {
            'nombreProducto': 'Crema Facial',
            'precio': 25000,
            'stock': 30,
            'descripcion': 'Crema hidratante para todo tipo de piel',
            'idCategoria': cat_cuidado,
            'idSubcategoria': subcat_skincare,
        },
        {
            'nombreProducto': 'Base de Maquillaje',
            'precio': 35000,
            'stock': 40,
            'descripcion': 'Base líquida de cobertura media',
            'idCategoria': cat_belleza,
            'idSubcategoria': subcat_maquillaje,
        },
        {
            'nombreProducto': 'Sérum Vitamina C',
            'precio': 45000,
            'stock': 25,
            'descripcion': 'Sérum antioxidante con vitamina C',
            'idCategoria': cat_cuidado,
            'idSubcategoria': subcat_skincare,
        },
    ]
    
    for prod_data in productos_prueba:
        Producto.objects.get_or_create(
            nombreProducto=prod_data['nombreProducto'],
            defaults={
                'precio': prod_data['precio'],
                'stock': prod_data['stock'],
                'descripcion': prod_data['descripcion'],
                'idCategoria': prod_data['idCategoria'],
                'idSubcategoria': prod_data['idSubcategoria'],
                'cantidadDisponible': prod_data['stock'],
                'fechaIngreso': timezone.now(),
                'fechaVencimiento': fecha_vencimiento,
                'precio_venta': int(prod_data['precio'] * 1.19 * 1.1 / 50) * 50,  # Precio con IVA y margen
            }
        )

def revertir(apps, schema_editor):
    """Revertir la creación de datos de prueba"""
    Producto = apps.get_model('core', 'Producto')
    Subcategoria = apps.get_model('core', 'Subcategoria')
    Categoria = apps.get_model('core', 'Categoria')
    
    # Eliminar en orden inverso por dependencias
    Producto.objects.filter(nombreProducto__in=[
        'Labial Rojo', 'Crema Facial', 'Base de Maquillaje', 'Sérum Vitamina C'
    ]).delete()
    
    Subcategoria.objects.filter(idSubcategoria__in=[1, 2]).delete()
    Categoria.objects.filter(idCategoria__in=[1, 2]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_crear_usuario_admin'),
    ]

    operations = [
        migrations.RunPython(crear_datos_prueba, revertir),
    ]
