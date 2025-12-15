#!/bin/bash

# Script para aplicar los fixes

echo "🔧 Aplicando fixes a Glamstore..."
echo ""

# 1. Ejecutar migraciones
echo "📦 Ejecutando migraciones..."
python manage.py migrate

echo ""
echo "✅ Migraciones completadas"
echo ""

# 2. Procesar correos pendientes
echo "📧 Procesando correos pendientes..."
python manage.py enviar_correos_pendientes

echo ""
echo "✅ Correos procesados"
echo ""

echo "🎉 Todos los fixes han sido aplicados exitosamente"
echo ""
echo "Próximos pasos:"
echo "1. Configura un cron job para ejecutar: python manage.py enviar_correos_pendientes"
echo "2. Prueba la asignación de repartidores"
echo "3. Verifica que las notificaciones cargan correctamente"
