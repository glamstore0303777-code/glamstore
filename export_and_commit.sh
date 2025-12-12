#!/bin/bash
# Script para exportar datos de Render y hacer commit automático

echo "=== Exportando datos de Render ==="

# Ejecutar el comando de exportación
python manage.py export_data

# Verificar si los archivos fueron creados
if [ -f "repartidores_export.json" ] && [ -f "notificaciones_export.json" ]; then
    echo "✓ Archivos exportados exitosamente"
    
    # Configurar git
    git config user.email "bot@glamstore.com"
    git config user.name "GlamStore Bot"
    
    # Agregar los archivos
    git add repartidores_export.json notificaciones_export.json
    
    # Hacer commit si hay cambios
    if git diff --cached --quiet; then
        echo "✓ No hay cambios en los datos"
    else
        git commit -m "Exportar datos de Render: repartidores y notificaciones

- Exportación automática de repartidores
- Exportación automática de notificaciones
- Timestamp: $(date)"
        
        # Hacer push
        git push origin main
        echo "✓ Datos sincronizados a GitHub"
    fi
else
    echo "✗ Error: No se pudieron crear los archivos de exportación"
    exit 1
fi

echo "=== Exportación completada ==="
