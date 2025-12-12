#!/bin/bash
# Script para ejecutar la restauración de BD en Render
# Uso: bash run_restore_in_render.sh

echo "=========================================="
echo "Restauración de Base de Datos en Render"
echo "=========================================="
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "manage.py" ]; then
    echo "✗ Error: manage.py no encontrado"
    echo "Asegúrate de estar en el directorio del proyecto"
    exit 1
fi

# Verificar que el archivo SQL existe
if [ ! -f "glamstoredb_postgres.sql" ]; then
    echo "✗ Error: glamstoredb_postgres.sql no encontrado"
    echo "Asegúrate de que el archivo está en el directorio actual"
    exit 1
fi

echo "✓ Archivos encontrados"
echo ""

# Ejecutar la restauración
echo "Iniciando restauración..."
python restore_database_final.py glamstoredb_postgres.sql

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ Restauración completada exitosamente"
    echo "=========================================="
    echo ""
    echo "Próximos pasos:"
    echo "1. Verifica los datos con: python manage.py shell"
    echo "2. Prueba la aplicación"
    echo "3. Si todo funciona, la BD está lista"
else
    echo ""
    echo "=========================================="
    echo "✗ Error durante la restauración"
    echo "=========================================="
    echo ""
    echo "Intenta ejecutar nuevamente o revisa los logs"
    exit 1
fi
