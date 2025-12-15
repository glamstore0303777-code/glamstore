import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("PRAGMA table_info(notificaciones_problema)")
    columns = cursor.fetchall()
    print("Columnas en notificaciones_problema:")
    for col in columns:
        print(f"  {col[1]}: {col[2]}")
