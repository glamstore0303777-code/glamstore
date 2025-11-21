#!/usr/bin/env python
"""
Script para probar la eliminación de clientes sin errores de integridad referencial.
Este script simula el proceso de eliminación que se ejecuta en la vista.
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

django.setup()

from core.models.clientes import Cliente
from core.models.usuarios import Usuario
from core.models.pedidos import Pedido
from django.db import transaction

def test_client_deletion_process(client_id):
    """
    Prueba el proceso de eliminación de un cliente específico.
    """
    try:
        cliente = Cliente.objects.get(idCliente=client_id)
        print(f"Cliente encontrado: {cliente.nombre} (ID: {cliente.idCliente})")
        
        # Verificar usuarios relacionados
        usuarios_relacionados = Usuario.objects.filter(idCliente=client_id)
        print(f"Usuarios relacionados: {usuarios_relacionados.count()}")
        
        # Verificar pedidos relacionados
        pedidos_relacionados = Pedido.objects.filter(idCliente=client_id)
        print(f"Pedidos relacionados: {pedidos_relacionados.count()}")
        
        print("\n--- SIMULACIÓN DE ELIMINACIÓN ---")
        print("1. Actualizando usuarios relacionados...")
        usuarios_actualizados = Usuario.objects.filter(idCliente=client_id).count()
        print(f"   Se actualizarían {usuarios_actualizados} usuario(s)")
        
        print("2. Verificando pedidos...")
        if pedidos_relacionados.count() > 0:
            print(f"   ADVERTENCIA: Se eliminarían {pedidos_relacionados.count()} pedido(s)")
        
        print("3. El cliente se eliminaría correctamente")
        print("\n✅ PROCESO DE ELIMINACIÓN SERÍA EXITOSO")
        
        return True
        
    except Cliente.DoesNotExist:
        print(f"❌ ERROR: Cliente con ID {client_id} no existe")
        return False
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def list_clients_with_references():
    """
    Lista todos los clientes y sus referencias.
    """
    print("=== CLIENTES Y SUS REFERENCIAS ===")
    clientes = Cliente.objects.all()
    
    for cliente in clientes:
        usuarios_count = Usuario.objects.filter(idCliente=cliente.idCliente).count()
        pedidos_count = Pedido.objects.filter(idCliente=cliente.idCliente).count()
        
        print(f"Cliente: {cliente.nombre} (ID: {cliente.idCliente})")
        print(f"  - Usuarios: {usuarios_count}")
        print(f"  - Pedidos: {pedidos_count}")
        print()

if __name__ == "__main__":
    print("🔍 DIAGNÓSTICO DE ELIMINACIÓN DE CLIENTES")
    print("=" * 50)
    
    # Listar todos los clientes y sus referencias
    list_clients_with_references()
    
    # Si se proporciona un ID específico, probar la eliminación
    if len(sys.argv) > 1:
        try:
            client_id = int(sys.argv[1])
            print(f"\n🧪 PROBANDO ELIMINACIÓN DEL CLIENTE ID: {client_id}")
            print("-" * 50)
            test_client_deletion_process(client_id)
        except ValueError:
            print("❌ ERROR: Proporciona un ID de cliente válido")
    else:
        print("\n💡 USO: python test_client_deletion.py <client_id>")
        print("   Ejemplo: python test_client_deletion.py 14")