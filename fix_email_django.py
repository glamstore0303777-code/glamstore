#!/usr/bin/env python
"""
Script para aumentar el tamaño del campo email usando Django
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection

try:
    print("Aumentando tamaño del campo email en tabla usuarios...")
    with connection.cursor() as cursor:
        cursor.execute("""
            ALTER TABLE usuarios
            ALTER COLUMN email TYPE character varying(255);
        """)
    
    print("✓ Campo email actualizado a 255 caracteres")
    
except Exception as e:
    print(f"✗ Error: {str(e)}")
