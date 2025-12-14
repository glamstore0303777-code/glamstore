# Generated migration to fix missing tables and columns on Render

from django.db import migrations
from django.conf import settings


def fix_missing_tables_and_columns(apps, schema_editor):
    """Crear tablas y columnas faltantes de forma segura"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        if 'postgresql' in db_engine:
            # PostgreSQL
            
            # 1. Crear tabla distribuidores si no existe
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS distribuidores (
                        idDistribuidor SERIAL PRIMARY KEY,
                        nombreDistribuidor VARCHAR(100) NOT NULL,
                        contacto VARCHAR(100),
                        email VARCHAR(100),
                        telefono VARCHAR(20),
                        direccion VARCHAR(255)
                    );
                """)
            except Exception:
                pass
            
            # 2. Agregar columna codigo_lote a lotes_producto si no existe
            try:
                cursor.execute("""
                    ALTER TABLE lotes_producto
                    ADD COLUMN IF NOT EXISTS codigo_lote VARCHAR(100);
                """)
            except Exception:
                pass
            
            # 3. Agregar columna foto a notificacionproblema si no existe
            try:
                cursor.execute("""
                    ALTER TABLE notificacionproblema
                    ADD COLUMN IF NOT EXISTS foto VARCHAR(255);
                """)
            except Exception:
                pass
        else:
            # SQLite
            
            # 1. Verificar si tabla distribuidores existe
            try:
                cursor.execute("PRAGMA table_info(distribuidores);")
                if not cursor.fetchall():
                    cursor.execute("""
                        CREATE TABLE distribuidores (
                            idDistribuidor INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombreDistribuidor VARCHAR(100) NOT NULL,
                            contacto VARCHAR(100),
                            email VARCHAR(100),
                            telefono VARCHAR(20),
                            direccion VARCHAR(255)
                        );
                    """)
            except Exception:
                pass
            
            # 2. Agregar columna codigo_lote a lotes_producto si no existe
            try:
                cursor.execute("PRAGMA table_info(lotes_producto);")
                columns = {row[1] for row in cursor.fetchall()}
                if 'codigo_lote' not in columns:
                    cursor.execute("""
                        ALTER TABLE lotes_producto
                        ADD COLUMN codigo_lote VARCHAR(100);
                    """)
            except Exception:
                pass
            
            # 3. Agregar columna foto a notificacionproblema si no existe
            try:
                cursor.execute("PRAGMA table_info(notificacionproblema);")
                columns = {row[1] for row in cursor.fetchall()}
                if 'foto' not in columns:
                    cursor.execute("""
                        ALTER TABLE notificacionproblema
                        ADD COLUMN foto VARCHAR(255);
                    """)
            except Exception:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_final_fix_nullable'),
    ]

    operations = [
        migrations.RunPython(fix_missing_tables_and_columns, migrations.RunPython.noop),
    ]
