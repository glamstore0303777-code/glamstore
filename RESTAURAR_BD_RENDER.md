# Restaurar Base de Datos en Render

Este documento explica cómo restaurar la BD en Render desde el archivo SQL `glamstoredb.sql`.

## Problema

La BD en Render está vacía (0 repartidores, 0 notificaciones) pero los datos ya existen en el archivo SQL local `glamstoredb.sql`.

## Solución

### Paso 1: Subir el archivo SQL a GitHub

```bash
git add glamstoredb.sql
git commit -m "Add SQL dump for database restore"
git push origin main
```

### Paso 2: Restaurar BD en Render

Tienes dos opciones:

#### Opción A: Usar la consola de Render (recomendado)

1. Ve a https://dashboard.render.com
2. Abre tu servicio de Render
3. Haz clic en "Shell" en la parte superior
4. Ejecuta los siguientes comandos:

```bash
cd ~/project/src
python manage.py populate_data glamstoredb.sql
```

Esto restaurará toda la BD desde el archivo SQL.

#### Opción B: Usar el script Python (local)

```bash
python restore_db_render.py
```

Este script:
- Verifica que `glamstoredb.sql` existe
- Lo sube a GitHub
- Te muestra los pasos a seguir en Render

### Paso 3: Verificar que los datos se restauraron

En la consola de Render, ejecuta:

```bash
python manage.py export_data
```

Deberías ver algo como:

```
Exportando datos...
✓ Exportados X repartidores a repartidores_export.json
✓ Exportadas Y notificaciones a notificaciones_export.json
✓ Exportación completada
```

Si ves números mayores a 0, ¡la restauración fue exitosa!

### Paso 4: Sincronizar datos exportados a GitHub (opcional)

Si quieres guardar los datos exportados en GitHub:

```bash
git add repartidores_export.json notificaciones_export.json
git commit -m "Export data from restored database"
git push origin main
```

## Archivos Involucrados

- `glamstoredb.sql` - Dump completo de la BD con todos los datos
- `core/management/commands/populate_data.py` - Comando Django para restaurar desde SQL
- `core/management/commands/export_data.py` - Comando Django para exportar datos a JSON
- `restore_db_render.py` - Script Python para automatizar el proceso
- `restore_and_export.sh` - Script bash para ejecutar en Render

## Notas Importantes

1. **Backup**: Asegúrate de tener un backup de la BD actual antes de restaurar
2. **Datos existentes**: La restauración sobrescribirá los datos existentes
3. **Permisos**: Necesitas acceso a la consola de Render para ejecutar los comandos
4. **Tiempo**: Dependiendo del tamaño del SQL, puede tomar algunos minutos

## Troubleshooting

### Error: "Archivo no encontrado: glamstoredb.sql"

Asegúrate de que el archivo está en la raíz del proyecto y que fue subido a GitHub.

### Error: "Unknown command: 'populate_data'"

Ejecuta:
```bash
python manage.py migrate
```

Luego intenta de nuevo.

### La BD sigue vacía después de restaurar

1. Verifica que no hay errores en los logs de Render
2. Intenta ejecutar `python manage.py export_data` para ver si hay datos
3. Si sigue vacío, revisa el contenido del archivo SQL

## Próximos Pasos

Una vez restaurada la BD:

1. Verifica que `/gestion/repartidores/` funciona correctamente
2. Verifica que `/gestion/notificaciones/` funciona correctamente
3. Haz un commit con los cambios
4. Redeploy en Render si es necesario
