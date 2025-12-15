"""
Servicio para enviar planes semanales a repartidores usando Brevo
"""

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings
from django.utils.html import strip_tags
from datetime import timedelta, date
from core.models.pedidos import Pedido
from core.models.repartidores import Repartidor
from core.Gestion_admin.services_repartidores import (
    calcular_fecha_vencimiento,
    calcular_dias_habiles_restantes
)
import logging

logger = logging.getLogger(__name__)


def enviar_correo_brevo_repartidor(destinatario, asunto, contenido_html):
    """
    Envía un correo usando Brevo a un repartidor
    
    Args:
        destinatario: Email del repartidor
        asunto: Asunto del correo
        contenido_html: Contenido HTML del correo
    
    Returns:
        True si se envió exitosamente, False si falló
    """
    try:
        if not settings.BREVO_API_KEY:
            logger.error("[ERROR] BREVO_API_KEY no está configurado")
            print("[ERROR] BREVO_API_KEY no está configurado")
            return False
        
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = settings.BREVO_API_KEY.strip()
        
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
        )
        
        email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": destinatario}],
            sender={"name": "Glam Store", "email": "glamstore0303777@gmail.com"},
            subject=asunto,
            html_content=contenido_html,
            text_content=asunto
        )
        
        response = api_instance.send_transac_email(email)
        
        logger.info(f"[OK] Correo enviado a repartidor {destinatario} - ID: {response.message_id}")
        print(f"[OK] Correo enviado a repartidor {destinatario}")
        return True
        
    except ApiException as e:
        logger.error(f"[ERROR] Error de API Brevo: {e}")
        print(f"[ERROR] Error de API Brevo: {e}")
        return False
    except Exception as e:
        logger.error(f"[ERROR] Error al enviar correo: {str(e)}")
        print(f"[ERROR] Error al enviar correo: {str(e)}")
        return False


