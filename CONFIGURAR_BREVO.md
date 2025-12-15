# Configuración de Brevo para Envío de Correos

## ¿Qué es Brevo?
Brevo (anteriormente Sendinblue) es un servicio profesional de envío de correos. Es mucho más confiable que Gmail para producción.

## PASO 1: Crear Cuenta en Brevo

1. Ve a https://www.brevo.com/
2. Haz clic en "Sign Up" (Registrarse)
3. Completa el formulario con:
   - Email: Tu email
   - Contraseña: Una contraseña segura
   - Nombre de empresa: Glam Store
4. Verifica tu email
5. Completa el perfil

## PASO 2: Obtener la API Key

1. Inicia sesión en Brevo
2. Ve a "Settings" (Configuración) → "SMTP & API"
3. En la sección "API Keys", haz clic en "Create a new API key"
4. Dale un nombre: "Glam Store Django"
5. Copia la API Key (es una cadena larga)

## PASO 3: Configurar en tu Proyecto

### 3.1 Agregar a `.env`
```
BREVO_API_KEY='tu_api_key_aqui'
```

Reemplaza `tu_api_key_aqui` con la API Key que copiaste.

### 3.2 Verificar `requirements.txt`
Ya está agregado:
```
sib-api-v3-sdk==7.6.0
```

### 3.3 Instalar dependencias (Local)
```bash
pip install -r requirements.txt
```

## PASO 4: Verificar Remitente

1. En Brevo, ve a "Senders & Contacts" → "Senders"
2. Verifica que `glamstore0303777@gmail.com` esté registrado
3. Si no está, agrega el email:
   - Haz clic en "Add a sender"
   - Email: glamstore0303777@gmail.com
   - Nombre: Glam Store
   - Verifica el email

## PASO 5: Probar Localmente

```bash
python manage.py shell
>>> from core.services.brevo_service import enviar_correo_brevo
>>> enviar_correo_brevo(
...     destinatario='tu_email@gmail.com',
...     asunto='Prueba de Brevo',
...     contenido_html='<h1>¡Funciona!</h1>'
... )
```

Si ves `[OK] Correo enviado`, ¡está funcionando!

## PASO 6: Desplegar en Render

1. Ve a tu dashboard de Render
2. Selecciona tu servicio
3. Ve a "Environment"
4. Agrega una nueva variable:
   - Key: `BREVO_API_KEY`
   - Value: Tu API Key de Brevo
5. Haz clic en "Save"
6. Render redesplegará automáticamente

## PASO 7: Probar en Producción

1. Ve a tu tienda en Render
2. Confirma un pedido
3. Verifica que el correo llegue al cliente

## Ventajas de Brevo

✓ Más confiable que Gmail
✓ Mejor entrega de correos
✓ Soporte profesional
✓ Plan gratuito: 300 correos/día
✓ No requiere cron jobs
✓ Envío inmediato

## Límites del Plan Gratuito

- 300 correos por día
- Contactos ilimitados
- Soporte por email

Si necesitas más, puedes actualizar a un plan de pago.

## Solución de Problemas

### Error: "API key not found"
- Verifica que `BREVO_API_KEY` esté en `.env`
- Verifica que la API Key sea correcta

### Error: "Sender not verified"
- Ve a Brevo → Senders
- Verifica que `glamstore0303777@gmail.com` esté verificado

### Los correos no llegan
- Revisa la carpeta de spam
- Verifica en Brevo → Statistics que se hayan enviado
- Revisa los logs en Render

## Documentación Oficial

- Brevo: https://www.brevo.com/
- API Docs: https://developers.brevo.com/
- Python SDK: https://github.com/getbrevo/brevo-python

## Resumen

| Paso | Acción |
|------|--------|
| 1 | Crear cuenta en Brevo |
| 2 | Obtener API Key |
| 3 | Agregar a `.env` |
| 4 | Verificar remitente |
| 5 | Probar localmente |
| 6 | Desplegar en Render |
| 7 | Probar en producción |

¡Listo! Los correos ahora se enviarán con Brevo.
