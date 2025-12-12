#!/usr/bin/env python
"""
Script para restaurar BD desde SQL ejecutando directamente en PostgreSQL
Ejecuta: python restore_from_sql.py glamstoredb.sql
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.conf import settings
import psycopg2


def restore_sql_file(sql_file):
    """Restaurar BD desde archivo SQL"""
    
    if not os.path.exists(sql_file):
        print(f"✗ Archivo no encontrado: {sql_file}")
        sys.exit(1)
    
    print(f"Leyendo {sql_file}...")
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    db_config = settings.DATABASES['default']
    
    print(f"\nConectando a PostgreSQL...")
    print(f"Host: {db_config['HOST']}")
    print(f"BD: {db_config['NAME']}\n")
    
    try:
        conn = psycopg2.connect(
            host=db_config['HOST'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            database=db_config['NAME'],
            port=db_config['PORT']
        )
        
        cursor = conn.cursor()
        
        # Ejecutar el SQL completo
        print("Ejecutando SQL...")
        try:
            cursor.execute(sql_content)
            conn.commit()
            print("✓ SQL ejecutado exitosamente")
        except Exception as e:
            print(f"⚠ Error ejecutando SQL: {str(e)[:200]}")
            conn.rollback()
        
        cursor.close()
        conn.close()
        
        # Verificar datos
        print(f"\nVerificando datos...")
        conn = psycopg2.connect(
            host=db_config['HOST'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            database=db_config['NAME'],
            port=db_config['PORT']
        )
        
        cursor = conn.cursor()
        
        # Contar datos importantes
        tables_to_check = [
            ('repartidores', 'Repartidores'),
            ('notificaciones_problema', 'Notificaciones'),
            ('roles', 'Roles'),
            ('usuarios', 'Usuarios'),
            ('pedidos', 'Pedidos'),
            ('productos', 'Productos'),
            ('clientes', 'Clientes'),
        ]
        
        for table, label in tables_to_check:
            try:
                cursor.execute(f'SELECT COUNT(*) FROM "{table}";')
                count = cursor.fetchone()[0]
                if count > 0:
                    print(f"  ✓ {label}: {count}")
                else:
                    print(f"  - {label}: 0")
            except:
                pass
        
        cursor.close()
        conn.close()
        
        print(f"\n✓ Proceso completado")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)


def main():
    print("=" * 60)
    print("RESTAURAR BD DESDE SQL")
    print("=" * 60 + "\n")
    
    sql_file = sys.argv[1] if len(sys.argv) > 1 else 'glamstoredb.sql'
    
    restore_sql_file(sql_file)


if __name__ == '__main__':
    main()
