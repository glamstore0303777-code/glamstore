#!/usr/bin/env python
"""
Script para diagnosticar el problema con la cédula de clientes
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from django.db import connection
from core.models.clientes import Cliente

def diagnosticar():
    print("=" * 80)
    print("DIAGNÓSTICO: Cédula de Clientes")
    print("=" * 80)
    
    # 1. Verificar si la columna cedula existe
    print("\n1. Verificando si la columna 'cedula' existe en la tabla 'clientes'...")
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.columns 
                WHERE table_name = 'clientes' AND column_name = 'cedula'
            );
        """)
        existe = cursor.fetchone()[0]
        print(f"   ✓ Columna 'cedula' existe: {existe}")
        
        if existe:
            # Obtener información de la columna
            cursor.execute("""
                SELECT data_type, is_nullable
                FROM information_schema.columns
                WHERE table_name = 'clientes' AND column_name = 'cedula';
            """)
            data_type, is_nullable = cursor.fetchone()
            print(f"   - Tipo de dato: {data_type}")
            print(f"   - Nullable: {is_nullable}")
    
    # 2. Contar clientes con cédula NULL
    print("\n2. Contando clientes con cédula NULL...")
    clientes_null = Cliente.objects.filter(cedula__isnull=True).count()
    clientes_vacio = Cliente.objects.filter(cedula='').count()
    clientes_con_cedula = Cliente.objects.exclude(cedula__isnull=True).exclude(cedula='').count()
    
    print(f"   - Clientes con cédula NULL: {clientes_null}")
    print(f"   - Clientes con cédula vacía: {clientes_vacio}")
    print(f"   - Clientes con cédula: {clientes_con_cedula}")
    print(f"   - Total de clientes: {Cliente.objects.count()}")
    
    # 3. Mostrar algunos ejemplos
    print("\n3. Ejemplos de clientes:")
    clientes = Cliente.objects.all()[:5]
    for cliente in clientes:
        print(f"   - ID: {cliente.idCliente}, Nombre: {cliente.nombre}, Cédula: {cliente.cedula}")
    
    # 4. Verificar si hay datos en la BD directamente
    print("\n4. Consultando directamente en la BD...")
    with connection.cursor() as cursor:
        cursor.execute("SELECT idcliente, nombrecliente, cedula FROM clientes LIMIT 5;")
        rows = cursor.fetchall()
        for row in rows:
            print(f"   - ID: {row[0]}, Nombre: {row[1]}, Cédula: {row[2]}")
    
    print("\n" + "=" * 80)
    print("FIN DEL DIAGNÓSTICO")
    print("=" * 80)

if __name__ == '__main__':
    diagnosticar()
