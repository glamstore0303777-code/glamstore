#!/bin/bash

echo "=========================================="
echo "Ejecutando diagnóstico inicial..."
echo "=========================================="
python diagnostico_movimientos_lote.py

echo ""
echo "=========================================="
echo "Ejecutando migraciones..."
echo "=========================================="
python manage.py migrate

echo ""
echo "=========================================="
echo "Ejecutando diagnóstico final..."
echo "=========================================="
python diagnostico_movimientos_lote.py

echo ""
echo "=========================================="
echo "¡Proceso completado!"
echo "=========================================="
