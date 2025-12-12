#!/bin/bash
# Script para restaurar BD desde SQL y exportar datos en Render

set -e

echo "=========================================="
echo "Restaurando BD desde glamstoredb.sql..."
echo "=========================================="

cd ~/project/src

# Restaurar BD desde SQL
python manage.py populate_data glamstoredb.sql

echo ""
echo "=========================================="
echo "Exportando datos a JSON..."
echo "=========================================="

# Exportar datos
python manage.py export_data

echo ""
echo "=========================================="
echo "✓ Proceso completado"
echo "=========================================="
