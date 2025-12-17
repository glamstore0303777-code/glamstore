#!/usr/bin/env python
"""
Script para diagnosticar la trazabilidad y recepción de pedidos
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models.pedidos import Pedido
from core.models.confirmacion_entrega import ConfirmacionEntrega
from django.db import connection

def diagnosticar():
    print("=" * 80)
    print("DIAGNÓSTICO: Trazabilidad y Recepción de Pedidos")
    print("=" * 80)
    
    # 1. Verificar tabla confirmaciones_entrega
    print("\n1. Verificando tabla 'confirmaciones_entrega'...")
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables 
                WHERE table_name = 'confirmaciones_entrega'
            );
        """)
        existe = cursor.fetchone()[0]
        print(f"   ✓ Tabla existe: {existe}")
        
        if existe:
            cursor.execute("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = 'confirmaciones_entrega'
                ORDER BY ordinal_position;
            """)
            columnas = cursor.fetchall()
            print(f"   - Columnas ({len(columnas)}):")
            for col_name, data_type in columnas:
                print(f"     • {col_name}: {data_type}")
    
    # 2. Estadísticas de pedidos
    print("\n2. Estadísticas de Pedidos:")
    total_pedidos = Pedido.objects.count()
    pedidos_entregados = Pedido.objects.filter(estado_pedido='Completado').count()
    pedidos_en_camino = Pedido.objects.filter(estado_pedido='En Camino').count()
    pedidos_confirmados = Pedido.objects.filter(estado_pedido='Confirmado').count()
    pedidos_sin_repartidor = Pedido.objects.filter(idRepartidor__isnull=True).count()
    
    print(f"   - Total de pedidos: {total_pedidos}")
    print(f"   - Pedidos completados: {pedidos_entregados}")
    print(f"   - Pedidos en camino: {pedidos_en_camino}")
    print(f"   - Pedidos confirmados: {pedidos_confirmados}")
    print(f"   - Pedidos sin repartidor: {pedidos_sin_repartidor}")
    
    # 3. Confirmaciones de entrega
    print("\n3. Confirmaciones de Entrega:")
    total_confirmaciones = ConfirmacionEntrega.objects.count()
    confirmaciones_con_foto = ConfirmacionEntrega.objects.exclude(foto_entrega='').count()
    calificacion_promedio = ConfirmacionEntrega.objects.values('calificacion').count()
    
    print(f"   - Total de confirmaciones: {total_confirmaciones}")
    print(f"   - Confirmaciones con foto: {confirmaciones_con_foto}")
    print(f"   - Tasa de confirmación: {(total_confirmaciones / total_pedidos * 100):.1f}%" if total_pedidos > 0 else "   - Tasa de confirmación: N/A")
    
    # 4. Calificaciones promedio
    print("\n4. Calificaciones de Entregas:")
    from django.db.models import Avg
    calificacion_promedio = ConfirmacionEntrega.objects.aggregate(Avg('calificacion'))['calificacion__avg']
    print(f"   - Calificación promedio: {calificacion_promedio:.2f} estrellas" if calificacion_promedio else "   - Calificación promedio: N/A")
    
    # 5. Ejemplos de pedidos con trazabilidad
    print("\n5. Ejemplos de Pedidos con Trazabilidad:")
    pedidos_con_confirmacion = Pedido.objects.filter(confirmacion_entrega__isnull=False).select_related('idCliente', 'idRepartidor', 'confirmacion_entrega')[:5]
    
    if pedidos_con_confirmacion:
        for pedido in pedidos_con_confirmacion:
            confirmacion = pedido.confirmacion_entrega
            print(f"\n   Pedido #{pedido.idPedido}:")
            print(f"   - Cliente: {pedido.idCliente.nombre}")
            print(f"   - Repartidor: {pedido.idRepartidor.nombreRepartidor if pedido.idRepartidor else 'N/A'}")
            print(f"   - Estado: {pedido.estado_pedido}")
            print(f"   - Calificación: {confirmacion.calificacion} estrellas")
            print(f"   - Comentario: {confirmacion.comentario[:50] if confirmacion.comentario else 'N/A'}")
            print(f"   - Foto: {'Sí' if confirmacion.foto_entrega else 'No'}")
            print(f"   - Fecha confirmación: {confirmacion.fecha_confirmacion}")
    else:
        print("   No hay pedidos con confirmación de entrega")
    
    # 6. Pedidos sin confirmación
    print("\n6. Pedidos sin Confirmación de Entrega:")
    pedidos_sin_confirmacion = Pedido.objects.filter(confirmacion_entrega__isnull=True, estado_pedido='Completado').count()
    print(f"   - Pedidos completados sin confirmación: {pedidos_sin_confirmacion}")
    
    # 7. Verificar integridad referencial
    print("\n7. Verificación de Integridad Referencial:")
    confirmaciones_sin_pedido = ConfirmacionEntrega.objects.filter(pedido__isnull=True).count()
    confirmaciones_sin_repartidor = ConfirmacionEntrega.objects.filter(repartidor__isnull=True).count()
    
    print(f"   - Confirmaciones sin pedido: {confirmaciones_sin_pedido}")
    print(f"   - Confirmaciones sin repartidor: {confirmaciones_sin_repartidor}")
    
    print("\n" + "=" * 80)
    print("FIN DEL DIAGNÓSTICO")
    print("=" * 80)

if __name__ == '__main__':
    diagnosticar()
