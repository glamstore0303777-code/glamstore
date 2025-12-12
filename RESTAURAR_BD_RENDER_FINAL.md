# Restaurar Base de Datos en Render

## Pasos para restaurar la BD completa con todos los datos

### 1. Conectarse a Render
```bash
ssh render@srv-xxxxx
cd ~/project/src
```

### 2. Ejecutar el script de restauración
```bash
python restore_database_final.py glamstoredb_postgres.sql
```

Este script:
- Lee el archivo SQL convertido a PostgreSQL
- Parsea todos los statements SQL
- Los ejecuta uno por uno
- Muestra el progreso
- Verifica que los datos se restauraron correctamente

### 3. Verificar los datos
```bash
python manage.py shell
```

Luego en el shell de Django:
```python
from core.models import Repartidor, NotificacionProblema
print(f"Repartidores: {Repartidor.objects.count()}")
print(f"Notificaciones: {NotificacionProblema.objects.count()}")
```

### 4. Si algo falla

Si el script falla, intenta esto:

```bash
# Opción 1: Usar psql directamente
psql postgresql://glamstoredb_user:PASSWORD@HOST:5432/glamstoredb < glamstoredb_postgres.sql

# Opción 2: Usar el comando Django
python manage.py populate_data glamstoredb_postgres.sql

# Opción 3: Ejecutar el script mejorado
python restore_database_final.py glamstoredb_postgres.sql
```

## Archivos necesarios

- `glamstoredb_postgres.sql` - Dump de la BD convertido a PostgreSQL
- `restore_database_final.py` - Script de restauración mejorado
- `convert_mysql_to_postgres.py` - Script para convertir MySQL a PostgreSQL

## Notas importantes

- El archivo `glamstoredb.sql` es MySQL y NO funcionará directamente en PostgreSQL
- Debe convertirse primero a `glamstoredb_postgres.sql`
- La conversión ya está hecha y subida a GitHub
- El script `restore_database_final.py` maneja errores comunes automáticamente
