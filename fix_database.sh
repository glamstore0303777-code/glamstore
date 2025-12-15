#!/bin/bash

echo "🔧 Reparando la base de datos..."
echo ""

# 1. Ejecutar migraciones
echo "📦 Ejecutando migraciones..."
python manage.py migrate

echo ""
echo "✅ Migraciones completadas"
echo ""

# 2. Verificar estado
echo "🔍 Verificando estado de la BD..."
python manage.py shell << EOF
from django.db import connection
from core.models import Distribuidor, NotificacionProblema, CorreoPendiente

# Verificar tablas
with connection.cursor() as cursor:
    # Distribuidores
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_name = 'distribuidores'
        );
    """)
    print(f"✅ Tabla distribuidores: {'Existe' if cursor.fetchone()[0] else 'NO existe'}")
    
    # Notificaciones
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_name = 'notificaciones_problema'
        );
    """)
    print(f"✅ Tabla notificaciones_problema: {'Existe' if cursor.fetchone()[0] else 'NO existe'}")
    
    # Correos pendientes
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_name = 'correos_pendientes'
        );
    """)
    print(f"✅ Tabla correos_pendientes: {'Existe' if cursor.fetchone()[0] else 'NO existe'}")

# Contar registros
try:
    dist_count = Distribuidor.objects.count()
    print(f"📊 Distribuidores: {dist_count}")
except Exception as e:
    print(f"❌ Error al contar distribuidores: {e}")

try:
    notif_count = NotificacionProblema.objects.count()
    print(f"📊 Notificaciones: {notif_count}")
except Exception as e:
    print(f"❌ Error al contar notificaciones: {e}")

try:
    correos_count = CorreoPendiente.objects.count()
    print(f"📊 Correos pendientes: {correos_count}")
except Exception as e:
    print(f"❌ Error al contar correos: {e}")
EOF

echo ""
echo "✅ Diagnóstico completado"
