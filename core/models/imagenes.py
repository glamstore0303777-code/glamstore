from django.db import models
from core.models.categoria import Categoria, Subcategoria
from core.models.productos import Producto

class ImagenCategoria(models.Model):
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE, db_column='idcategoria', primary_key=True)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

class ImagenSubcategoria(models.Model):
    subcategoria = models.OneToOneField(Subcategoria, on_delete=models.CASCADE, db_column='idsubcategoria', primary_key=True)
    imagen = models.ImageField(upload_to='subcategorias/', null=True, blank=True)

class ImagenProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, db_column='idproducto', primary_key=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)