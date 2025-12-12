#!/usr/bin/env python
"""
Script para sincronizar datos de Render a GitHub
Exporta repartidores y notificaciones y hace commit automático
"""
import os
import sys
import django
import json
import subprocess
from datetime import datetime

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models.repartidores import Repartidor
from core.models.notificaciones import NotificacionProblema


def serialize_datetime(obj):
    """Serializar datetime a string ISO"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def export_data():
    """Exportar datos a JSON"""
    print("=== Exportando datos de Render ===\n")
    
    try:
        # Exportar repartidores
        print("Exportando repartidores...")
        repartidores = list(Repartidor.objects.all().values())
        with open('repartidores_export.json', 'w', encoding='utf-8') as f:
            json.dump(repartidores, f, indent=2, ensure_ascii=False, 
                     default=serialize_datetime)
        print(f"✓ Exportados {len(repartidores)} repartidores\n")
        
        # Exportar notificaciones
        print("Exportando notificaciones...")
        notificaciones = list(NotificacionProblema.objects.all().values())
        with open('notificaciones_export.json', 'w', encoding='utf-8') as f:
            json.dump(notificaciones, f, indent=2, ensure_ascii=False,
                     default=serialize_datetime)
        print(f"✓ Exportadas {len(notificaciones)} notificaciones\n")
        
        return True
    except Exception as e:
        print(f"✗ Error exportando datos: {e}\n")
        return False


def commit_and_push():
    """Hacer commit y push a GitHub"""
    print("=== Sincronizando con GitHub ===\n")
    
    try:
        # Configurar git
        subprocess.run(['git', 'config', 'user.email', 'bot@glamstore.com'], check=True)
        subprocess.run(['git', 'config', 'user.name', 'GlamStore Bot'], check=True)
        
        # Agregar archivos
        subprocess.run(['git', 'add', 'repartidores_export.json', 'notificaciones_export.json'], check=True)
        
        # Verificar si hay cambios
        result = subprocess.run(['git', 'diff', '--cached', '--quiet'], capture_output=True)
        
        if result.returncode == 0:
            print("✓ No hay cambios en los datos\n")
            return True
        
        # Hacer commit
        commit_msg = f"""Exportar datos de Render: repartidores y notificaciones

- Exportación automática de repartidores
- Exportación automática de notificaciones
- Timestamp: {datetime.now().isoformat()}"""
        
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
        print("✓ Commit realizado\n")
        
        # Hacer push
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("✓ Datos sincronizados a GitHub\n")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error en git: {e}\n")
        return False
    except Exception as e:
        print(f"✗ Error sincronizando: {e}\n")
        return False


if __name__ == '__main__':
    # Exportar datos
    if not export_data():
        sys.exit(1)
    
    # Sincronizar con GitHub (opcional, solo si está configurado)
    if os.environ.get('SYNC_TO_GITHUB') == 'true':
        if not commit_and_push():
            sys.exit(1)
    
    print("=== Sincronización completada ===")
