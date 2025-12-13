#!/usr/bin/env python
"""
Script de compatibilidad para Render
Redirige a ejecutar_en_render.py
"""
import sys
import os

# Ejecutar el script de restauración real
if __name__ == '__main__':
    print("Ejecutando restauración de datos...")
    
    # Importar y ejecutar el script principal
    from ejecutar_en_render import (
        crear_secuencias,
        restaurar_datos,
        verificar_datos
    )
    
    archivo_dump = 'glamstoredb.sql'
    
    # Verificar que el archivo existe
    if not os.path.exists(archivo_dump):
        print(f"⚠ Archivo '{archivo_dump}' no encontrado")
        print(f"  Directorio actual: {os.getcwd()}")
        print("  Continuando sin restauración...")
        sys.exit(0)
    
    print(f"✓ Archivo '{archivo_dump}' encontrado")
    
    try:
        if not crear_secuencias():
            print("⚠ Error creando secuencias (continuando...)")
        
        if not restaurar_datos(archivo_dump):
            print("⚠ Error restaurando datos (continuando...)")
        
        if not verificar_datos():
            print("⚠ Error verificando datos (continuando...)")
        
        print("\n✓ Restauración completada")
    except Exception as e:
        print(f"⚠ Error durante restauración: {str(e)}")
        print("  Continuando sin restauración...")
