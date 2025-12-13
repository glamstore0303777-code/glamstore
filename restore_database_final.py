#!/usr/bin/env python
"""
Script para restaurar la BD desde SQL en Render
Uso: python restore_database_final.py glamstoredb_postgres.sql
"""
import os
import sys
import psycopg2
from psycopg2 import sql
from django.conf import settings
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()


def parse_sql_statements(sql_content):
    """Parsear solo INSERT statements del SQL"""
    statements = []
    current_statement = []
    in_string = False
    string_char = None
    
    lines = sql_content.split('\n')
    
    for line in lines:
        # Ignorar comentarios
        if line.strip().startswith('--'):
            continue
        
        # Solo procesar líneas que empiezan con INSERT
        if line.strip().upper().startswith('INSERT'):
            current_statement = [line]
            
            # Si la línea termina con ;, es un statement completo
            if line.strip().endswith(';'):
                statement = ''.join(current_statement).strip()
                if statement:
                    statements.append(statement)
                current_statement = []
            else:
                # Continuar leyendo hasta encontrar ;
                continue
        elif current_statement:
            # Continuamos con el statement anterior
            current_statement.append(line)
            
            if line.strip().endswith(';'):
                statement = ''.join(current_statement).strip()
                if statement:
                    statements.append(statement)
                current_statement = []
    
    return statements


def restore_database(sql_file):
    """Restaurar la BD desde archivo SQL"""
    
    if not os.path.exists(sql_file):
        print(f"✗ Archivo no encontrado: {sql_file}")
        sys.exit(1)
    
    print(f"Leyendo {sql_file}...")
    
    try:
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
    except Exception as e:
        print(f"✗ Error leyendo archivo: {e}")
        sys.exit(1)
    
    print("Parseando SQL...")
    statements = parse_sql_statements(sql_content)
    print(f"✓ {len(statements)} statements encontrados")
    
    # Conectar a PostgreSQL
    db_config = settings.DATABASES['default']
    
    print(f"\nConectando a PostgreSQL...")
    print(f"Host: {db_config['HOST']}")
    print(f"BD: {db_config['NAME']}")
    
    try:
        conn = psycopg2.connect(
            host=db_config['HOST'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            database=db_config['NAME'],
            port=db_config['PORT']
        )
        
        print(f"\nEjecutando {len(statements)} statements...")
        executed = 0
        failed = 0
        
        for i, statement in enumerate(statements, 1):
            if not statement.strip():
                continue
            
            cursor = conn.cursor()
            
            try:
                cursor.execute(statement)
                conn.commit()
                executed += 1
                
                # Mostrar progreso cada 10 statements
                if i % 10 == 0:
                    print(f"  {i}/{len(statements)} completados...")
                    
            except psycopg2.Error as e:
                conn.rollback()
                failed += 1
                error_msg = str(e).split('\n')[0]
                
                # Solo mostrar errores importantes
                if 'duplicate key' not in error_msg.lower() and 'does not exist' not in error_msg and 'already exists' not in error_msg:
                    print(f"  ⚠ Statement {i}: {error_msg[:80]}")
            finally:
                cursor.close()
        
        conn.close()
        
        print(f"\n✓ Restauración completada")
        print(f"  - Ejecutados: {executed}")
        print(f"  - Fallidos: {failed}")
        
        # Verificar datos
        print(f"\nVerificando datos...")
        verify_data()
        
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)


def verify_data():
    """Verificar que los datos se restauraron correctamente"""
    try:
        from core.models import Repartidor, NotificacionProblema
        
        repartidores = Repartidor.objects.count()
        notificaciones = NotificacionProblema.objects.count()
        
        print(f"  - Repartidores: {repartidores}")
        print(f"  - Notificaciones: {notificaciones}")
        
        if repartidores > 0 or notificaciones > 0:
            print(f"\n✓ Datos restaurados exitosamente")
        else:
            print(f"\n⚠ No se encontraron datos. Verifica el archivo SQL.")
            
    except Exception as e:
        print(f"  ⚠ Error verificando datos: {e}")


if __name__ == '__main__':
    sql_file = sys.argv[1] if len(sys.argv) > 1 else 'glamstoredb_postgres.sql'
    restore_database(sql_file)
