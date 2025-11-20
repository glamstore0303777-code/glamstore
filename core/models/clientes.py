from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'clientes'
        managed = False  # ← evita que Django intente crearla
        app_label = 'core'    # ← asocia el modelo a tu app
