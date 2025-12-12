#!/usr/bin/env python
"""
Script para restaurar BD en Render desde archivo SQL
Ejecuta el comando populate_data en Render
"""
import subprocess
import sys
import os

def run_command(cmd, description):
    """Ejecutar comando y mostrar resultado"""
    print(f"\n{'='*50}")
    print(f"{description}")
    print(f"{'='*50}")
    print(f"Ejecutando: {cmd}\n")
    
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n✗ Error ejecutando: {cmd}")
        sys.exit(1)
    print(f"✓ {description} completado")

def main():
    print("\n" + "="*50)
    print("RESTAURAR BD EN RENDER")
    print("="*50)
    
    # Verificar que el archivo SQL existe
    if not os.path.exists('glamstoredb.sql'):
        print("\n✗ Error: No se encontró glamstoredb.sql")
        sys.exit(1)
    
    print("\n✓ Archivo glamstoredb.sql encontrado")
    
    # Hacer commit del archivo SQL si no está en git
    run_command(
        "git add glamstoredb.sql && git commit -m 'Add SQL dump for restore' || true",
        "Agregando glamstoredb.sql a git"
    )
    
    # Push a GitHub
    run_command(
        "git push origin main",
        "Subiendo cambios a GitHub"
    )
    
    print("\n" + "="*50)
    print("PRÓXIMOS PASOS EN RENDER:")
    print("="*50)
    print("""
1. Ve a https://dashboard.render.com
2. Abre tu servicio de Render
3. Ve a la sección "Shell" o "Console"
4. Ejecuta:
   
   cd ~/project/src
   python manage.py populate_data glamstoredb.sql
   python manage.py export_data

5. Verifica que se exportaron los datos:
   - repartidores_export.json
   - notificaciones_export.json

6. Haz commit de los archivos exportados:
   git add repartidores_export.json notificaciones_export.json
   git commit -m "Export data from restored database"
   git push origin main
    """)

if __name__ == '__main__':
    main()
