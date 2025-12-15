from django.db import models
from .productos import Producto
from django.db import models

class Distribuidor(models.Model):
    idDistribuidor = models.AutoField(primary_key=True, db_column='iddistribuidor')
    nombreDistribuidor = models.CharField(max_length=30, null=True, db_column='nombredistribuidor')
    contacto = models.CharField(max_length=20, db_column='contacto')

    class Meta:
        db_table = 'distribuidores'
        managed = True
        app_label = 'core'  
        
class DistribuidorProducto(models.Model):
    id = models.AutoField(primary_key=True)
    idDistribuidor = models.IntegerField(db_column='iddistribuidor')
    idProducto = models.CharField(max_length=30, db_column='idproducto')

    class Meta:
        db_table = 'distribuidor_producto'
        managed = True
        app_label = 'core'