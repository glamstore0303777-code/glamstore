from django.db import models


class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    fechaCreacion = models.DateTimeField(db_column='fechaCreacion') # Asumiendo que la columna se llama así
    estado = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    idCliente = models.ForeignKey('core.Cliente', on_delete=models.CASCADE, db_column='idCliente')
    idRepartidor = models.ForeignKey(
        'core.Repartidor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='idRepartidor'
    )


    class Meta:
        db_table = 'pedidos'
        managed = False
        app_label = 'core'

    def __str__(self):
        return f"Pedido #{self.idPedido} - {self.estado}"


class DetallePedido(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        db_column='idPedido'
    )
    idProducto = models.ForeignKey(
        'Producto',
        on_delete=models.CASCADE,
        db_column='idProducto'
    )
    cantidad = models.PositiveIntegerField(default=1, blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'detallepedido'
        managed = False
        app_label = 'core'

    def __str__(self):
        return f"Detalle #{self.idDetalle} - Producto {self.idProducto_id}"


class PedidoProducto(models.Model):
    idPedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        db_column='idPedido'
    )
    idProducto = models.ForeignKey(
        'Producto',
        on_delete=models.CASCADE,
        db_column='idProducto'
    )
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'pedidoproducto'
        managed = False
        app_label = 'core'
        unique_together = ('idPedido', 'idProducto')

    def __str__(self):
        return f"Pedido {self.idPedido_id} - Producto {self.idProducto_id}"