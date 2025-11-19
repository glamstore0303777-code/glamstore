from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=30, unique=True)
    direccion = models.CharField(max_length=30, null=True)
    telefono = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'clientes'
        managed = False  # ← evita que Django intente crearla
        app_label = 'core'    # ← asocia el modelo a tu app