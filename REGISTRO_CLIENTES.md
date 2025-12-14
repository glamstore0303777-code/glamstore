# Sistema de Registro de Clientes - Glam Store

## Descripción General

El sistema de registro permite que nuevos clientes creen una cuenta en Glam Store. El proceso es simple y seguro.

## Flujo de Registro

### 1. Acceso a la Página de Registro
- URL: `/registro/`
- Desde la página de login, haz clic en "Regístrate"
- O desde la tienda, accede directamente a `/registro/`

### 2. Formulario de Registro
El formulario solicita los siguientes datos:

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| Nombre Completo | Texto | Sí | Tu nombre completo |
| Correo Electrónico | Email | Sí | Tu correo (debe ser único) |
| Cédula | Texto | Sí | Tu número de identificación |
| Dirección | Texto | Sí | Tu dirección de residencia |
| Teléfono | Teléfono | Sí | Tu número de contacto |
| Contraseña | Contraseña | Sí | Mínimo 6 caracteres |
| Confirmar Contraseña | Contraseña | Sí | Debe coincidir con la contraseña |

### 3. Validaciones

El sistema valida:

✓ **Campos requeridos**: Todos los campos deben estar completos
✓ **Email único**: No puede haber dos cuentas con el mismo correo
✓ **Contraseñas coinciden**: Las dos contraseñas deben ser idénticas
✓ **Longitud mínima**: La contraseña debe tener al menos 6 caracteres

### 4. Creación de Cuenta

Cuando envías el formulario:

1. Se crea un registro de **Cliente** con tus datos personales
2. Se crea un registro de **Usuario** vinculado al cliente
3. Se asigna automáticamente el rol de **Cliente** (rol=2)
4. Se guarda la contraseña de forma segura (hasheada)

### 5. Después del Registro

- Recibirás un mensaje de éxito
- Serás redirigido a la página de login
- Inicia sesión con tu correo y contraseña
- Accederás a tu perfil y podrás hacer compras

## Casos Especiales

### Cliente que ya hizo un pedido como invitado

Si ya hiciste un pedido sin registrarte:

1. Cuando te registres con el mismo correo
2. Tu cuenta de cliente existente se actualizará con tus datos
3. Se creará un usuario vinculado a esa cuenta
4. Podrás ver todos tus pedidos anteriores en tu perfil

### Email ya registrado

Si intentas registrarte con un email que ya tiene una cuenta:

1. Verás un mensaje de error
2. Se te ofrecerá un botón para ir a iniciar sesión
3. Si olvidaste tu contraseña, usa la opción "Recuperar contraseña"

## Seguridad

- Las contraseñas se almacenan hasheadas (no en texto plano)
- Se valida que el email sea único
- Se requiere confirmación de contraseña
- Se valida la longitud mínima de contraseña

## Troubleshooting

### "Las contraseñas no coinciden"
- Verifica que ambas contraseñas sean exactamente iguales
- Recuerda que es sensible a mayúsculas/minúsculas

### "La contraseña debe tener al menos 6 caracteres"
- Usa una contraseña más larga
- Ejemplo: `MiPassword123`

### "Ya tienes una cuenta registrada con este correo"
- Usa otro correo para crear una nueva cuenta
- O inicia sesión con tu correo actual
- Si olvidaste la contraseña, usa "Recuperar contraseña"

### "Por favor completa todos los campos"
- Asegúrate de llenar todos los campos del formulario
- No dejes ninguno en blanco

## Estructura de Base de Datos

### Tabla: clientes
```sql
CREATE TABLE clientes (
    idcliente SERIAL PRIMARY KEY,
    cedula VARCHAR(20),
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    direccion VARCHAR(200),
    telefono VARCHAR(20)
);
```

### Tabla: usuarios
```sql
CREATE TABLE usuarios (
    idusuario SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    id_rol INTEGER,
    idcliente INTEGER,
    fechacreacion TIMESTAMP,
    nombre VARCHAR(50),
    telefono VARCHAR(20),
    direccion VARCHAR(50),
    reset_token VARCHAR(255),
    reset_token_expires TIMESTAMP,
    ultimoacceso TIMESTAMP,
    FOREIGN KEY (idcliente) REFERENCES clientes(idcliente)
);
```

## Código Relevante

### Vista de Registro (core/Clientes/views.py)
```python
def registro(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        # Validar datos
        # Crear cliente
        # Crear usuario
        # Redirigir a login
```

### Template (core/Clientes/registrar_usuario/registrar_usuario.html)
- Formulario HTML con validación del lado del cliente
- Estilos personalizados de Glam Store
- Mensajes de error y éxito

### URLs (core/Clientes/urls.py)
```python
path('registro/', views.registro, name='registro'),
```

## Testing

Para probar el sistema de registro:

```bash
python manage.py shell < test_registro.py
```

Este script:
1. Crea un cliente de prueba
2. Crea un usuario de prueba
3. Verifica que se crearon correctamente
4. Verifica la autenticación

## Próximos Pasos

Después de registrarte:

1. **Completa tu perfil**: Agrega más información si es necesario
2. **Explora la tienda**: Navega por los productos
3. **Haz tu primer pedido**: Agrega productos al carrito y compra
4. **Recibe tu pedido**: Sigue el estado de tu pedido en tu perfil

## Soporte

Si tienes problemas con el registro:

- Contacta a: glamstore0303777@gmail.com
- Teléfono: [Tu número de contacto]
- Chat: [Si tienes chat disponible]
