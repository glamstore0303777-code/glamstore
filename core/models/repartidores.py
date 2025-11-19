from django.db import models

class Repartidor(models.Model):
    idRepartidor = models.AutoField(primary_key=True)
    nombreRepartidor = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=11, null=True)
    estado_turno = models.CharField(max_length=20, null=True, default='Disponible')

    class Meta:
        db_table = 'repartidores'   
        managed = False             
        app_label = 'core'     

        