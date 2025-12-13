"""
Comando Django para restaurar la BD desde archivo SQL
Uso: python manage.py restore_db [archivo_sql]
Ejemplo: python manage.py restore_db glamstoredb.sql
Compatible con: PostgreSQL, MySQL, SQLite
"""
import os
import sys
import subprocess
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings


class Command(BaseCommand):
    help = 'Restaura la BD desde un archivo SQL (compatible con PostgreSQL, MySQL, SQLite)'

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
            # Obtener configuración de BD
            db_config = settings.DATABASES['default']
            db_engine = db_config['ENGINE']
            
            if 'postgresql' in db_engine:
                self._restore_postgresql(db_config, sql_file)
            elif 'mysql' in db_engine:
                self._restore_mysql(db_config, sql_file)
            else:
                # Para SQLite u otras BDs, usar el método con Django
                self._restore_with_django(sql_file)
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error restaurando BD: {e}'))
            sys.exit(1)

    def _restore_postgresql(self, db_config, sql_file):
        """Restaurar usando psql para PostgreSQL"""
        try:
            # Construir comando psql
            cmd = [
                'psql',
                f"-h{db_config['HOST']}",
                f"-U{db_config['USER']}",
                f"-d{db_config['NAME']}",
                f"-f{sql_file}"
            ]
            
            env = os.environ.copy()
            if db_config['PASSWORD']:
                env['PGPASSWORD'] = db_config['PASSWORD']
            
            result = subprocess.run(cmd, capture_output=True, text=True, env=env)
            
            if result.returncode != 0:
                self.stdout.write(self.style.ERROR(f'✗ Error: {result.stderr}'))
                sys.exit(1)
            
            self.stdout.write(self.style.SUCCESS('✓ BD PostgreSQL restaurada exitosamente'))
        except FileNotFoundError:
            self.stdout.write(self.style.WARNING('⚠ psql no encontrado, usando método Django'))
            self._restore_with_django(sql_file)

    def _restore_mysql(self, db_config, sql_file):
        """Restaurar usando mysql para MySQL"""
        try:
            # Ejecutar con shell=True para que funcione la redirección
            cmd = f"mysql -h{db_config['HOST']} -u{db_config['USER']} -p{db_config['PASSWORD']} {db_config['NAME']} < {sql_file}"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode != 0:
                self.stdout.write(self.style.ERROR(f'✗ Error: {result.stderr}'))
                sys.exit(1)
            
            self.stdout.write(self.style.SUCCESS('✓ BD MySQL restaurada exitosamente'))
        except FileNotFoundError:
            self.stdout.write(self.style.WARNING('⚠ mysql no encontrado, usando método Django'))
            self._restore_with_django(sql_file)

    def _restore_with_django(self, sql_file):
        """Restaurar usando Django ORM (fallback para todas las BDs)"""
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        with connection.cursor() as cursor:
            statements = sql_content.split(';')
            executed = 0
            
            for statement in statements:
                statement = statement.strip()
                if statement and not statement.startswith('--'):
                    try:
                        cursor.execute(statement)
                        executed += 1
                    except Exception as e:
                        # Algunos statements pueden fallar (especialmente si son específicos de MySQL)
                        pass
            
            connection.commit()
        
        self.stdout.write(self.style.SUCCESS(
            f'✓ BD restaurada exitosamente ({executed} statements ejecutados)'
        ))
