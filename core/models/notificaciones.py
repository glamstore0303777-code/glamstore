from django.db import models


class NotificacionProblema(models.Model):
    idNotificacion = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(
        'core.Pedido',
        on_delete=models.CASCADE,
        db_column='idPedido'
    )
    motivo = models.TextField()
    foto = models.ImageField(upload_to='problemas_entrega/', null=True, blank=True)
    fechaReporte = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'notificaciones_problema'
        managed = True  # Django puede crear esta tabla
        app_label = 'core'
        ordering = ['-fechaReporte']
    
    def __str__(self):
        return f"Problema Pedido #{self.idPedido_id} - {self.fechaReporte}"
