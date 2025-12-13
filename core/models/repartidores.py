from django.db import models, connection
from django.conf import settings

class Repartidor(models.Model):
    idRepartidor = models.AutoField(primary_key=True, db_column='idrepartidor')
    nombreRepartidor = models.CharField(max_length=50, null=True, db_column='nombre')
    telefono = models.CharField(max_length=20, null=True, db_column='telefono')
    email = models.EmailField(max_length=100, null=True, blank=True, db_column='email')

    class Meta:
        db_table = 'repartidores'   
        managed = False             
        app_label = 'core'
    
    def __str__(self):
        return self.nombreRepartidor or f"Repartidor {self.idRepartidor}"
    
    @classmethod
    def ensure_email_column_exists(cls):
        """Asegura que la columna email existe en la tabla (compatible con PostgreSQL, MySQL, SQLite)"""
        try:
            db_engine = settings.DATABASES['default']['ENGINE']
            
            with connection.cursor() as cursor:
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
                
                if not column_exists:
                    cursor.execute("""
                        ALTER TABLE repartidores 
                        ADD COLUMN email VARCHAR(100) NULL DEFAULT NULL
                    """)
        except Exception:
            pass 
    
    @classmethod
    def ensure_telefono_column_size(cls):
        """Asegura que la columna telefono tiene el tamaño correcto (compatible con PostgreSQL, MySQL, SQLite)"""
        try:
            db_engine = settings.DATABASES['default']['ENGINE']
            
            with connection.cursor() as cursor:
                if 'postgresql' in db_engine:
                    cursor.execute("""
                        SELECT data_type 
                        FROM information_schema.columns 
                        WHERE table_name = 'repartidores' 
                        AND column_name = 'telefono'
                    """)
                    result = cursor.fetchone()
                    if result and result[0] != 'character varying':
                        cursor.execute("""
                            ALTER TABLE repartidores 
                            ALTER COLUMN telefono TYPE VARCHAR(20)
                        """)
                        
                elif 'mysql' in db_engine:
                    cursor.execute("""
                        SELECT COLUMN_TYPE 
                        FROM INFORMATION_SCHEMA.COLUMNS 
                        WHERE TABLE_NAME = 'repartidores' 
                        AND COLUMN_NAME = 'telefono'
                    """)
                    result = cursor.fetchone()
                    if result and 'varchar(11)' in result[0].lower():
                        cursor.execute("""
                            ALTER TABLE repartidores 
                            MODIFY COLUMN telefono VARCHAR(20) NULL
                        """)
        except Exception:
            pass     

        