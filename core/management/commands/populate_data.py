"""
Comando Django para restaurar la BD desde archivo SQL
Uso: python manage.py populate_data [archivo_sql]
Ejemplo: python manage.py populate_data glamstoredb.sql
"""
import os
import sys
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings


class Command(BaseCommand):
    help = 'Restaura la BD desde un archivo SQL'

    def add_arguments(self, parser):
        parser.add_argument(
            'sql_file',
            nargs='?',
            default='glamstoredb.sql',
            type=str,
            help='Ruta del archivo SQL a restaurar (default: glamstoredb.sql)'
        )

    def handle(self, *args, **options):
        sql_file = options['sql_file']
        
        # Verificar que el archivo existe
        if not os.path.exists(sql_file):
            self.stdout.write(self.style.ERROR(f'✗ Archivo no encontrado: {sql_file}'))
            sys.exit(1)
        
        self.stdout.write(self.style.SUCCESS(f'Restaurando BD desde {sql_file}...'))
        
        try:
            with open(sql_file, 'r', encoding='utf-8') as f:
                sql_content = f.read()
            
            # Ejecutar el SQL
            with connection.cursor() as cursor:
                # Dividir por ; para ejecutar cada statement
                statements = sql_content.split(';')
                executed = 0
                
                for statement in statements:
                    statement = statement.strip()
                    if statement and not statement.startswith('--'):
                        try:
                            cursor.execute(statement)
                            executed += 1
                        except Exception as e:
                            # Algunos statements pueden fallar (ej: DROP TABLE si no existe)
                            # Continuamos con los siguientes
                            pass
                
                connection.commit()
            
            self.stdout.write(self.style.SUCCESS(
                f'✓ BD restaurada exitosamente ({executed} statements ejecutados)'
            ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error restaurando BD: {e}'))
            sys.exit(1)
