"""
Comando Django para poblar la BD con datos de prueba
Uso: python manage.py populate_data
"""
from django.core.management.base import BaseCommand
from core.models.repartidores import Repartidor
from core.models.notificaciones import NotificacionProblema
from core.models.pedidos import Pedido


class Command(BaseCommand):
    help = 'Puebla la BD con datos de prueba de repartidores y notificaciones'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Poblando BD con datos de prueba...'))
        
        # Crear repartidores
        self.create_repartidores()
        
        # Crear notificaciones
        self.create_notificaciones()
        
        self.stdout.write(self.style.SUCCESS('\n✓ Población completada'))

    def create_repartidores(self):
        """Crear repartidores de prueba"""
        repartidores_data = [
            {
                'nombreRepartidor': 'Juan Pérez',
                'telefono': '3001234567',
                'email': 'juan.perez@glamstore.com'
            },
            {
                'nombreRepartidor': 'María García',
                'telefono': '3007654321',
                'email': 'maria.garcia@glamstore.com'
            },
            {
                'nombreRepartidor': 'Carlos López',
                'telefono': '3009876543',
                'email': 'carlos.lopez@glamstore.com'
            },
            {
                'nombreRepartidor': 'Ana Martínez',
                'telefono': '3005555555',
                'email': 'ana.martinez@glamstore.com'
            },
            {
                'nombreRepartidor': 'Roberto Sánchez',
                'telefono': '3004444444',
                'email': 'roberto.sanchez@glamstore.com'
            },
        ]
        
        count = 0
        for data in repartidores_data:
            repartidor, created = Repartidor.objects.get_or_create(
                nombreRepartidor=data['nombreRepartidor'],
                defaults={
                    'telefono': data['telefono'],
                    'email': data['email'],
                }
            )
            if created:
                count += 1
                self.stdout.write(f"  ✓ Creado repartidor: {data['nombreRepartidor']}")
            else:
                self.stdout.write(f"  ℹ Repartidor ya existe: {data['nombreRepartidor']}")
        
        self.stdout.write(self.style.SUCCESS(f'\n✓ {count} repartidores creados'))

    def create_notificaciones(self):
        """Crear notificaciones de prueba"""
        # Obtener algunos pedidos para asociar notificaciones
        pedidos = Pedido.objects.all()[:3]
        
        if not pedidos:
            self.stdout.write(self.style.WARNING(
                '\n⚠ No hay pedidos en la BD. Crea algunos pedidos primero.'
            ))
            return
        
        notificaciones_data = [
            {
                'motivo': 'El cliente no estaba en casa al momento de la entrega',
                'leida': False,
            },
            {
                'motivo': 'Dirección incorrecta proporcionada por el cliente',
                'leida': True,
                'respuesta_admin': 'Se contactó al cliente para confirmar la dirección correcta',
            },
            {
                'motivo': 'Producto llegó dañado',
                'leida': False,
            },
        ]
        
        count = 0
        for i, data in enumerate(notificaciones_data):
            if i < len(pedidos):
                notificacion, created = NotificacionProblema.objects.get_or_create(
                    idPedido=pedidos[i],
                    motivo=data['motivo'],
                    defaults={
                        'leida': data.get('leida', False),
                        'respuesta_admin': data.get('respuesta_admin'),
                    }
                )
                if created:
                    count += 1
                    self.stdout.write(f"  ✓ Creada notificación para pedido #{pedidos[i].idPedido}")
                else:
                    self.stdout.write(f"  ℹ Notificación ya existe para pedido #{pedidos[i].idPedido}")
        
        self.stdout.write(self.style.SUCCESS(f'\n✓ {count} notificaciones creadas'))
