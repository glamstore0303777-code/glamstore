#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection

# Limpiar TODAS las migraciones de core
with connection.cursor() as cursor:
    # Eliminar todas las migraciones de core
    cursor.execute("DELETE FROM django_migrations WHERE app='core'")
    
    print("✓ Todas las migraciones de core han sido eliminadas del historial")
    
    # Ver migraciones restantes
    cursor.execute("SELECT COUNT(*) FROM django_migrations WHERE app='core'")
    count = cursor.fetchone()[0]
    print(f"✓ Migraciones de core restantes: {count}")
