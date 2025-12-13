#!/usr/bin/env python
"""
Script para restaurar BD usando psql directamente
Uso: python restore_with_psql.py glamstoredb_postgres.sql
"""
import os
import sys
import subprocess
from django.conf import settings
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

def restore_with_psql(sql_file):
    """Restaurar usando psql"""
    
    if not os.path.exists(sql_file):
        print(f"✗ Archivo no encontrado: {sql_file}")
        sys.exit(1)
    
    db_config = settings.DATABASES['default']
    
    # Construir URL de conexión
    db_url = f"postgresql://{db_config['USER']}:{db_config['PASSWORD']}@{db_config['HOST']}:{db_config['PORT']}/{db_config['NAME']}"
    
    print(f"Restaurando BD usando psql...")
    print(f"Host: {db_config['HOST']}")
    print(f"BD: {db_config['NAME']}")
    print()
    
    # Ejecutar psql
    cmd = f"psql '{db_url}' < {sql_file}"
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✓ Restauración completada")
        
        # Verificar datos
        print("\nVerificando datos...")
        verify_data()
    else:
        print(f"✗ Error: {result.stderr}")
        sys.exit(1)


def verify_data():
    """Verificar que los datos se restauraron"""
    try:
        from core.models import Repartidor, NotificacionProblema
        
        repartidores = Repartidor.objects.count()
        notificaciones = NotificacionProblema.objects.count()
        
        print(f"  - Repartidores: {repartidores}")
        print(f"  - Notificaciones: {notificaciones}")
        
        if repartidores > 0 or notificaciones > 0:
            print(f"\n✓ Datos restaurados exitosamente")
        else:
            print(f"\n⚠ No se encontraron datos")
            
    except Exception as e:
        print(f"  ⚠ Error verificando: {e}")


if __name__ == '__main__':
    sql_file = sys.argv[1] if len(sys.argv) > 1 else 'glamstoredb_postgres.sql'
    restore_with_psql(sql_file)
