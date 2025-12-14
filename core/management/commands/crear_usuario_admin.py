from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from core.models import Usuario, Rol
from django.utils import timezone

class Command(BaseCommand):
    help = 'Crea un usuario administrador de prueba'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, default='admin@glamstore.com', help='Email del admin')
        parser.add_argument('--password', type=str, default='admin123', help='Contraseña del admin')
        parser.add_argument('--nombre', type=str, default='Administrador', help='Nombre del admin')

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']
        nombre = options['nombre']

        # Verificar si el usuario ya existe
        if Usuario.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'El usuario {email} ya existe'))
            return

        # Crear el usuario
        usuario = Usuario.objects.create(
            email=email,
            password=make_password(password),
            nombre=nombre,
            id_rol=1,  # 1 = Administrador
            fechacreacion=timezone.now(),
            ultimoacceso=timezone.now()
        )

        self.stdout.write(self.style.SUCCESS(f'Usuario {email} creado exitosamente'))
        self.stdout.write(f'Email: {email}')
        self.stdout.write(f'Contraseña: {password}')
