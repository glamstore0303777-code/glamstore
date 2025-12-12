#!/usr/bin/env python
"""
Script para insertar repartidores y notificaciones directamente en Render
Ejecuta: python insert_repartidores_notificaciones.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models.repartidores import Repartidor
from core.models.notificaciones import NotificacionProblema
from core.models.pedidos import Pedido


def insert_repartidores():
    """Insertar repartidores desde el SQL"""
    repartidores_data = [
        {
            'idRepartidor': 15,
            'nombreRepartidor': 'lauren',
            'telefono': '3024892804',
            'email': 'laurensamanta0.r@gmail.com',
        },
        {
            'idRepartidor': 16,
            'nombreRepartidor': 'michael ',
            'telefono': '3024892804',
            'email': 'michaeldaramirez117@gmail.com',
        },
        {
            'idRepartidor': 17,
            'nombreRepartidor': 'carlos',
            'telefono': '3024892804',
            'email': 'carlos@glamstore.com',
        },
    ]
    
    print("Insertando repartidores...")
    created = 0
    
    for data in repartidores_data:
        try:
            repartidor, was_created = Repartidor.objects.get_or_create(
                idRepartidor=data['idRepartidor'],
                defaults={
                    'nombreRepartidor': data['nombreRepartidor'],
                    'telefono': data['telefono'],
                    'email': data['email'],
                }
            )
            if was_created:
                created += 1
                print(f"  ✓ Creado: {data['nombreRepartidor']}")
            else:
                print(f"  ℹ Ya existe: {data['nombreRepartidor']}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print(f"✓ {created} repartidores creados\n")
    return created


def insert_notificaciones():
    """Insertar notificaciones de prueba"""
    print("Insertando notificaciones...")
    
    # Obtener algunos pedidos
    pedidos = Pedido.objects.all()[:3]
    
    if not pedidos:
        print("  ⚠ No hay pedidos en la BD. Saltando notificaciones.\n")
        return 0
    
    notificaciones_data = [
        {
            'motivo': 'El cliente no estaba en casa al momento de la entrega',
            'leida': False,
        },
        {
            'motivo': 'Dirección incorrecta proporcionada por el cliente',
            'leida': True,
            'respuesta_admin': 'Se contactó al cliente para confirmar la dirección correcta',
        },
        {
            'motivo': 'Producto llegó dañado',
            'leida': False,
        },
    ]
    
    created = 0
    
    for i, data in enumerate(notificaciones_data):
        if i < len(pedidos):
            try:
                notificacion, was_created = NotificacionProblema.objects.get_or_create(
                    idPedido=pedidos[i],
                    motivo=data['motivo'],
                    defaults={
                        'leida': data.get('leida', False),
                        'respuesta_admin': data.get('respuesta_admin'),
                    }
                )
                if was_created:
                    created += 1
                    print(f"  ✓ Creada notificación para pedido #{pedidos[i].idPedido}")
                else:
                    print(f"  ℹ Ya existe notificación para pedido #{pedidos[i].idPedido}")
            except Exception as e:
                print(f"  ✗ Error: {e}")
    
    print(f"✓ {created} notificaciones creadas\n")
    return created


def verify_data():
    """Verificar que los datos se insertaron"""
    print("Verificando datos...")
    
    repartidores_count = Repartidor.objects.count()
    notificaciones_count = NotificacionProblema.objects.count()
    
    print(f"  - Repartidores: {repartidores_count}")
    print(f"  - Notificaciones: {notificaciones_count}")
    
    if repartidores_count > 0:
        print(f"\n  Repartidores:")
        for r in Repartidor.objects.all()[:5]:
            print(f"    - {r.nombreRepartidor} ({r.telefono})")
    
    return repartidores_count, notificaciones_count


def main():
    print("=" * 60)
    print("INSERTAR REPARTIDORES Y NOTIFICACIONES")
    print("=" * 60 + "\n")
    
    try:
        # Insertar repartidores
        repartidores_created = insert_repartidores()
        
        # Insertar notificaciones
        notificaciones_created = insert_notificaciones()
        
        # Verificar
        repartidores_count, notificaciones_count = verify_data()
        
        print("\n" + "=" * 60)
        if repartidores_count > 0:
            print("✓ ÉXITO: Datos insertados correctamente")
        else:
            print("⚠ ADVERTENCIA: No se insertaron datos")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
