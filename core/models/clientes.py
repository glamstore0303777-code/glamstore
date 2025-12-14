from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, db_column='idcliente')
    email = models.CharField(max_length=100, unique=True, db_column='email', null=True, blank=True)

    class Meta:
        db_table = 'clientes'
        managed = True  # Django maneja la creación y actualización de esta tabla
        app_label = 'core'
