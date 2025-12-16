#!/usr/bin/env python
"""
Script para diagnosticar el problema con movimientos_lote.lote_id
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection

def diagnosticar():
    with connection.cursor() as cursor:
        print("=" * 80)
        print("DIAGNÓSTICO: movimientos_lote")
        print("=" * 80)
        
        # 1. Verificar si la tabla existe
        print("\n1. Verificando si la tabla movimientos_lote existe...")
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables 
                WHERE table_name = 'movimientos_lote'
            );
        """)
        existe = cursor.fetchone()[0]
        print(f"   ✓ Tabla existe: {existe}")
        
        if not existe:
            print("   ✗ La tabla no existe. Abortando diagnóstico.")
            return
        
        # 2. Listar todas las columnas
        print("\n2. Columnas en la tabla movimientos_lote:")
        cursor.execute("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'movimientos_lote'
            ORDER BY ordinal_position;
        """)
        columnas = cursor.fetchall()
        for col_name, data_type, is_nullable in columnas:
            nullable = "NULL" if is_nullable == "YES" else "NOT NULL"
            print(f"   - {col_name}: {data_type} ({nullable})")
        
        # 3. Verificar si lote_id existe
        print("\n3. Verificando columna lote_id:")
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.columns 
                WHERE table_name = 'movimientos_lote' AND column_name = 'lote_id'
            );
        """)
        lote_id_existe = cursor.fetchone()[0]
        print(f"   ✓ Columna lote_id existe: {lote_id_existe}")
        
        # 4. Verificar constraints
        print("\n4. Constraints en movimientos_lote:")
        cursor.execute("""
            SELECT constraint_name, constraint_type
            FROM information_schema.table_constraints
            WHERE table_name = 'movimientos_lote';
        """)
        constraints = cursor.fetchall()
        if constraints:
            for constraint_name, constraint_type in constraints:
                print(f"   - {constraint_name}: {constraint_type}")
        else:
            print("   (Sin constraints)")
        
        # 5. Contar registros
        print("\n5. Registros en movimientos_lote:")
        cursor.execute("SELECT COUNT(*) FROM movimientos_lote;")
        count = cursor.fetchone()[0]
        print(f"   Total: {count} registros")
        
        # 6. Verificar si hay datos con lote_id NULL
        if lote_id_existe:
            print("\n6. Registros con lote_id NULL:")
            cursor.execute("SELECT COUNT(*) FROM movimientos_lote WHERE lote_id IS NULL;")
            null_count = cursor.fetchone()[0]
            print(f"   Total: {null_count} registros")
        
        print("\n" + "=" * 80)
        print("FIN DEL DIAGNÓSTICO")
        print("=" * 80)

if __name__ == '__main__':
    diagnosticar()
