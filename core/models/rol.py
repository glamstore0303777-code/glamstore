from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=20)

    class Meta:
        db_table = 'roles'          
        managed = False
        app_label = 'core'