#!/usr/bin/env python
"""
Script para aumentar el tamaño del campo email en PostgreSQL
"""
import os
import psycopg2

DB_HOST = os.getenv('DATABASE_HOST', 'dpg-d4t0vo2li9vc7394ahjg-a.virginia-postgres.render.com')
DB_NAME = os.getenv('DATABASE_NAME', 'glamstoredb')
DB_USER = os.getenv('DATABASE_USER', 'glamstoredb_user')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD', '')
DB_PORT = os.getenv('DATABASE_PORT', '5432')

try:
    print("Conectando a PostgreSQL...")
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER,
        password=DB_PASSWORD, port=DB_PORT
    )
    cursor = conn.cursor()
    
    print("Aumentando tamaño del campo email en tabla usuarios...")
    cursor.execute("""
        ALTER TABLE usuarios
        ALTER COLUMN email TYPE character varying(255);
    """)
    
    conn.commit()
    print("✓ Campo email actualizado a 255 caracteres")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"✗ Error: {str(e)}")
