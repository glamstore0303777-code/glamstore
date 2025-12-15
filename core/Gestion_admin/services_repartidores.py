from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.conf import settings
from datetime import timedelta, time, date
from decimal import Decimal
from core.models.pedidos import Pedido, DetallePedido
from core.models.repartidores import Repartidor
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
import logging
import os
import base64

logger = logging.getLogger(__name__)

COSTO_ENVIO = Decimal('10000')  # $10,000 COP
IVA_PORCENTAJE = Decimal('0.19')  # 19%

HORARIO_INICIO = 6  # 6 AM
HORARIO_FIN = 15    # 3 PM
TIEMPO_ENTREGA_MINUTOS = 120  # 2 horas por pedido
PEDIDOS_POR_REPARTIDOR = (HORARIO_FIN - HORARIO_INICIO) * 60 // TIEMPO_ENTREGA_MINUTOS  # 4 pedidos máximo


def es_dia_habil(fecha):
    """Verifica si es día hábil (lunes a viernes)"""
    return fecha.weekday() < 5  # 0-4 son lunes a viernes


def calcular_fecha_vencimiento(fecha_pedido, ciudad):
    """
    Calcula fecha de vencimiento según ciudad
    - Bogotá: 2 días hábiles desde la fecha del pedido
    - Soacha: 3 días hábiles desde la fecha del pedido
    
    Nota: Los días se cuentan desde la fecha del pedido, no desde hoy.
    """
    ciudad_lower = ciudad.lower().replace('á', 'a')
    dias_vencimiento = 2 if 'bogota' in ciudad_lower else 3
    
    # Convertir a date si es datetime
    if hasattr(fecha_pedido, 'date'):
        fecha_pedido = fecha_pedido.date()
    
    fecha_actual = fecha_pedido
    dias_contados = 0
    
    while dias_contados < dias_vencimiento:
        fecha_actual += timedelta(days=1)
        if es_dia_habil(fecha_actual):
            dias_contados += 1
    
    return fecha_actual


def calcular_dias_habiles_restantes(fecha_pedido, fecha_vencimiento):
    """
    Calcula cuántos días hábiles quedan entre hoy y la fecha de vencimiento.
    Retorna un número negativo si ya pasó la fecha de vencimiento.
    """
    hoy = timezone.now().date()
    
    # Si ya pasó la fecha de vencimiento
    if hoy > fecha_vencimiento:
        return (hoy - fecha_vencimiento).days * -1  # Retorna negativo
    
    # Contar días hábiles desde hoy hasta la fecha de vencimiento
    dias_habiles = 0
    fecha_actual = hoy
    
    while fecha_actual < fecha_vencimiento:
        fecha_actual += timedelta(days=1)
        if es_dia_habil(fecha_actual) and fecha_actual <= fecha_vencimiento:
            dias_habiles += 1
    
    return dias_habiles


def obtener_pedidos_sin_asignar(fecha=None):
    """Obtiene los pedidos sin repartidor asignado para una fecha específica"""
    if fecha is None:
        fecha = timezone.now().date()
    
    return Pedido.objects.filter(
        idRepartidor__isnull=True,
        estado_pedido__in=['Confirmado', 'En Preparación'],
        fechaCreacion__date=fecha
    ).select_related('idCliente').order_by('fechaCreacion')


def obtener_repartidores_disponibles():
    """Obtiene los repartidores disponibles"""
    return Repartidor.objects.all().order_by('idRepartidor')


def calcular_capacidad_repartidor(repartidor, fecha=None):
    """Calcula cuántos pedidos más puede tomar un repartidor en un día"""
    if fecha is None:
        fecha = timezone.now().date()
    
    pedidos_asignados = Pedido.objects.filter(
        idRepartidor=repartidor,
        estado_pedido__in=['En Camino', 'Confirmado'],
        fechaCreacion__date=fecha
    ).count()
    
    capacidad_restante = PEDIDOS_POR_REPARTIDOR - pedidos_asignados
    return max(0, capacidad_restante)


