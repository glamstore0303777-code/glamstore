from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def precio_venta(precio):
    """Calcula el precio de venta recomendado (precio + 15%)"""
    try:
        precio_decimal = Decimal(str(precio))
        return precio_decimal * Decimal('1.15')
    except:
        return 0
