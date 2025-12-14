# Configuración de Envío de Correos - Glam Store

## Estado Actual
✅ La configuración de correos ya está implementada en el código
✅ La contraseña de aplicación de Gmail ya está en `.env`

## Cómo Funciona el Sistema de Correos

El sistema utiliza un modelo de **correos encolados** para garantizar que los correos se envíen de forma confiable:

1. **Encolar Correo**: Cuando se confirma un pedido, se encola un correo en la tabla `correos_pendientes`
2. **Enviar Pendientes**: Un comando de Django envía todos los correos encolados
3. **Reintentos**: Si falla, reintentar hasta 3 veces

## Configuración en `.env`

Tu archivo `.env` ya tiene:
```
EMAIL_HOST_USER='glamstore0303777@gmail.com'
EMAIL_HOST_PASSWORD='lyuuvczxwhbljttc'
```

## Configuración en `glamstore/settings.py`

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'glamstore0303777@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'Glam Store <glamstore0303777@gmail.com>'
```

## Cómo Enviar Correos Pendientes

### Opción 1: Comando de Django (Local)
```bash
python manage.py enviar_correos_pendientes
```

### Opción 2: En Render (Producción)
Necesitas configurar un **Cron Job** en Render para ejecutar el comando periódicamente.

En tu `render.yaml`, agrega:
```yaml
services:
  - type: web
    name: glamstore
    # ... resto de configuración ...

jobs:
  - type: cron
    name: enviar-correos-pendientes
    schedule: "*/5 * * * *"  # Cada 5 minutos
    command: "python manage.py enviar_correos_pendientes"
```

### Opción 3: Verificar Correos Encolados (Local)
```bash
python manage.py shell
>>> from core.models.correos_pendientes import CorreoPendiente
>>> CorreoPendiente.objects.filter(enviado=False).count()
```

## Flujo de Envío de Correos de Pedidos

1. **Cliente confirma pedido** → Se encola correo en `correos_pendientes`
2. **Comando ejecuta** → Envía todos los correos pendientes
3. **Correo llega al cliente** → Con factura HTML adjunta

## Archivos Involucrados

- `core/services/correos_service.py` - Lógica de envío
- `core/models/correos_pendientes.py` - Modelo de correos encolados
- `core/management/commands/enviar_correos_pendientes.py` - Comando de Django
- `core/Clientes/views.py` - Donde se encolan los correos (línea ~665)

## Prueba Local

1. Confirma un pedido en local
2. Ejecuta: `python manage.py enviar_correos_pendientes`
3. Verifica que el correo se envió correctamente

## Solución de Problemas

### Los correos no se envían
1. Verifica que `EMAIL_HOST_PASSWORD` esté en `.env`
2. Verifica que la contraseña sea una **contraseña de aplicación** de Gmail (no la contraseña normal)
3. Ejecuta el comando manualmente: `python manage.py enviar_correos_pendientes`
4. Revisa los logs en Render

### Contraseña de Aplicación de Gmail
Si necesitas generar una nueva:
1. Ve a https://myaccount.google.com/apppasswords
2. Selecciona "Mail" y "Windows Computer"
3. Copia la contraseña generada
4. Actualiza `EMAIL_HOST_PASSWORD` en `.env`

### Ver Errores de Envío
```bash
python manage.py shell
>>> from core.models.correos_pendientes import CorreoPendiente
>>> correos = CorreoPendiente.objects.filter(enviado=False)
>>> for c in correos:
...     print(f"Pedido {c.idPedido}: {c.error}")
```

## Próximos Pasos

1. **En Render**: Configura el cron job en `render.yaml` para ejecutar el comando cada 5 minutos
2. **Prueba**: Confirma un pedido y verifica que llegue el correo
3. **Monitoreo**: Revisa regularmente los correos encolados para detectar problemas