def enviar_plan_semanal_repartidor(repartidor):
    """
    Envía el plan semanal de entregas a un repartidor
    Incluye todos los pedidos asignados para la semana actual
    
    Args:
        repartidor: Objeto Repartidor
    
    Returns:
        True si se envió exitosamente, False si falló
    """
    if not repartidor.email:
        logger.warning(f"Repartidor {repartidor.nombreRepartidor} sin email")
        print(f"[DEBUG] Repartidor sin email")
        return False
    
    try:
        # Obtener la fecha de hoy y calcular el rango de la semana
        hoy = date.today()
        # Lunes de esta semana
        lunes = hoy - timedelta(days=hoy.weekday())
        # Viernes de esta semana
        viernes = lunes + timedelta(days=4)
        
        # Obtener pedidos de la semana
        pedidos = Pedido.objects.filter(
            idRepartidor=repartidor,
            fechaCreacion__date__gte=lunes,
            fechaCreacion__date__lte=viernes
        ).exclude(
            estado_pedido__in=['Cancelado', 'Devuelto']
        ).select_related('idCliente').prefetch_related('detallepedido_set__idProducto').order_by('fechaCreacion')
        
        if not pedidos.exists():
            logger.info(f"No hay pedidos para {repartidor.nombreRepartidor} esta semana")
            print(f"[DEBUG] No hay pedidos para esta semana")
            return False
        
        # Preparar información de pedidos
        pedidos_por_dia = {}
        total_pedidos = 0
        total_ingresos = 0
        
        for pedido in pedidos:
            dia = pedido.fechaCreacion.date().strftime('%A')
            dia_numero = pedido.fechaCreacion.date().strftime('%d/%m/%Y')
            
            if dia_numero not in pedidos_por_dia:
                pedidos_por_dia[dia_numero] = []
            
            # Calcular información del pedido
            ciudad = 'Soacha' if 'soacha' in pedido.idCliente.direccion.lower() else 'Bogotá'
            fecha_vencimiento = calcular_fecha_vencimiento(pedido.fechaCreacion.date(), ciudad)
            dias_restantes = calcular_dias_habiles_restantes(pedido.fechaCreacion.date(), fecha_vencimiento)
            
            # Determinar alerta
            if dias_restantes <= 0:
                alerta = 'VENCIDO' if dias_restantes < 0 else 'VENCE HOY'
                alerta_color = '#dc2626'
            else:
                alerta = f'Vence en {dias_restantes} días'
                alerta_color = '#f97316' if dias_restantes == 1 else '#6b7280'
            
            cobra_envio = 'SÍ' if pedido.estado_pago == 'Pago Parcial' else 'NO'
            
            pedidos_por_dia[dia_numero].append({
                'numero': pedido.idPedido,
                'cliente': pedido.idCliente.nombre,
                'telefono': pedido.idCliente.telefono,
                'direccion': pedido.idCliente.direccion,
                'total': int(pedido.total),
                'estado_pago': pedido.estado_pago,
                'cobra_envio': cobra_envio,
                'alerta': alerta,
                'alerta_color': alerta_color,
                'fecha_vencimiento': fecha_vencimiento.strftime('%d/%m/%Y')
            })
            
            total_pedidos += 1
            total_ingresos += int(pedido.total)
        
        # Generar tabla de pedidos por día
        tabla_dias = ""
        for dia, pedidos_dia in sorted(pedidos_por_dia.items()):
            tabla_dias += f"""
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; margin-bottom: 15px;">
                <h4 style="color: #7c3aed; margin: 0 0 10px 0; font-size: 14px; border-bottom: 2px solid #c4b5fd; padding-bottom: 8px;">
                    📅 {dia} ({len(pedidos_dia)} pedidos)
                </h4>
            """
            
            for idx, pedido in enumerate(pedidos_dia, 1):
                tabla_dias += f"""
                <div style="background-color: {'#fef2f2' if pedido['alerta_color'] == '#dc2626' else '#ffffff'}; border-left: 4px solid {pedido['alerta_color']}; padding: 12px; margin-bottom: 10px; border-radius: 4px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <strong style="color: #374151;">Pedido #{pedido['numero']} - {pedido['cliente']}</strong>
                        <span style="background-color: {pedido['alerta_color']}; color: white; padding: 3px 8px; border-radius: 3px; font-size: 11px; font-weight: bold;">{pedido['alerta']}</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 12px; color: #6b7280;">
                        <div>
                            <p style="margin: 2px 0;"><strong>Teléfono:</strong> {pedido['telefono']}</p>
                            <p style="margin: 2px 0;"><strong>Dirección:</strong> {pedido['direccion']}</p>
                        </div>
                        <div>
                            <p style="margin: 2px 0;"><strong>Total:</strong> ${pedido['total']:,}</p>
                            <p style="margin: 2px 0;"><strong>¿Cobrar?:</strong> <span style="color: {'#dc2626' if pedido['cobra_envio'] == 'SÍ' else '#6b7280'}; font-weight: bold;">{pedido['cobra_envio']}</span></p>
                        </div>
                    </div>
                </div>
                """
            
            tabla_dias += "</div>"
        
        # Generar HTML del correo
        html_message = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #faf8ff; margin: 0; padding: 0; }}
                .container {{ max-width: 900px; margin: 20px auto; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); overflow: hidden; }}
                .header {{ background: linear-gradient(135deg, #e8d5ff 0%, #f0e6ff 100%); color: #6b46c1; padding: 30px; text-align: center; border-bottom: 3px solid #c4b5fd; }}
                .header h1 {{ margin: 0; font-size: 28px; font-weight: 700; }}
                .header p {{ margin: 10px 0 0 0; font-size: 14px; opacity: 0.8; }}
                .content {{ padding: 30px; }}
                .resumen {{ background-color: #f3f0ff; border-left: 5px solid #c4b5fd; padding: 20px; margin-bottom: 25px; border-radius: 6px; }}
                .resumen-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 10px; }}
                .resumen-item {{ text-align: center; }}
                .resumen-numero {{ font-size: 24px; font-weight: bold; color: #7c3aed; }}
                .resumen-label {{ font-size: 12px; color: #6b7280; margin-top: 5px; }}
                .footer {{ background-color: #faf8ff; padding: 20px; text-align: center; border-top: 1px solid #e5e7eb; color: #9ca3af; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Plan Semanal de Entregas</h1>
                    <p>Semana del {lunes.strftime('%d/%m/%Y')} al {viernes.strftime('%d/%m/%Y')}</p>
                </div>
                
                <div class="content">
                    <p>Hola <strong>{repartidor.nombreRepartidor}</strong>,</p>
                    <p>Aquí está tu plan de entregas para esta semana. Recuerda revisar los estados de pago y las fechas de vencimiento.</p>
                    
                    <div class="resumen">
                        <h3 style="color: #7c3aed; margin-top: 0;">Resumen de la Semana</h3>
                        <div class="resumen-grid">
                            <div class="resumen-item">
                                <div class="resumen-numero">{total_pedidos}</div>
                                <div class="resumen-label">Total de Pedidos</div>
                            </div>
                            <div class="resumen-item">
                                <div class="resumen-numero">${total_ingresos:,}</div>
                                <div class="resumen-label">Ingresos Totales</div>
                            </div>
                            <div class="resumen-item">
                                <div class="resumen-numero">${int(total_ingresos / total_pedidos) if total_pedidos > 0 else 0:,}</div>
                                <div class="resumen-label">Promedio por Pedido</div>
                            </div>
                        </div>
                    </div>
                    
                    <h3 style="color: #374151; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">Pedidos por Día</h3>
                    {tabla_dias}
                    
                    <div style="background-color: #fef7ed; border-left: 5px solid #f97316; padding: 20px; margin-top: 25px; border-radius: 6px;">
                        <h3 style="color: #ea580c; margin-top: 0;">Recomendaciones</h3>
                        <ul style="margin: 10px 0; padding-left: 20px; color: #9a3412; font-size: 14px;">
                            <li>Verifica los estados de pago antes de entregar</li>
                            <li>Cobra el envío solo a los pedidos marcados con "SÍ"</li>
                            <li>Prioriza los pedidos que vencen hoy o mañana</li>
                            <li>Confirma la entrega en el sistema</li>
                        </ul>
                    </div>
                </div>
                
                <div class="footer">
                    <p><strong>Glam Store</strong></p>
                    <p>¿Preguntas? Contáctanos en glamstore0303777@gmail.com</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        asunto = f"Plan Semanal de Entregas - {lunes.strftime('%d/%m/%Y')} al {viernes.strftime('%d/%m/%Y')}"
        
        return enviar_correo_brevo_repartidor(repartidor.email, asunto, html_message)
        
    except Exception as e:
        logger.error(f"[ERROR] Error al enviar plan semanal: {str(e)}")
        print(f"[ERROR] Error al enviar plan semanal: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def enviar_planes_semanales_todos_repartidores():
    """
    Envía planes semanales a todos los repartidores
    
    Returns:
        Diccionario con información sobre el envío
    """
    resultado = {
        'total_repartidores': 0,
        'correos_enviados': 0,
        'correos_fallidos': 0,
        'detalles': []
    }
    
    try:
        repartidores = Repartidor.objects.filter(email__isnull=False).exclude(email='')
        resultado['total_repartidores'] = repartidores.count()
        
        for repartidor in repartidores:
            if enviar_plan_semanal_repartidor(repartidor):
                resultado['correos_enviados'] += 1
                resultado['detalles'].append(f"✓ {repartidor.nombreRepartidor}")
            else:
                resultado['correos_fallidos'] += 1
                resultado['detalles'].append(f"✗ {repartidor.nombreRepartidor}")
        
        logger.info(f"Planes semanales enviados: {resultado['correos_enviados']}/{resultado['total_repartidores']}")
        print(f"[OK] Planes semanales enviados: {resultado['correos_enviados']}/{resultado['total_repartidores']}")
        
    except Exception as e:
        logger.error(f"[ERROR] Error al enviar planes semanales: {str(e)}")
        print(f"[ERROR] Error al enviar planes semanales: {str(e)}")
    
    return resultado
