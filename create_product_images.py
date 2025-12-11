#!/usr/bin/env python
"""
Script para crear imágenes placeholder para todos los productos
"""
import os
from pathlib import Path

# Crear directorio de productos si no existe
MEDIA_DIR = Path('media/productos')
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

# Lista de imágenes de productos del SQL
PRODUCT_IMAGES = [
    'rubor.jpg',
    'ilumi_p.webp',
    'corrector.avif',
    'base_polvo.webp',
    'base.png',
    's.jpg',
    'delini.webp',
    'pestanina.webp',
    'pinta_cejaz.avif',
    'l.webp',
    'll.webp',
    'balsamo.webp',
    'dd.webp',
    'la.webp',
    'esm.webp',
    'top.jpg',
    'tr.webp',
    'ess.webp',
    'ki.webp',
    'br.webp',
    'esp.webp',
    'pinzas.webp',
    'o.webp',
    'es.jpg',
    'red_velved.jpg',
    'otra_b.webp',
    'p.webp',
    'bronceador.jpg',
    'Serum_Centella_Asiática_Antiedad_Calmante_Control_Poros_Tipo_De_Piel_Todo_Tipo_h3J3iRp.png',
]

# SVG placeholder template
SVG_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e8b4f0;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d4a5e8;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="300" height="300" fill="url(#grad)"/>
  <circle cx="150" cy="150" r="80" fill="#c2185b" opacity="0.3"/>
  <text x="150" y="155" font-size="16" text-anchor="middle" fill="#666" font-family="Arial">
    Producto
  </text>
</svg>
'''

# Crear archivos placeholder
for image_name in PRODUCT_IMAGES:
    image_path = MEDIA_DIR / image_name
    
    # Si el archivo ya existe, no lo sobrescribimos
    if image_path.exists():
        print(f"✓ {image_name} ya existe")
        continue
    
    # Crear archivo SVG como placeholder
    try:
        image_path.write_text(SVG_TEMPLATE)
        print(f"✓ Creado: {image_name}")
    except Exception as e:
        print(f"✗ Error creando {image_name}: {e}")

print("\n✓ Imágenes placeholder creadas exitosamente")
