"""
Servicio de correos usando Brevo (Sendinblue)
Más confiable que Gmail para producción
"""

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


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
