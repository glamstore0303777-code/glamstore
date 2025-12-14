#!/bin/bash
# Script para ejecutar después del deploy en Render
# Restaura los datos desde el dump de MySQL

echo "=== Post-Deploy: Restaurando datos ==="

# Esperar a que la BD esté lista
sleep 5

# Ejecutar migraciones pendientes
echo "Ejecutando migraciones..."
python manage.py migrate

# Ejecutar la restauración
python ejecutar_en_render.py glamstoredb.sql

echo "=== Post-Deploy completado ==="
