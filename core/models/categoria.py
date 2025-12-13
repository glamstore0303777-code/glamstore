from django.db import models


class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, db_column='idcategoria')
    nombreCategoria = models.CharField(max_length=20, db_column='nombrecategoria')
    descripcion = models.TextField(null=True, db_column='descripcion')
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True, db_column='imagen')

    class Meta:
        db_table = 'categorias'
        managed = True
        app_label = 'core'

    def __str__(self):
        return self.nombreCategoria


class Subcategoria(models.Model):
    idSubcategoria = models.AutoField(primary_key=True, db_column='idsubcategoria')
    nombreSubcategoria = models.CharField(max_length=50, db_column='nombresubcategoria')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        db_column='idcategoria'
    )

    class Meta:
        db_table = 'subcategorias'
        managed = True
        app_label = 'core'

    def __str__(self):
        return f"{self.nombreSubcategoria} ({self.categoria.nombreCategoria})"
    
    