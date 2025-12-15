#!/usr/bin/env python
"""
Script de diagnóstico para verificar el servicio de vencimientos
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.services.vencimientos_service import VencimientosService
from core.models.lotes import LoteProducto
from datetime import date, timedelta

print("=" * 70)
print("🔍 DIAGNÓSTICO DEL SERVICIO DE VENCIMIENTOS")
print("=" * 70)
print()

# 0. Verificar productos disponibles
print("0️⃣  Verificando productos en la base de datos...")
try:
    from core.models.productos import Producto
    total_productos = Producto.objects.count()
    print(f"   ✅ Total de productos: {total_productos}")
    if total_productos > 0:
        productos = Producto.objects.all()[:5]
        print(f"   📋 Primeros 5 productos:")
        for prod in productos:
            print(f"      - {prod.nombreProducto} (ID: {prod.idproducto}, Stock: {prod.stock})")
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print()

# 1. Verificar que la tabla de lotes existe
print("1️⃣  Verificando tabla lotes_producto...")
try:
    count = LoteProducto.objects.count()
    print(f"   ✅ Tabla existe")
    print(f"   📊 Total de lotes: {count}")
    if count > 0:
        lotes = LoteProducto.objects.all()[:5]
        print(f"   📋 Primeros 5 lotes:")
        for lote in lotes:
            print(f"      - {lote.codigo_lote}: {lote.cantidad_disponible} unidades (Vence: {lote.fecha_vencimiento})")
except Exception as e:
    print(f"   ❌ Error: {e}")
    sys.exit(1)

print()

# 2. Verificar lotes vencidos
print("2️⃣  Verificando lotes vencidos...")
try:
    hoy = date.today()
    lotes_vencidos = LoteProducto.objects.filter(
        fecha_vencimiento__lt=hoy,
        cantidad_disponible__gt=0
    )
    print(f"   ✅ Consulta exitosa")
    print(f"   📦 Lotes vencidos: {lotes_vencidos.count()}")
    for lote in lotes_vencidos[:3]:
        print(f"      - {lote.codigo_lote}: {lote.cantidad_disponible} unidades (vencido hace {(hoy - lote.fecha_vencimiento).days} días)")
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print()

# 3. Verificar lotes por vencer
print("3️⃣  Verificando lotes por vencer (próximos 30 días)...")
try:
    hoy = date.today()
    fecha_limite = hoy + timedelta(days=30)
    lotes_por_vencer = LoteProducto.objects.filter(
        fecha_vencimiento__gte=hoy,
        fecha_vencimiento__lte=fecha_limite,
        cantidad_disponible__gt=0
    )
    print(f"   ✅ Consulta exitosa")
    print(f"   📦 Lotes por vencer: {lotes_por_vencer.count()}")
    for lote in lotes_por_vencer[:3]:
        dias_restantes = (lote.fecha_vencimiento - hoy).days
        print(f"      - {lote.codigo_lote}: {lote.cantidad_disponible} unidades (vence en {dias_restantes} días)")
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print()

# 4. Probar función obtener_productos_vencidos
print("4️⃣  Probando VencimientosService.obtener_productos_vencidos()...")
try:
    productos_vencidos = VencimientosService.obtener_productos_vencidos()
    print(f"   ✅ Función ejecutada exitosamente")
    print(f"   📊 Productos vencidos: {len(productos_vencidos)}")
    if productos_vencidos:
        print(f"   📋 Estructura del primer item:")
        item = productos_vencidos[0]
        for key in item.keys():
            print(f"      - {key}: {type(item[key]).__name__}")
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print()

# 5. Probar función obtener_productos_por_vencer
print("5️⃣  Probando VencimientosService.obtener_productos_por_vencer()...")
try:
    productos_por_vencer = VencimientosService.obtener_productos_por_vencer()
    print(f"   ✅ Función ejecutada exitosamente")
    print(f"   📊 Productos por vencer: {len(productos_por_vencer)}")
    if productos_por_vencer:
        print(f"   📋 Estructura del primer item:")
        item = productos_por_vencer[0]
        for key in item.keys():
            print(f"      - {key}: {type(item[key]).__name__}")
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print()

# 6. Probar función obtener_resumen_vencimientos
print("6️⃣  Probando VencimientosService.obtener_resumen_vencimientos()...")
try:
    resumen = VencimientosService.obtener_resumen_vencimientos()
    print(f"   ✅ Función ejecutada exitosamente")
    print(f"   📋 Estructura del resumen:")
    print(f"      - Tipo: {type(resumen).__name__}")
    print(f"      - Claves principales: {list(resumen.keys())}")
    
    if 'productos_vencidos' in resumen:
        pv = resumen['productos_vencidos']
        print(f"   📦 productos_vencidos:")
        print(f"      - Tipo: {type(pv).__name__}")
        print(f"      - Claves: {list(pv.keys())}")
        print(f"      - total_productos: {pv.get('total_productos')}")
        print(f"      - total_cantidad: {pv.get('total_cantidad')}")
        print(f"      - total_valor: {pv.get('total_valor')}")
        print(f"      - detalle (cantidad): {len(pv.get('detalle', []))}")
    
    if 'productos_por_vencer' in resumen:
        ppv = resumen['productos_por_vencer']
        print(f"   📦 productos_por_vencer:")
        print(f"      - Tipo: {type(ppv).__name__}")
        print(f"      - Claves: {list(ppv.keys())}")
        print(f"      - total_productos: {ppv.get('total_productos')}")
        print(f"      - total_cantidad: {ppv.get('total_cantidad')}")
        print(f"      - total_valor: {ppv.get('total_valor')}")
        print(f"      - criticos: {ppv.get('criticos')}")
        print(f"      - altos: {ppv.get('altos')}")
        print(f"      - medios: {ppv.get('medios')}")
        print(f"      - detalle (cantidad): {len(ppv.get('detalle', []))}")
        
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print()
print("=" * 70)
print("✅ Diagnóstico completado")
print("=" * 70)
