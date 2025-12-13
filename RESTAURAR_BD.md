# Restauración de Base de Datos en Render

## Problema
La BD en Render no tiene los datos de repartidores, notificaciones y otros. Además, hay problemas con:
- Secuencias faltantes en PostgreSQL
- Nombres de columnas que no coinciden (MySQL vs PostgreSQL)
- El registro de clientes no funciona porque `idusuario` no se genera automáticamente

## Solución

### Paso 1: Subir los archivos a Render
Asegúrate de que estos archivos estén en el repositorio:
- `glamstoredb.sql` - Dump original de MySQL con todos los datos
- `ejecutar_en_render.py` - Script para restaurar la BD

### Paso 2: Ejecutar en Render
Conéctate a Render y ejecuta:

```bash
python ejecutar_en_render.py glamstoredb.sql
```

Este script hará:
1. **Crear secuencias** - Crea las secuencias de auto-incremento para todas las tablas
2. **Restaurar datos** - Inserta todos los datos del dump de MySQL
3. **Verificar** - Muestra cuántos registros se insertaron

### Paso 3: Verificar en Django Shell
```bash
python manage.py shell
```

Luego ejecuta:
```python
from core.models import Repartidor, Usuario, Cliente, Pedido
print(f"Repartidores: {Repartidor.objects.count()}")
print(f"Usuarios: {Usuario.objects.count()}")
print(f"Clientes: {Cliente.objects.count()}")
print(f"Pedidos: {Pedido.objects.count()}")

# Ver un repartidor
if Repartidor.objects.exists():
    print(Repartidor.objects.first())
```

## Cambios en el código

### 1. Función de registro (`core/Clientes/views.py`)
Se cambió para usar raw SQL en lugar de Django ORM:
```python
with connection.cursor() as cursor:
    cursor.execute("""
        INSERT INTO usuarios (email, password, id_rol, idcliente, fechacreacion, nombre, telefono, direccion)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, [email, make_password(password), 2, cliente.idCliente, timezone.now(), nombre, telefono, direccion])
```

Esto permite que PostgreSQL genere automáticamente el `idusuario` usando la secuencia.

### 2. Modelos
- `core/models/repartidores.py` - Tiene `db_column` mappings para convertir nombres
- `core/models/usuarios.py` - Tiene `managed=False` pero ahora con secuencias

## Mapeo de columnas
El script convierte automáticamente:
- `idRepartidor` → `idrepartidor`
- `nombreRepartidor` → `nombre`
- `estado_turno` → (se ignora, no existe en PostgreSQL)

## Si algo falla

### Error: "duplicate key value violates unique constraint"
Significa que hay datos duplicados. Limpia la tabla primero:
```bash
python manage.py shell
```
```python
from django.db import connection
cursor = connection.cursor()
cursor.execute("TRUNCATE TABLE repartidores CASCADE;")
cursor.execute("TRUNCATE TABLE usuarios CASCADE;")
cursor.execute("TRUNCATE TABLE clientes CASCADE;")
```

### Error: "column does not exist"
Verifica que el mapeo de columnas sea correcto en `ejecutar_en_render.py`

### Error: "null value in column 'idusuario'"
Significa que la secuencia no se creó. El script `ejecutar_en_render.py` lo hace automáticamente.

## Próximos pasos
1. Ejecuta el script en Render
2. Verifica que los datos se insertaron
3. Prueba el registro de clientes
4. Prueba el login
