# core/Clientes/services.py
from django.db import connection
from django.contrib.auth.hashers import check_password

def autenticar_usuario(email, password):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT idUsuario, password, nombre, id_rol FROM usuarios
            WHERE email = %s
        """, [email])
        usuario = cursor.fetchone()

    if usuario and check_password(password, usuario[1]):
        return {
            'id': usuario[0],
            'nombre': usuario[2],
            'rol': usuario[3]
        }
    return None