# Guía Completa: Configuración y Envío de Correos

## Problema: Los correos no se están enviando

Si los correos no llegan a los clientes, sigue estos pasos:

---

## PASO 1: Verificar la Configuración Local

### 1.1 Ejecutar el diagnóstico
```bash
python diagnostico_correos.py
```

Este script te mostrará:
- ✓ Si la configuración de Gmail está correcta
- ✓ Cuántos correos están encolados
- ✓ Cuántos se han enviado
- ✓ Si hay errores

### 1.2 Verificar el archivo `.env`
Asegúrate de que tienes:
```
EMAIL_HOST_USER='glamstore0303777@gmail.com'
EMAIL_HOST_PASSWORD='lyuuvczxwhbljttc'
```

**IMPORTANTE**: La contraseña debe ser una **contraseña de aplicación de Gmail**, no tu contraseña normal.

---

## PASO 2: Enviar Correos Manualmente (Local)

Si hay correos encolados, ejecuta:
```bash
python manage.py enviar_correos_pendientes
```

Esto enviará todos los correos pendientes inmediatamente.

---

## PASO 3: Verificar en la Base de Datos

### 3.1 Ver correos encolados
```bash
python manage.py shell
>>> from core.models.correos_pendientes import CorreoPendiente
>>> CorreoPendiente.objects.all().count()  # Total de correos
>>> CorreoPendiente.objects.filter(enviado=False).count()  # Pendientes
>>> CorreoPendiente.objects.filter(enviado=True).count()  # Enviados
```

### 3.2 Ver detalles de un correo
```bash
>>> correo = CorreoPendiente.objects.first()
>>> print(f"Destinatario: {correo.destinatario}")
>>> print(f"Asunto: {correo.asunto}")
>>> print(f"Enviado: {correo.enviado}")
>>> print(f"Error: {correo.error}")
```

---

## PASO 4: Configuración en Render (Producción)

El cron job ya está configurado en `render.yaml`:
```yaml
jobs:
  - type: cron
    name: enviar-correos-pendientes
    schedule: "*/5 * * * *"
    command: "python manage.py enviar_correos_pendientes"
```

Esto ejecuta el comando cada 5 minutos automáticamente.

### 4.1 Verificar que el cron job está activo
1. Ve a tu dashboard de Render
2. Selecciona tu servicio
3. Ve a la sección "Cron Jobs"
4. Verifica que "enviar-correos-pendientes" esté activo

### 4.2 Ver logs del cron job
1. En Render, ve a "Logs"
2. Busca mensajes de "enviar_correos_pendientes"
3. Verifica si hay errores

---

## PASO 5: Solucionar Problemas Comunes

### Problema: "No se pudo importar la implementación de psycopg"
**Solución**: Esto es solo una advertencia, no afecta el envío de correos.

### Problema: "SMTP authentication failed"
**Solución**: 
1. Verifica que `EMAIL_HOST_PASSWORD` sea una contraseña de aplicación
2. Genera una nueva en: https://myaccount.google.com/apppasswords
3. Actualiza `.env` con la nueva contraseña

### Problema: "Connection refused"
**Solución**:
1. Verifica que `EMAIL_HOST = 'smtp.gmail.com'`
2. Verifica que `EMAIL_PORT = 587`
3. Verifica que `EMAIL_USE_TLS = True`

### Problema: Los correos se encolan pero no se envían
**Solución**:
1. Ejecuta manualmente: `python manage.py enviar_correos_pendientes`
2. Verifica los logs para errores
3. Revisa que el cron job esté activo en Render

---

## PASO 6: Prueba Completa

### 6.1 Crear un pedido de prueba
1. Ve a tu tienda
2. Agrega productos al carrito
3. Confirma el pedido
4. El correo debe encolarse automáticamente

### 6.2 Verificar que se encoló
```bash
python diagnostico_correos.py
```

Deberías ver un correo pendiente.

### 6.3 Enviar el correo
```bash
python manage.py enviar_correos_pendientes
```

### 6.4 Verificar que se envió
```bash
python diagnostico_correos.py
```

El correo debe aparecer como "Enviado".

---

## PASO 7: Monitoreo Continuo

### 7.1 Ejecutar diagnóstico regularmente
```bash
python diagnostico_correos.py
```

### 7.2 Revisar logs en Render
- Ve a tu dashboard de Render
- Selecciona tu servicio
- Ve a "Logs"
- Busca "enviar_correos_pendientes"

### 7.3 Configurar alertas (Opcional)
En Render, puedes configurar notificaciones si el cron job falla.

---

## Resumen Rápido

| Acción | Comando |
|--------|---------|
| Ver estado de correos | `python diagnostico_correos.py` |
| Enviar correos pendientes | `python manage.py enviar_correos_pendientes` |
| Ver correos en BD | `python manage.py shell` |
| Verificar configuración | Revisar `.env` |
| Ver logs en Render | Dashboard → Logs |

---

## Contacto y Soporte

Si los correos aún no funcionan:
1. Ejecuta `python diagnostico_correos.py`
2. Revisa los logs en Render
3. Verifica que `EMAIL_HOST_PASSWORD` esté configurado
4. Intenta generar una nueva contraseña de aplicación de Gmail

**Nota**: Los correos se envían cada 5 minutos en Render. Si confirmas un pedido, espera hasta 5 minutos para que llegue el correo.
