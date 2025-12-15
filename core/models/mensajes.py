from django.db import models

class MensajeContacto(models.Model):
    idMensaje = models.AutoField(primary_key=True, db_column='idmensaje')
    nombre = models.CharField(max_length=50, db_column='nombre')
    email = models.CharField(max_length=100, db_column='email')
    telefono = models.CharField(max_length=20, null=True, blank=True, db_column='telefono')
    mensaje = models.TextField(db_column='mensaje')
    fecha = models.DateTimeField(auto_now_add=True, db_column='fecha')

    class Meta:
        db_table = 'mensajes_contacto'
        managed = True
        app_label = 'core'
    
    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.fecha}"