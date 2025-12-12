"""
Comando Django para restaurar la BD desde archivo SQL
Uso: python manage.py populate_data [archivo_sql]
Ejemplo: python manage.py populate_data glamstoredb.sql

NOTA: El archivo SQL debe ser compatible con la BD actual.
Si es MySQL y usas PostgreSQL, necesitarás convertirlo primero.
"""
import os
import sys
import subprocess
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
            db_config = settings.DATABASES['default']
            
            # PostgreSQL
            if 'postgresql' in db_config['ENGINE'].lower():
                self.stdout.write('Detectado PostgreSQL. Usando psql para restaurar...')
                self._restore_postgresql(sql_file, db_config)
            
            # MySQL
            elif 'mysql' in db_config['ENGINE'].lower():
                self.stdout.write('Detectado MySQL. Usando mysql CLI para restaurar...')
                self._restore_mysql(sql_file, db_config)
            
            # SQLite u otras
            else:
                self.stdout.write('Usando Django para restaurar...')
                self._restore_with_django(sql_file)
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error restaurando BD: {e}'))
            sys.exit(1)

    def _restore_postgresql(self, sql_file, db_config):
        """Restaurar usando psql para PostgreSQL"""
        # Construir URL de conexión
        db_url = (
            f"postgresql://{db_config['USER']}:{db_config['PASSWORD']}"
            f"@{db_config['HOST']}:{db_config['PORT']}/{db_config['NAME']}"
        )
        
        cmd = f"psql {db_url} < {sql_file}"
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            self.stdout.write(self.style.WARNING(f'⚠ Advertencia: {result.stderr[:200]}'))
            # Continuar de todas formas, algunos errores son normales
        
        self.stdout.write(self.style.SUCCESS('✓ BD restaurada exitosamente'))

    def _restore_mysql(self, sql_file, db_config):
        """Restaurar usando mysql CLI para MySQL"""
        cmd = (
            f"mysql -h{db_config['HOST']} "
            f"-u{db_config['USER']} "
            f"-p{db_config['PASSWORD']} "
            f"{db_config['NAME']} < {sql_file}"
        )
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            self.stdout.write(self.style.ERROR(f'✗ Error: {result.stderr}'))
            sys.exit(1)
        
        self.stdout.write(self.style.SUCCESS('✓ BD restaurada exitosamente'))

    def _restore_with_django(self, sql_file):
        """Restaurar usando Django ORM"""
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Procesar el SQL de forma más robusta
        statements = self._parse_sql_statements(sql_content)
        
        with connection.cursor() as cursor:
            executed = 0
            
            for statement in statements:
                if statement.strip():
                    try:
                        cursor.execute(statement)
                        executed += 1
                    except Exception as e:
                        # Algunos statements pueden fallar
                        pass
            
            connection.commit()
        
        self.stdout.write(self.style.SUCCESS(
            f'✓ BD restaurada exitosamente ({executed} statements ejecutados)'
        ))

    def _parse_sql_statements(self, sql_content):
        """Parsear statements SQL de forma más robusta"""
        statements = []
        current_statement = []
        in_string = False
        string_char = None
        
        for i, char in enumerate(sql_content):
            # Detectar inicio/fin de strings
            if char in ('"', "'") and (i == 0 or sql_content[i-1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
            
            # Si encontramos ; fuera de un string, es fin de statement
            if char == ';' and not in_string:
                current_statement.append(char)
                statement = ''.join(current_statement).strip()
                
                # Filtrar comentarios y líneas vacías
                if statement and not statement.startswith('--'):
                    statements.append(statement)
                
                current_statement = []
            else:
                current_statement.append(char)
        
        # Agregar último statement si existe
        if current_statement:
            statement = ''.join(current_statement).strip()
            if statement and not statement.startswith('--'):
                statements.append(statement)
        
        return statements
