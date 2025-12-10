#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from PIL import Image, ImageDraw
from core.models import Categoria
from django.core.files.base import ContentFile
from io import BytesIO

# Crear directorio si no existe
os.makedirs('media/categorias', exist_ok=True)

# Colores para cada categoría
colores = {
    'Maquillaje': '#FF69B4',
    'Skincare': '#87CEEB',
    'Fragancias': '#FFD700',
    'Accesorios': '#DDA0DD',
    'Cabello': '#F0E68C'
}

# Obtener todas las categorías
categorias = Categoria.objects.all()

for categoria in categorias:
    # Si ya tiene imagen, saltar
    if categoria.imagen:
        print(f"✓ {categoria.nombreCategoria} ya tiene imagen")
        continue
    
    # Obtener color o usar uno por defecto
    color = colores.get(categoria.nombreCategoria, '#A855F7')
    color_rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    # Crear imagen
    img = Image.new('RGB', (400, 300), color_rgb)
    draw = ImageDraw.Draw(img)
    
    # Dibujar texto
    text = categoria.nombreCategoria
    bbox = draw.textbbox((0, 0), text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (400 - text_width) // 2
    y = (300 - text_height) // 2
    
    draw.text((x, y), text, fill='white')
    
    # Guardar en memoria
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)
    
    # Guardar en el modelo
    filename = f'{categoria.nombreCategoria.lower()}.png'
    categoria.imagen.save(filename, ContentFile(img_io.read()), save=True)
    
    print(f"✓ Imagen creada para: {categoria.nombreCategoria}")

print("\n¡Listo! Todas las categorías tienen imágenes.")
