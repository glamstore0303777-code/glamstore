from django.db import models
from .productos import Producto
from django.db import models

class Distribuidor(models.Model):
    idDistribuidor = models.AutoField(primary_key=True)
    nombreDistribuidor = models.CharField(max_length=30, null=True)
    contacto = models.CharField(max_length=20) 

    class Meta:
        db_table = 'distribuidores'
        managed = False
        app_label = 'core'  
        
class DistribuidorProducto(models.Model):
    id = models.AutoField(primary_key=True)
    idDistribuidor = models.IntegerField()
    idProducto = models.CharField(max_length=30)

    class Meta:
        db_table = 'distribuidor_producto'
        managed = False
        app_label = 'core'