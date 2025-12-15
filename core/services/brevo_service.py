"""
Servicio de correos usando Brevo (Sendinblue)
Más confiable que Gmail para producción
"""

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings
from django.utils.html import strip_tags
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

COSTO_ENVIO = Decimal('10000')  # $10,000 COP
IVA_PORCENTAJE = Decimal('0.19')  # 19%


def generar_html_factura(pedido):
    """
    Genera el HTML de la factura para un pedido
    Retorna el HTML como string
    """
    from core.models.pedidos import DetallePedido
    from datetime import timedelta
    
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
    def es_dia_habil(fecha):
        return fecha.weekday() < 5
    
    def calcular_fecha_vencimiento(fecha_pedido, ciudad):
        ciudad_lower = ciudad.lower().replace('á', 'a')
        dias_vencimiento = 2 if 'bogota' in ciudad_lower else 3
        
        if hasattr(fecha_pedido, 'date'):
            fecha_pedido = fecha_pedido.date()
        
        fecha_actual = fecha_pedido
        dias_contados = 0
        
        while dias_contados < dias_vencimiento:
            fecha_actual += timedelta(days=1)
            if es_dia_habil(fecha_actual):
                dias_contados += 1
        
        return fecha_actual
    
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


def enviar_correo_brevo(destinatario, asunto, contenido_html, contenido_texto=None):
    """
    Envía un correo usando Brevo
    
    Args:
        destinatario: Email del destinatario
        asunto: Asunto del correo
        contenido_html: Contenido HTML del correo
        contenido_texto: Contenido de texto (opcional)
    
    Returns:
        True si se envió exitosamente, False si falló
    """
    try:
        # Verificar que BREVO_API_KEY esté configurado
        if not settings.BREVO_API_KEY:
            logger.error("[ERROR] BREVO_API_KEY no está configurado en las variables de entorno")
            print("[ERROR] BREVO_API_KEY no está configurado")
            return False
        
        # Configurar la API de Brevo
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = settings.BREVO_API_KEY.strip()
        
        # Crear instancia del cliente
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
        )
        
        # Preparar el correo
        email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": destinatario}],
            sender={"name": "Glam Store", "email": "glamstore0303777@gmail.com"},
            subject=asunto,
            html_content=contenido_html,
            text_content=contenido_texto or asunto
        )
        
        # Enviar
        response = api_instance.send_transac_email(email)
        
        logger.info(f"[OK] Correo enviado a {destinatario} - ID: {response.message_id}")
        print(f"[OK] Correo enviado a {destinatario}")
        return True
        
    except ApiException as e:
        logger.error(f"[ERROR] Error de API Brevo: {e}")
        print(f"[ERROR] Error de API Brevo: {e}")
        return False
    except Exception as e:
        logger.error(f"[ERROR] Error al enviar correo con Brevo: {str(e)}")
        print(f"[ERROR] Error al enviar correo con Brevo: {str(e)}")
        return False


def enviar_factura_brevo(pedido):
    """
    Envía la factura del pedido al cliente usando Brevo.
    Se adapta automáticamente según si hay repartidor asignado o no.
    
    Args:
        pedido: Objeto Pedido
    
    Returns:
        True si se envió exitosamente, False si falló
    """
    try:
        from core.models.pedidos import DetallePedido
        from datetime import timedelta, date
        
        cliente = pedido.idCliente
        
        if not cliente or not cliente.email:
            logger.warning(f"Cliente sin email para pedido #{pedido.idPedido}")
            print(f"[DEBUG] Cliente {cliente.nombre if cliente else 'desconocido'} no tiene email")
            return False
        
        # Obtener detalles del pedido
        detalles = DetallePedido.objects.filter(idPedido=pedido).select_related('idProducto')
        
        # Calcular totales
        subtotal_productos = sum(d.subtotal for d in detalles)
        iva = int(subtotal_productos * IVA_PORCENTAJE)
        
        # Determinar si debe pagar envío
        debe_pagar_envio = pedido.estado_pago == 'Pago Parcial'
        costo_envio = COSTO_ENVIO if debe_pagar_envio else 0
        
        # Calcular fecha de entrega estimada
        def es_dia_habil(fecha):
            return fecha.weekday() < 5
        
        def calcular_fecha_vencimiento(fecha_pedido, ciudad):
            ciudad_lower = ciudad.lower().replace('á', 'a')
            dias_vencimiento = 2 if 'bogota' in ciudad_lower else 3
            
            if hasattr(fecha_pedido, 'date'):
                fecha_pedido = fecha_pedido.date()
            
            fecha_actual = fecha_pedido
            dias_contados = 0
            
            while dias_contados < dias_vencimiento:
                fecha_actual += timedelta(days=1)
                if es_dia_habil(fecha_actual):
                    dias_contados += 1
            
            return fecha_actual
        
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
        
        # Determinar el asunto según el estado
        if pedido.idRepartidor:
            asunto = f"Factura de tu Pedido #{pedido.idPedido} - Repartidor Asignado - Glam Store"
        else:
            asunto = f"Factura de tu Pedido #{pedido.idPedido} - Glam Store"
        
        # Enviar usando Brevo
        return enviar_correo_brevo(cliente.email, asunto, html_message, strip_tags(html_message))
        
    except Exception as e:
        logger.error(f"[ERROR] Error al enviar factura con Brevo: {str(e)}")
        print(f"[ERROR] Error al enviar factura: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
