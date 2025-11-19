from django.db import models

class Profile(models.Model):
    idProfile = models.AutoField(primary_key=True)
    usuario = models.IntegerField()  # o ForeignKey si lo conectas con Usuario
    imagen = models.CharField(max_length=255, null=True)
    descripcion = models.TextField(null=True)

    class Meta:
        db_table = 'perfil'    
        managed = True     # ← ajusta si el nombre real es distinto
        app_label = 'core'      # ← esta línea es obligatoria