from django.db import models
from .pedidos import Pedido
from .repartidores import Repartidor


class ConfirmacionEntrega(models.Model):
    idConfirmacion = models.AutoField(primary_key=True)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='confirmacion_entrega')
    repartidor = models.ForeignKey(Repartidor, on_delete=models.SET_NULL, null=True, blank=True)
    foto_entrega = models.ImageField(upload_to='confirmaciones_entrega/', null=True, blank=True)
    calificacion = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)
    comentario = models.TextField(blank=True, null=True)
    fecha_confirmacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'confirmaciones_entrega'
        app_label = 'core'

    def __str__(self):
        return f"Confirmación Pedido #{self.pedido.idPedido} - {self.calificacion} estrellas"
