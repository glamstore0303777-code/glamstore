# Instrucciones Finales - Restauración de BD en Render

## Problema resuelto
El deploy anterior fallaba porque buscaba `restore_data.py` que no existe. He reorganizado todo para que funcione correctamente.

## Cambios realizados

### 1. Simplificación del `build.sh`
- Ahora solo ejecuta: migraciones, inicialización de BD y recopilación de archivos estáticos
- NO intenta restaurar datos (eso se hace después del deploy)

### 2. Nuevo `post_deploy.sh`
- Se ejecuta DESPUÉS de que el deploy esté completo
- Ejecuta `python ejecutar_en_render.py glamstoredb.sql`
- Restaura todos los datos desde el dump de MySQL

### 3. Actualización de `render.yaml`
- Agregué `postDeployCommand: bash post_deploy.sh`
- Esto asegura que la restauración se ejecute después del deploy

## Cómo funciona ahora

### Durante el build (build.sh):
1. ✓ Ejecuta migraciones
2. ✓ Inicializa usuarios básicos
3. ✓ Recopila archivos estáticos
4. ✓ Inicia el servidor

### Después del deploy (post_deploy.sh):
1. ✓ Espera 5 segundos a que todo esté listo
2. ✓ Ejecuta `ejecutar_en_render.py`
3. ✓ Crea secuencias de auto-incremento
4. ✓ Restaura todos los datos desde `glamstoredb.sql`
5. ✓ Verifica que se insertaron correctamente

## Próximos pasos

### 1. Haz redeploy en Render
- Ve a https://dashboard.render.com
- Selecciona "glamstore"
- Haz clic en "Manual Deploy" o "Redeploy"
- Espera a que termine (incluye el post-deploy)

### 2. Verifica que funcionó
```bash
python manage.py shell
```

```python
from core.models import Repartidor, Usuario, Cliente, Pedido

print(f"Repartidores: {Repartidor.objects.count()}")
print(f"Usuarios: {Usuario.objects.count()}")
print(f"Clientes: {Cliente.objects.count()}")
print(f"Pedidos: {Pedido.objects.count()}")

# Ver un repartidor
if Repartidor.objects.exists():
    r = Repartidor.objects.first()
    print(f"\nPrimer repartidor: {r.nombre} ({r.email})")
```

### 3. Prueba el registro de clientes
- Ve a la página de registro
- Intenta crear una nueva cuenta
- Debería funcionar sin errores

### 4. Prueba el login
- Intenta iniciar sesión con una cuenta existente
- Debería funcionar correctamente

## Archivos importantes

- `build.sh` - Script de build (simplificado)
- `post_deploy.sh` - Script de post-deploy (restauración)
- `ejecutar_en_render.py` - Script de restauración de datos
- `render.yaml` - Configuración de Render
- `glamstoredb.sql` - Dump de MySQL con todos los datos

## Si algo falla

### Error: "Archivo 'glamstoredb.sql' no encontrado"
- Verifica que `glamstoredb.sql` esté en el repositorio
- Asegúrate de que está en la raíz del proyecto

### Error: "duplicate key value violates unique constraint"
- Limpia las tablas antes de restaurar:
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

### El post-deploy no se ejecuta
- Verifica que `post_deploy.sh` esté en el repositorio
- Verifica que `render.yaml` tenga `postDeployCommand: bash post_deploy.sh`
- Haz un nuevo redeploy

## Resumen

Todo está configurado para que:
1. El build sea rápido y simple
2. La restauración de datos se haga después del deploy
3. El servidor esté listo antes de restaurar datos
4. El registro de clientes funcione correctamente

¡Listo para hacer redeploy!