def enviar_factura_cliente(pedido):
    """
    Envía la factura al cliente por correo electrónico.
    Se usa cuando:
    1. Se crea el pedido (sin repartidor)
    2. Se asigna un repartidor al pedido (con datos del repartidor)
    
    La factura se adapta automáticamente según si hay repartidor asignado o no.
    """
    cliente = pedido.idCliente
    
    if not cliente.email:
        print(f"[DEBUG] Cliente {cliente.nombre} no tiene email registrado")
        return False
    
    try:
        # Generar HTML de la factura (se adapta según si hay repartidor o no)
        html_message = generar_html_factura(pedido)
        
        # Determinar el asunto según el estado
        if pedido.idRepartidor:
            asunto = f"Factura de tu Pedido #{pedido.idPedido} - Repartidor Asignado - Glam Store"
        else:
            asunto = f"Factura de tu Pedido #{pedido.idPedido} - Glam Store"
        
        # Enviar correo
        email = EmailMultiAlternatives(
            subject=asunto,
            body=strip_tags(html_message),
            from_email='glamstore0303777@gmail.com',
            to=[cliente.email]
        )
        email.attach_alternative(html_message, "text/html")
        
        resultado = email.send()
        
        if resultado > 0:
            estado = "con repartidor" if pedido.idRepartidor else "sin repartidor"
            print(f"[DEBUG] Factura enviada a {cliente.email} para pedido #{pedido.idPedido} ({estado})")
            return True
        else:
            print(f"[DEBUG] Error al enviar factura a {cliente.email}")
            return False
            
    except Exception as e:
        print(f"[DEBUG] Error al enviar factura: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def generar_html_factura(pedido):
    """
    Genera el HTML de la factura para un pedido
    Retorna el HTML como string
    """
    if not pedido or not pedido.idPedido:
        raise ValueError("Pedido inválido o sin ID")
    
    cliente = pedido.idCliente
    
    # Obtener detalles del pedido
    detalles = DetallePedido.objects.filter(idPedido=pedido).select_related('idProducto')
    
    # Calcular totales
    subtotal_productos = sum(d.subtotal for d in detalles)
    iva = int(subtotal_productos * IVA_PORCENTAJE)
    
    # Determinar si debe pagar envío
    debe_pagar_envio = pedido.estado_pago == 'Pago Parcial'
    costo_envio = COSTO_ENVIO if debe_pagar_envio else 0
    
    # Calcular fecha de entrega estimada
    ciudad = 'Soacha' if 'soacha' in cliente.direccion.lower() else 'Bogotá'
    fecha_entrega = calcular_fecha_vencimiento(pedido.fechaCreacion.date(), ciudad)
    
    fecha_entrega_formateada = fecha_entrega.strftime('%d de %B de %Y')
    
    # Preparar lista de productos
    productos_html = ""
    for detalle in detalles:
        productos_html += f"""
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">{detalle.idProducto.nombreProducto}</td>
            <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; text-align: center;">{detalle.cantidad}</td>
            <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; text-align: right;">${detalle.precio_unitario:,.0f}</td>
            <td style="padding: 10px; border-bottom: 1px solid #e5e7eb; text-align: right;">${detalle.subtotal:,.0f}</td>
        </tr>
        """
    
    # Información del repartidor y fecha de entrega
    repartidor_info = ""
    if pedido.idRepartidor:
        repartidor_info = f"""
        <div style="background-color: #f3f0ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <h3 style="color: #7c3aed; margin: 0 0 10px 0;">Información de Entrega</h3>
            <p style="margin: 5px 0;"><strong>Repartidor:</strong> {pedido.idRepartidor.nombreRepartidor}</p>
            <p style="margin: 5px 0;"><strong>Teléfono:</strong> {pedido.idRepartidor.telefono}</p>
            <p style="margin: 5px 0;"><strong>Fecha estimada de entrega:</strong> {fecha_entrega_formateada}</p>
            <p style="margin: 5px 0;"><strong>Estado del pedido:</strong> {pedido.estado_pedido}</p>
        </div>
        """
    
    # Mensaje sobre pago de envío
    pago_envio_html = ""
    if debe_pagar_envio:
        pago_envio_html = f"""
        <div style="background-color: #fef2f2; border: 2px solid #dc2626; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <h3 style="color: #dc2626; margin: 0 0 10px 0;">IMPORTANTE: Pago Contra Entrega</h3>
            <p style="margin: 5px 0; color: #991b1b;">Tu pedido tiene <strong>Pago Parcial</strong>. Debes pagar el envío al repartidor:</p>
            <p style="margin: 10px 0; font-size: 24px; font-weight: bold; color: #dc2626;">Total a pagar: ${costo_envio:,.0f}</p>
        </div>
        """
    else:
        pago_envio_html = """
        <div style="background-color: #f0fdf4; border: 2px solid #22c55e; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <h3 style="color: #16a34a; margin: 0 0 10px 0;">Pago Completo</h3>
            <p style="margin: 5px 0; color: #166534;">Tu pedido está completamente pagado. No debes pagar nada al repartidor.</p>
        </div>
        """
    
    # HTML del correo
    html_message = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 20px auto; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); overflow: hidden; }}
            .header {{ background: linear-gradient(135deg, #e8d5ff 0%, #f0e6ff 100%); color: #6b46c1; padding: 30px; text-align: center; }}
            .header h1 {{ margin: 0; font-size: 28px; font-weight: 700; }}
            .content {{ padding: 30px; }}
            .footer {{ background-color: #f8f9fa; padding: 20px; text-align: center; color: #9ca3af; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Glam Store</h1>
                <p>Factura de tu Pedido #{pedido.idPedido}</p>
            </div>
            
            <div class="content">
                <p>Hola <strong>{cliente.nombre}</strong>,</p>
                <p>{"Tu pedido ha sido asignado a un repartidor y pronto estará en camino." if pedido.idRepartidor else "Tu pedido ha sido creado exitosamente. Aquí están los detalles de tu compra:"} Aquí están los detalles:</p>
                
                {repartidor_info}
                
                <h3 style="color: #374151; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">Detalle de Productos</h3>
                <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
                    <thead>
                        <tr style="background-color: #f3f0ff;">
                            <th style="padding: 10px; text-align: left; color: #7c3aed;">Producto</th>
                            <th style="padding: 10px; text-align: center; color: #7c3aed;">Cantidad</th>
                            <th style="padding: 10px; text-align: right; color: #7c3aed;">Precio Unit.</th>
                            <th style="padding: 10px; text-align: right; color: #7c3aed;">Subtotal</th>
                        </tr>
                    </thead>
                    <tbody>
                        {productos_html}
                    </tbody>
                </table>
                
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0;">
                    <table style="width: 100%;">
                        <tr>
                            <td style="padding: 5px 0;"><strong>Subtotal:</strong></td>
                            <td style="padding: 5px 0; text-align: right;">${subtotal_productos:,.0f}</td>
                        </tr>
                        <tr>
                            <td style="padding: 5px 0;"><strong>IVA (19%):</strong></td>
                            <td style="padding: 5px 0; text-align: right;">${iva:,.0f}</td>
                        </tr>
                        <tr>
                            <td style="padding: 5px 0;"><strong>Envío:</strong></td>
                            <td style="padding: 5px 0; text-align: right;">${costo_envio:,.0f}</td>
                        </tr>
                        <tr style="border-top: 2px solid #e5e7eb;">
                            <td style="padding: 10px 0; font-size: 18px;"><strong>TOTAL:</strong></td>
                            <td style="padding: 10px 0; text-align: right; font-size: 18px; font-weight: bold; color: #7c3aed;">${subtotal_productos + iva + costo_envio:,.0f}</td>
                        </tr>
                    </table>
                </div>
                
                {pago_envio_html}
                
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0;">
                    <h3 style="color: #374151; margin: 0 0 10px 0;">Dirección de Entrega</h3>
                    <p style="margin: 5px 0;">{cliente.direccion}</p>
                    <p style="margin: 5px 0;"><strong>Teléfono:</strong> {cliente.telefono}</p>
                </div>
                
                <p style="color: #6b7280; font-size: 14px;">
                    Si tienes alguna pregunta, contáctanos en <strong>glamstore0303777@gmail.com</strong>
                </p>
            </div>
            
            <div class="footer">
                <p><strong>Glam Store</strong></p>
                <p>Gracias por tu compra</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_message


def asignar_pedidos_automaticamente(fecha=None):
    """
    Asigna automáticamente los pedidos a los repartidores disponibles.
    Distribuye equitativamente: si hay 10 pedidos y 3 repartidores,
    dos tendrán 3 pedidos y uno tendrá 4.
    Retorna un diccionario con información sobre la asignación.
    """
    if fecha is None:
        fecha = timezone.now().date()
    
    resultado = {
        'pedidos_asignados': 0,
        'pedidos_agendados': 0,
        'repartidores_sin_capacidad': False,
        'mensaje': '',
        'detalle_asignacion': {}
    }
    
    # Obtener TODOS los pedidos sin repartidor asignado (sin importar estado ni fecha)
    pedidos_sin_asignar = list(Pedido.objects.filter(
        idRepartidor__isnull=True
    ).exclude(
        estado_pedido__in=['Cancelado', 'Devuelto']  # Excluir solo cancelados y devueltos
    ).select_related('idCliente').order_by('fechaCreacion'))
    
    repartidores = list(obtener_repartidores_disponibles())
    
    total_pedidos = len(pedidos_sin_asignar)
    total_repartidores = len(repartidores)
    
    print(f"[DEBUG] Pedidos sin asignar: {total_pedidos}")
    print(f"[DEBUG] Repartidores disponibles: {total_repartidores}")
    
    if total_pedidos == 0:
        resultado['mensaje'] = "No hay pedidos pendientes para asignar"
        return resultado
    
    if total_repartidores == 0:
        resultado['repartidores_sin_capacidad'] = True
        resultado['mensaje'] = f"No hay repartidores disponibles para {total_pedidos} pedidos"
        return resultado
    
    # Calcular distribución equitativa
    pedidos_por_repartidor = total_pedidos // total_repartidores
    pedidos_extra = total_pedidos % total_repartidores
    
    print(f"[DEBUG] Pedidos base por repartidor: {pedidos_por_repartidor}")
    print(f"[DEBUG] Pedidos extra a distribuir: {pedidos_extra}")
    
    # Inicializar contador de asignaciones por repartidor
    asignaciones = {r.idRepartidor: 0 for r in repartidores}
    
    # Asignar pedidos equitativamente
    indice_pedido = 0
    
    for i, repartidor in enumerate(repartidores):
        # Calcular cuántos pedidos le tocan a este repartidor
        cantidad = pedidos_por_repartidor
        if i < pedidos_extra:
            cantidad += 1  # Los primeros repartidores reciben uno extra
        
        print(f"[DEBUG] Repartidor {repartidor.nombreRepartidor}: {cantidad} pedidos")
        
        # Asignar los pedidos
        for _ in range(cantidad):
            if indice_pedido < total_pedidos:
                pedido = pedidos_sin_asignar[indice_pedido]
                pedido.idRepartidor = repartidor
                pedido.estado_pedido = 'En Camino'
                pedido.save()
                
                # Enviar factura al cliente
                enviar_factura_cliente(pedido)
                
                asignaciones[repartidor.idRepartidor] += 1
                resultado['pedidos_asignados'] += 1
                indice_pedido += 1
    
    # Guardar detalle de asignación
    for repartidor in repartidores:
        resultado['detalle_asignacion'][repartidor.nombreRepartidor] = asignaciones[repartidor.idRepartidor]
    
    # Generar mensaje
    detalle = ", ".join([f"{nombre}: {cant}" for nombre, cant in resultado['detalle_asignacion'].items()])
    resultado['mensaje'] = f"Se asignaron {resultado['pedidos_asignados']} pedidos a {total_repartidores} repartidores. Distribución: {detalle}"
    
    print(f"[DEBUG] Resultado: {resultado['mensaje']}")
    
    return resultado


def generar_pdf_pedidos_repartidor(repartidor, fecha=None):
    """
    Genera un PDF con todos los pedidos asignados a un repartidor para un día específico
    """
    if fecha is None:
        fecha = timezone.now().date()
    
    pedidos = Pedido.objects.filter(
        idRepartidor=repartidor,
        estado_pedido__in=['En Camino', 'Confirmado'],
        fechaCreacion__date=fecha
    ).select_related('idCliente').prefetch_related('detallepedido_set__idProducto')
    
    # Calcular horarios de entrega y información de vencimiento
    pedidos_con_horario = []
    hora_inicio = HORARIO_INICIO
    
    for idx, pedido in enumerate(pedidos):
        hora_fin = hora_inicio + (TIEMPO_ENTREGA_MINUTOS // 60)
        
        # Calcular fecha de vencimiento dinámicamente (el campo no existe en BD)
        ciudad = 'Soacha' if 'soacha' in pedido.idCliente.direccion.lower() else 'Bogotá'
        fecha_vencimiento = calcular_fecha_vencimiento(pedido.fechaCreacion.date(), ciudad)
        
        # Calcular días hábiles restantes
        dias_restantes = calcular_dias_habiles_restantes(pedido.fechaCreacion.date(), fecha_vencimiento)
        
        # Determinar alerta
        if dias_restantes == 0:
            alerta = 'VENCE HOY'
        elif dias_restantes > 0:
            alerta = f'Vence en {dias_restantes} días'
        else:
            alerta = 'VENCIDO'
        
        pedidos_con_horario.append({
            'pedido': pedido,
            'hora_inicio': f"{hora_inicio:02d}:00",
            'hora_fin': f"{hora_fin:02d}:00",
            'numero_secuencia': idx + 1,
            'fecha_vencimiento': fecha_vencimiento.strftime('%d/%m/%Y'),
            'alerta': alerta,
            'dias_restantes': dias_restantes
        })
        hora_inicio = hora_fin
    
    context = {
        'repartidor': repartidor,
        'pedidos': pedidos_con_horario,
        'fecha': fecha,
        'total_pedidos': len(pedidos_con_horario),
        'horario_inicio': f"{HORARIO_INICIO:02d}:00",
        'horario_fin': f"{HORARIO_FIN:02d}:00"
    }
    
    template_path = 'asignacion_pedidos_repartidor_pdf.html'
    from django.template.loader import get_template
    template = get_template(template_path)
    html = template.render(context)
    
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        return result.getvalue()
    
    return None


def verificar_capacidad_repartidores():
    """
    Verifica la capacidad de todos los repartidores para el día actual.
    Retorna un diccionario con información sobre la capacidad.
    """
    fecha = timezone.now().date()
    repartidores = obtener_repartidores_disponibles()
    
    resultado = {}
    for repartidor in repartidores:
        capacidad = calcular_capacidad_repartidor(repartidor, fecha)
        resultado[repartidor.nombreRepartidor] = {
            'capacidad_restante': capacidad,
            'puede_recibir_pedidos': capacidad > 0
        }
    
    return resultado
