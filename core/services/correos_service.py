"""
Servicio para gestionar el envío de correos de forma asincrónica
"""
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.utils import timezone
from core.models.correos_pendientes import CorreoPendiente


def enviar_correo_directo(destinatario, asunto, contenido_html):
    """
    Envía un correo directamente sin encolar
    
    Args:
        destinatario: Email del destinatario
        asunto: Asunto del correo
        contenido_html: Contenido HTML del correo
    
    Returns:
        True si se envió exitosamente, False si falló
    """
    try:
        contenido_texto = strip_tags(contenido_html)
        
        email = EmailMultiAlternatives(
            subject=asunto,
            body=contenido_texto,
            from_email='glamstore0303777@gmail.com',
            to=[destinatario]
        )
        email.attach_alternative(contenido_html, "text/html")
        
        resultado = email.send()
        
        if resultado > 0:
            print(f"[OK] Correo enviado directamente a {destinatario}")
            return True
        else:
            print(f"[ERROR] No se pudo enviar correo a {destinatario}")
            return False
    except Exception as e:
        print(f"[ERROR] Error al enviar correo a {destinatario}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def encolar_correo(id_pedido, destinatario, asunto, contenido_html):
    """
    Encola un correo para envío posterior (fallback si el envío directo falla)
    
    Args:
        id_pedido: ID del pedido
        destinatario: Email del destinatario
        asunto: Asunto del correo
        contenido_html: Contenido HTML del correo
    """
    try:
        contenido_texto = strip_tags(contenido_html)
        
        correo = CorreoPendiente.objects.create(
            idPedido=id_pedido,
            destinatario=destinatario,
            asunto=asunto,
            contenido_html=contenido_html,
            contenido_texto=contenido_texto,
            enviado=False,
            intentos=0
        )
        
        print(f"[OK] Correo encolado para pedido {id_pedido}: {destinatario}")
        return True
    except Exception as e:
        print(f"[ERROR] Error al encolar correo: {e}")
        return False


def enviar_correos_pendientes():
    """
    Envía todos los correos pendientes
    Debe ejecutarse periódicamente (ej: cada 5 minutos)
    """
    correos_pendientes = CorreoPendiente.objects.filter(
        enviado=False,
        intentos__lt=3  # Máximo 3 intentos
    ).order_by('fecha_creacion')[:10]  # Procesar máximo 10 correos por vez
    
    for correo in correos_pendientes:
        try:
            email = EmailMultiAlternatives(
                subject=correo.asunto,
                body=correo.contenido_texto,
                from_email='glamstore0303777@gmail.com',
                to=[correo.destinatario]
            )
            email.attach_alternative(correo.contenido_html, "text/html")
            
            resultado = email.send()
            
            if resultado > 0:
                correo.enviado = True
                correo.fecha_envio = timezone.now()
                correo.save()
                print(f"[OK] Correo enviado para pedido {correo.idPedido}: {correo.destinatario}")
            else:
                correo.intentos += 1
                correo.error = "No se pudo enviar el correo"
                correo.save()
                print(f"[ERROR] Fallo al enviar correo para pedido {correo.idPedido}")
        except Exception as e:
            correo.intentos += 1
            correo.error = str(e)
            correo.save()
            print(f"[ERROR] Error al enviar correo para pedido {correo.idPedido}: {e}")
