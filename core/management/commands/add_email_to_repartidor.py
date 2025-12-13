from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Agrega la columna email a la tabla repartidores (compatible con PostgreSQL, MySQL, SQLite)'

    def handle(self, *args, **options):
        try:
            db_engine = settings.DATABASES['default']['ENGINE']
            
            with connection.cursor() as cursor:
                # Verificar si la columna ya existe según el motor de BD
                column_exists = False
                
                if 'postgresql' in db_engine:
                    cursor.execute("""
                        SELECT column_name 
                        FROM information_schema.columns 
                        WHERE table_name = 'repartidores' 
                        AND column_name = 'email'
                    """)
                    column_exists = cursor.fetchone() is not None
                    
                elif 'mysql' in db_engine:
                    cursor.execute("""
                        SELECT COLUMN_NAME 
                        FROM INFORMATION_SCHEMA.COLUMNS 
                        WHERE TABLE_NAME = 'repartidores' 
                        AND COLUMN_NAME = 'email'
                    """)
                    column_exists = cursor.fetchone() is not None
                    
                elif 'sqlite' in db_engine:
                    cursor.execute("PRAGMA table_info(repartidores)")
                    columns = [row[1] for row in cursor.fetchall()]
                    column_exists = 'email' in columns
                
                if column_exists:
                    self.stdout.write(self.style.SUCCESS("La columna 'email' ya existe en la tabla 'repartidores'"))
                else:
                    # Agregar la columna
                    cursor.execute("""
                        ALTER TABLE repartidores 
                        ADD COLUMN email VARCHAR(100) NULL DEFAULT NULL
                    """)
                    self.stdout.write(self.style.SUCCESS("Columna 'email' agregada exitosamente a la tabla 'repartidores'"))
                    
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
