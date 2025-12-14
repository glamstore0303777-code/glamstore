from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, db_column='idcliente')
    nombre = models.CharField(max_length=100, null=True, blank=True, db_column='nombrecliente')
    apellido = models.CharField(max_length=100, null=True, blank=True, db_column='apellidocliente')
    email = models.EmailField(max_length=100, null=True, blank=True, db_column='emailcliente')
    telefono = models.CharField(max_length=20, null=True, blank=True, db_column='telefonocliente')
    direccion = models.TextField(null=True, blank=True, db_column='direccioncliente')
    ciudad = models.CharField(max_length=50, null=True, blank=True, db_column='ciudadcliente')
    departamento = models.CharField(max_length=50, null=True, blank=True, db_column='departamentocliente')
    codigo_postal = models.CharField(max_length=20, null=True, blank=True, db_column='codigopostalcliente')

    class Meta:
        db_table = 'clientes'
        managed = False  # No dejar que Django maneje la tabla, ya existe en BD
        app_label = 'core'
    
    def __str__(self):
        return f"{self.nombre} ({self.idCliente})" if self.nombre else f"Cliente {self.idCliente}"
