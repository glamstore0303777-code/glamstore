# Generated migration to populate initial data from glamstoredb

from django.db import migrations
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta


def populate_data(apps, schema_editor):
    """Populate initial data - tables already exist in MySQL glamstoredb"""
    
    with schema_editor.connection.cursor() as cursor:
        # Insert admin user if doesn't exist
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = %s", ['admin@glamstore.com'])
        if cursor.fetchone()[0] == 0:
            hashed_password = make_password('admin123')
            cursor.execute("""
                INSERT INTO usuarios (email, password, id_rol, nombre, fechacreacion)
                VALUES (%s, %s, %s, %s, %s)
            """, ['admin@glamstore.com', hashed_password, 1, 'Administrador', datetime.now()])


def reverse_populate(apps, schema_editor):
    """Reverse the population"""
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE email = %s", ['admin@glamstore.com'])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_merge_20251213_1701'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_populate),
    ]
