from django.core.management.base import BaseCommand
from core.services.correos_service import enviar_correos_pendientes


class Command(BaseCommand):
    help = 'Envía los correos pendientes de la cola'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando envío de correos pendientes...'))
        enviar_correos_pendientes()
        self.stdout.write(self.style.SUCCESS('Envío de correos completado'))
