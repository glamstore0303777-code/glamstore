from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Agrega la columna margen_ganancia a la tabla productos (compatible con PostgreSQL, MySQL, SQLite)'

    def handle(self, *args, **options):
        db_engine = settings.DATABASES['default']['ENGINE']
        
        with connection.cursor() as cursor:
            try:
                # Verificar si la columna ya existe
                column_exists = False
                
                if 'postgresql' in db_engine:
                    cursor.execute("""
                        SELECT column_name 
                        FROM information_schema.columns 
                        WHERE table_name = 'productos' 
                        AND column_name = 'margen_ganancia'
                    """)
                    column_exists = cursor.fetchone() is not None
                    
                elif 'mysql' in db_engine:
                    cursor.execute("""
                        SELECT COLUMN_NAME 
                        FROM INFORMATION_SCHEMA.COLUMNS 
                        WHERE TABLE_NAME = 'productos' 
                        AND COLUMN_NAME = 'margen_ganancia'
                    """)
                    column_exists = cursor.fetchone() is not None
                    
                elif 'sqlite' in db_engine:
                    cursor.execute("PRAGMA table_info(productos)")
                    columns = [row[1] for row in cursor.fetchall()]
                    column_exists = 'margen_ganancia' in columns
                
                if column_exists:
                    self.stdout.write(self.style.WARNING('La columna margen_ganancia ya existe'))
                else:
                    cursor.execute('''
                        ALTER TABLE productos 
                        ADD COLUMN margen_ganancia DECIMAL(5, 2) DEFAULT 10
                    ''')
                    self.stdout.write(self.style.SUCCESS('Columna margen_ganancia agregada exitosamente'))
                    
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
