"""
Comando para diagnosticar el estado de la base de datos
"""

from django.core.management.base import BaseCommand
from django.db import connection
from core.models import Distribuidor, NotificacionProblema, CorreoPendiente, Pedido


class Command(BaseCommand):
    help = 'Diagnostica el estado de la base de datos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('🔍 DIAGNÓSTICO DE BASE DE DATOS'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write('')

        # 1. Verificar tabla distribuidores
        self.stdout.write('1️⃣  Verificando tabla distribuidores...')
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables 
                        WHERE table_name = 'distribuidores'
                    );
                """)
                existe = cursor.fetchone()[0]
            
            if existe:
                count = Distribuidor.objects.count()
                self.stdout.write(self.style.SUCCESS(f'   ✅ Tabla existe'))
                self.stdout.write(f'   📊 Total de registros: {count}')
            else:
                self.stdout.write(self.style.ERROR(f'   ❌ Tabla NO existe'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ❌ Error: {e}'))

        self.stdout.write('')

        # 2. Verificar tabla notificaciones
        self.stdout.write('2️⃣  Verificando tabla notificaciones_problema...')
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables 
                        WHERE table_name = 'notificaciones_problema'
                    );
                """)
                existe = cursor.fetchone()[0]
            
            if existe:
                count = NotificacionProblema.objects.count()
                no_leidas = NotificacionProblema.objects.filter(leida=False).count()
                self.stdout.write(self.style.SUCCESS(f'   ✅ Tabla existe'))
                self.stdout.write(f'   📊 Total de notificaciones: {count}')
                self.stdout.write(f'   🔔 No leídas: {no_leidas}')
            else:
                self.stdout.write(self.style.ERROR(f'   ❌ Tabla NO existe'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ❌ Error: {e}'))

        self.stdout.write('')

        # 3. Verificar tabla correos_pendientes
        self.stdout.write('3️⃣  Verificando tabla correos_pendientes...')
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables 
                        WHERE table_name = 'correos_pendientes'
                    );
                """)
                existe = cursor.fetchone()[0]
            
            if existe:
                count = CorreoPendiente.objects.count()
                pendientes = CorreoPendiente.objects.filter(enviado=False).count()
                self.stdout.write(self.style.SUCCESS(f'   ✅ Tabla existe'))
                self.stdout.write(f'   📊 Total de registros: {count}')
                self.stdout.write(f'   ⏳ Pendientes de envío: {pendientes}')
            else:
                self.stdout.write(self.style.ERROR(f'   ❌ Tabla NO existe'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ❌ Error: {e}'))

        self.stdout.write('')

        # 4. Verificar pedidos sin asignar
        self.stdout.write('4️⃣  Verificando pedidos sin asignar...')
        try:
            sin_asignar = Pedido.objects.filter(idRepartidor__isnull=True).exclude(
                estado_pedido__in=['Entregado', 'Completado', 'Cancelado']
            ).count()
            self.stdout.write(f'   📦 Pedidos sin repartidor: {sin_asignar}')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ❌ Error: {e}'))

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('✅ Diagnóstico completado'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
