"""
Comando Django para cargar datos iniciales de productos, categorías, etc.
Uso: python manage.py load_initial_data
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Categoria, Subcategoria, Producto
from decimal import Decimal


class Command(BaseCommand):
    help = 'Carga datos iniciales de productos, categorías y subcategorías'

    def handle(self, *args, **options):
        self.stdout.write('Verificando datos existentes...')
        
        # Verificar si ya hay productos
        if Producto.objects.exists():
            self.stdout.write(self.style.WARNING(
                f'Ya existen {Producto.objects.count()} productos en la BD. Saltando carga.'
            ))
            return
        
        self.stdout.write('Cargando datos iniciales...')
        
        try:
            with transaction.atomic():
                self._load_categorias()
                self._load_subcategorias()
                self._load_productos()
            
            self.stdout.write(self.style.SUCCESS(
                f'✓ Datos cargados: {Categoria.objects.count()} categorías, '
                f'{Subcategoria.objects.count()} subcategorías, '
                f'{Producto.objects.count()} productos'
            ))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error cargando datos: {e}'))
            raise

    def _load_categorias(self):
        """Cargar categorías"""
        categorias_data = [
            (1, 'Rostro', 'Base, correctores, polvos compactos, rubores e iluminadores', 'categorias/rostro.avif'),
            (2, 'Ojos', 'Sombras, delineadores, pestañinas y cejas', 'categorias/ojos.jpg'),
            (3, 'Labios', 'Labiales, brillos y delineadores de labios', 'categorias/la.jpg'),
            (4, 'Uñas', 'Esmaltes, tratamientos y accesorios para uñas', 'categorias/uñas.webp'),
            (5, 'Accesorios', 'Brochas, esponjas y herramientas de maquillaje', 'categorias/accessories_feb_main.jpg'),
            (9, 'Cuidado Facial', 'cremas,serums', 'categorias/cuidado_facial_T4konPk.jpg'),
        ]
        
        for id_cat, nombre, desc, imagen in categorias_data:
            Categoria.objects.update_or_create(
                idCategoria=id_cat,
                defaults={
                    'nombreCategoria': nombre,
                    'descripcion': desc,
                    'imagen': imagen
                }
            )
        self.stdout.write(f'  - {len(categorias_data)} categorías cargadas')


    def _load_subcategorias(self):
        """Cargar subcategorías"""
        subcategorias_data = [
            (1, 'Base', 1),
            (2, 'Correctores', 1),
            (3, 'Polvos compactos', 1),
            (4, 'Rubores', 1),
            (5, 'Iluminadores', 1),
            (6, 'Sombras', 2),
            (7, 'Delineadores', 2),
            (8, 'Pestañinas', 2),
            (9, 'Cejas', 2),
            (10, 'Labiales', 3),
            (11, 'Brillos', 3),
            (12, 'Bálsamos', 3),
            (13, 'Delineadores de labios', 3),
            (14, 'Esmaltes', 4),
            (15, 'Tratamientos', 4),
            (16, 'Accesorios uñas', 4),
            (17, 'Brochas', 5),
            (18, 'Esponjas', 5),
            (19, 'Organizadores', 5),
            (27, 'Bronceadores', 1),
            (28, 'Serums', 9),
        ]
        
        for id_sub, nombre, id_cat in subcategorias_data:
            try:
                categoria = Categoria.objects.get(idCategoria=id_cat)
                Subcategoria.objects.update_or_create(
                    idSubcategoria=id_sub,
                    defaults={
                        'nombreSubcategoria': nombre,
                        'categoria': categoria
                    }
                )
            except Categoria.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'  Categoría {id_cat} no existe para subcategoría {nombre}'))
        
        self.stdout.write(f'  - {len(subcategorias_data)} subcategorías cargadas')

    def _load_productos(self):
        """Cargar productos"""
        productos_data = [
            # (idProducto, nombreProducto, precio, descripcion, stock, idCategoria, idSubcategoria, imagen, precio_venta)
            (7700000000001, 'Rubor Rosado Glow', 34000, 'Rubor en polvo con acabado satinado y pigmento suave.', 469, 1, 4, 'productos/rubor.jpg', 44100),
            (7700000000002, 'Iluminador Perla Glam', 32000, 'Ilumina tus mejillas con un brillo nacarado y elegante.', 387, 1, 5, 'productos/ilumi_p.webp', 41500),
            (7700000000003, 'Corrector Liquido Soft Touch', 29000, 'Cobertura media con textura ligera y acabado natural.', 615, 1, 2, 'productos/corrector.avif', 37600),
            (7700000000004, 'Polvo Compacto Mate Glam', 38000, 'Controla el brillo con un acabado mate y aterciopelado.', 526, 1, 3, 'productos/base_polvo.webp', 49300),
            (7700000000005, 'Base Cushion Glow', 58000, 'Base ligera con esponja cushion y efecto luminoso.', 336, 1, 1, 'productos/base.png', 75250),
            (7700000000011, 'Sombra Cuarteto Rosa', 42000, 'Paleta de 4 tonos rosados con acabado satinado.', 101, 2, 6, 'productos/s.jpg', 54500),
            (7700000000012, 'Delineador Liquido Precision', 18000, 'Punta fina para trazos definidos y resistentes al agua.', 99, 2, 7, 'productos/delini.webp', 23350),
            (7700000000013, 'Pestañina Curvas Glam', 16000, 'Define y curva tus pestañas con fórmula ligera.', 45, 2, 8, 'productos/pestanina.webp', 20750),
            (7700000000014, 'Gel para Cejas Natural Brow', 20000, 'Fija y da forma a tus cejas con acabado natural.', 37, 2, 9, 'productos/pinta_cejaz.avif', 25950),
            (7700000000015, 'Sombra Liquida Glitter Pop', 25000, 'Brillo liquido para parpados con efecto multidimensional.', 45, 2, 6, 'productos/l.webp', 32450),
            (7700000000021, 'Brillo Labial Cristal', 22000, 'Gloss transparente con efecto volumen y aroma a vainilla.', 11, 3, 11, 'productos/ll.webp', 28550),
            (7700000000023, 'Balsamo Hidratante Berry Kiss', 18000, 'Hidratación profunda con aroma a frutos rojos.', 44, 3, 12, 'productos/balsamo.webp', 23350),
            (7700000000024, 'Delineador de Labios Coral Chic', 15000, 'Define y realza con precisión y suavidad.', 117, 3, 13, 'productos/dd.webp', 19450),
            (7700000000025, 'Labial Cremoso Fucsia Pop', 30000, 'Color vibrante con textura cremosa y humectante.', 13, 3, 10, 'productos/la.webp', 38900),
            (7700000000031, 'Esmalte Rosa Pastel', 12000, 'Color suave, fórmula vegana y secado rápido.', 11, 4, 14, 'productos/esm.webp', 15550),
            (7700000000032, 'Top Coat Brillo Extremo', 14000, 'Protección y brillo espejo para tus uñas.', 5, 4, 15, 'productos/top.jpg', 18150),
            (7700000000033, 'Tratamiento Fortalecedor', 18000, 'Fortalece uñas quebradizas con queratina y calcio.', 11, 4, 15, 'productos/tr.webp', 23350),
            (7700000000034, 'Esmalte Glitter Champagne', 15000, 'Brillo dorado para un acabado festivo y glamuroso.', 21, 4, 14, 'productos/ess.webp', 19450),
            (7700000000035, 'Kit Decoracion de Uñas', 5000, 'Piedras, stickers y pinceles para diseños creativos.', 101, 4, 16, 'productos/ki.webp', 6500),
            (7700000000041, 'Set de Brochas Rosa Gold', 48000, '10 brochas suaves para rostro y ojos en estuche glam.', 12, 5, 17, 'productos/br.webp', 62250),
            (7700000000042, 'Esponja Blender Lavanda', 15000, 'Esponja suave para base y corrector, acabado uniforme.', 15, 5, 18, 'productos/esp.webp', 19450),
            (7700000000043, 'Pinza de Cejas Glam', 12000, 'Precisión y diseño ergonómico en acabado metálico rosado.', 16, 5, 9, 'productos/pinzas.webp', 15550),
            (7700000000044, 'Organizador Acrilico Mini', 28000, 'Guarda tus productos con estilo y orden.', 14, 5, 19, 'productos/o.webp', 36300),
            (7700000000045, 'Espejo LED Glam', 35000, 'Espejo compacto con luz LED y aumento x5.', 55, 5, None, 'productos/es.jpg', 45400),
            (7701122334455, 'Labial Mate Velvet Glam', 5000, 'Color intenso, textura aterciopelada, larga duración', 84, 3, 10, 'productos/red_velved.jpg', 6500),
            (7701234567890, 'Base Liquida HD Glam', 55000, 'Cobertura alta, acabado natural, ideal para piel mixta', 198, 1, 1, 'productos/otra_b.webp', 71350),
            (7709876543210, 'Pestañina Volumen Total Glam', 15000, 'Volumen extremo, resistente al agua, fórmula vegana', 15, 2, 8, 'productos/p.webp', 19450),
            (7709876543220, 'Bronceador trendy', 15000, 'Bronceador de trendy', 16, 1, 27, 'productos/bronceador.jpg', 19450),
            (7709876543221, 'Serum Centella Asiática', 8500, 'Serum Centella Asiática Antiedad Calmante Control Poros', 8, 9, 28, 'productos/Serum_Centella_Asiática_Antiedad_Calmante_Control_Poros_Tipo_De_Piel_Todo_Tipo_h3J3iRp.png', 11050),
        ]
        
        for data in productos_data:
            id_prod, nombre, precio, desc, stock, id_cat, id_sub, imagen, precio_venta = data
            
            try:
                categoria = Categoria.objects.get(idCategoria=id_cat) if id_cat else None
            except Categoria.DoesNotExist:
                categoria = None
            
            try:
                subcategoria = Subcategoria.objects.get(idSubcategoria=id_sub) if id_sub else None
            except Subcategoria.DoesNotExist:
                subcategoria = None
            
            Producto.objects.update_or_create(
                idProducto=id_prod,
                defaults={
                    'nombreProducto': nombre,
                    'precio': Decimal(str(precio)),
                    'descripcion': desc,
                    'stock': stock,
                    'idCategoria': categoria,
                    'idSubcategoria': subcategoria,
                    'imagen': imagen,
                    'precio_venta': Decimal(str(precio_venta)),
                }
            )
        
        self.stdout.write(f'  - {len(productos_data)} productos cargados')
