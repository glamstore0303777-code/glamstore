from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, db_column='idcliente')
    cedula = models.CharField(max_length=20, db_column='cedula')
    nombre = models.CharField(max_length=100, null=True, db_column='nombre')
    email = models.CharField(max_length=100, unique=True, db_column='email')
    direccion = models.CharField(max_length=200, null=True, db_column='direccion')
    telefono = models.CharField(max_length=20, null=True, db_column='telefono')

    class Meta:
        db_table = 'clientes'
        managed = False  # ← evita que Django intente crearla
        app_label = 'core'    # ← asocia el modelo a tu app
