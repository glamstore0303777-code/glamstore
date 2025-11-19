from django.db import models


class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    class Meta:
        db_table = 'categorias'
        managed = True
        app_label = 'core'

    def __str__(self):
        return self.nombreCategoria


class Subcategoria(models.Model):
    idSubcategoria = models.AutoField(primary_key=True)
    nombreSubcategoria = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        db_column='idCategoria'
    )

    class Meta:
        db_table = 'subcategorias'
        managed = False
        app_label = 'core'

    def __str__(self):
        return f"{self.nombreSubcategoria} ({self.categoria.nombreCategoria})"
    
    