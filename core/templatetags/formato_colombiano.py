from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def pesos_colombianos(valor):
    """
    Formatea un número como pesos colombianos con separadores de miles.
    Ejemplo: 40000 -> $40.000
    """
    if valor is None:
        return "$0"
    
    try:
        # Convertir a Decimal si es necesario
        if isinstance(valor, str):
            valor = Decimal(valor.replace(',', '.'))
        else:
            valor = Decimal(str(valor))
        
        # Formatear con separador de miles (punto) y sin decimales
        valor_int = int(valor)
        valor_formateado = f"{valor_int:,}".replace(',', '.')
        
        return f"${valor_formateado}"
    except:
        return f"${valor}"

@register.filter
def pesos_colombianos_decimales(valor):
    """
    Formatea un número como pesos colombianos con separadores de miles y decimales.
    Ejemplo: 40000.50 -> $40.000,50
    """
    if valor is None:
        return "$0,00"
    
    try:
        # Convertir a Decimal si es necesario
        if isinstance(valor, str):
            valor = Decimal(valor.replace(',', '.'))
        else:
            valor = Decimal(str(valor))
        
        # Separar parte entera y decimal
        valor_str = f"{valor:.2f}"
        partes = valor_str.split('.')
        parte_entera = int(partes[0])
        parte_decimal = partes[1] if len(partes) > 1 else "00"
        
        # Formatear parte entera con separador de miles (punto)
        parte_entera_formateada = f"{parte_entera:,}".replace(',', '.')
        
        return f"${parte_entera_formateada},{parte_decimal}"
    except:
        return f"${valor}"
