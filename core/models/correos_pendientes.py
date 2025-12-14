from django.db import models


class CorreoPendiente(models.Model):
    idPedido = models.IntegerField(db_column='id_pedido')
    destinatario = models.EmailField(db_column='destinatario')
    asunto = models.CharField(max_length=255, db_column='asunto')
    contenido_html = models.TextField(db_column='contenido_html')
    contenido_texto = models.TextField(null=True, blank=True, db_column='contenido_texto')
    enviado = models.BooleanField(default=False, db_column='enviado')
    intentos = models.IntegerField(default=0, db_column='intentos')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    fecha_envio = models.DateTimeField(null=True, blank=True, db_column='fecha_envio')
    error = models.TextField(null=True, blank=True, db_column='error')
    
    class Meta:
        db_table = 'correos_pendientes'
        managed = True
        app_label = 'core'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"Correo para Pedido #{self.idPedido} - {self.destinatario}"
