from django.db import models
from django.utils import timezone


class CorreoPendiente(models.Model):
    """Modelo para almacenar correos pendientes de envío"""
    idPedido = models.IntegerField(db_column='id_pedido')
    destinatario = models.CharField(max_length=255, db_column='destinatario')
    asunto = models.CharField(max_length=255, db_column='asunto')
    contenido_html = models.TextField(db_column='contenido_html')
    contenido_texto = models.TextField(db_column='contenido_texto')
    enviado = models.BooleanField(default=False, db_column='enviado')
    intentos = models.IntegerField(default=0, db_column='intentos')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    fecha_envio = models.DateTimeField(null=True, blank=True, db_column='fecha_envio')
    error = models.TextField(null=True, blank=True, db_column='error')
    
    class Meta:
        db_table = 'correos_pendientes'
        managed = False
        app_label = 'core'
    
    def __str__(self):
        return f"Correo para pedido {self.idPedido} - {self.destinatario}"
