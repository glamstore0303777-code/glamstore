from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, db_column='idcliente')

    class Meta:
        db_table = 'clientes'
        managed = True  # Django maneja la creación y actualización de esta tabla
        app_label = 'core'
