from django.db import models


class Producto(models.Model):
    idProducto = models.BigAutoField(primary_key=True, db_column='idproducto')
    nombreProducto = models.CharField(max_length=50, db_column='nombreproducto')
    precio = models.DecimalField(max_digits=10, decimal_places=2, db_column='precio')
    stock = models.IntegerField(default=0, db_column='stock')
    descripcion = models.TextField(blank=True, null=True, db_column='descripcion')
    lote = models.CharField(max_length=100, blank=True, null=True, help_text="Código del lote actual", db_column='lote')
    cantidadDisponible = models.IntegerField(default=0, db_column='cantidaddisponible')
    fechaIngreso = models.DateTimeField(blank=True, null=True, db_column='fechaingreso')
    fechaVencimiento = models.DateField(blank=True, null=True, db_column='fechavencimiento')

    idCategoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        db_column='idcategoria'
    )

    idSubcategoria = models.ForeignKey(
        'Subcategoria',
        on_delete=models.SET_NULL,
        null=True,
        db_column='idsubcategoria'
    )

    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, db_column='imagen')
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Precio de venta calculado automáticamente", db_column='precio_venta')

    class Meta:
        db_table = 'productos'
        managed = True  # Django maneja la creación y actualización de esta tabla
        app_label = 'core'

    def __str__(self):
        return self.nombreProducto
    
    def calcular_precio_venta(self):
        """Calcula el precio de venta: Costo × 1.19 (IVA) × (1 + margen_ganancia_global/100)
        Redondea al múltiplo de 50 más cercano para precios limpios"""
        from decimal import Decimal
        
        if self.precio:
            # Convertir precio a Decimal si es string
            precio_decimal = Decimal(str(self.precio)) if not isinstance(self.precio, Decimal) else self.precio
            # Usar margen por defecto de 10%
            margen = Decimal('10')
            # Precio de Venta = Costo × 1.19 (IVA) × (1 + margen/100)
            factor_margen = Decimal('1') + (margen / Decimal('100'))
            precio_calculado = float(precio_decimal * Decimal('1.19') * factor_margen)
            # Redondear al múltiplo de 50 más cercano
            precio_redondeado = round(precio_calculado / 50) * 50
            return int(precio_redondeado)
        return 0
