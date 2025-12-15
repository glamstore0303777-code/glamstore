"""
Comando para enviar planes semanales a repartidores
Uso: python manage.py enviar_planes_repartidores
"""

from django.core.management.base import BaseCommand
from core.Gestion_admin.enviar_planes_repartidores import enviar_planes_semanales_todos_repartidores


class Command(BaseCommand):
    help = 'Envía planes semanales de entregas a todos los repartidores'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando envío de planes semanales...'))
        
        resultado = enviar_planes_semanales_todos_repartidores()
        
        self.stdout.write(f"\nResultado:")
        self.stdout.write(f"Total de repartidores: {resultado['total_repartidores']}")
        self.stdout.write(self.style.SUCCESS(f"Correos enviados: {resultado['correos_enviados']}"))
        self.stdout.write(self.style.ERROR(f"Correos fallidos: {resultado['correos_fallidos']}"))
        
        if resultado['detalles']:
            self.stdout.write("\nDetalles:")
            for detalle in resultado['detalles']:
                if '✓' in detalle:
                    self.stdout.write(self.style.SUCCESS(detalle))
                else:
                    self.stdout.write(self.style.ERROR(detalle))
        
        self.stdout.write(self.style.SUCCESS('\nProceso completado'))
