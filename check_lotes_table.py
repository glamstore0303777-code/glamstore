#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("PRAGMA table_info(lotes_producto)")
    columns = cursor.fetchall()
    print("Columnas en lotes_producto:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")
