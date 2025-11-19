from django.db import models

class Notificacion(models.Model):
    idNotificacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        db_table = 'notificaciones'  
        managed = True                # ← ajusta si el nombre real es distinto
        app_label = 'core'        # ← esta línea es obligatoria