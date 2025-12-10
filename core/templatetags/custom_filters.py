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

@register.filter
def colombian_currency(value):
    """
    Formatea un número como moneda colombiana con separadores de miles.
    Ejemplo: 30000 -> 30.000
    """
    try:
        # Convertir a entero
        value = int(float(value))
        # Formatear con separadores de miles
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
