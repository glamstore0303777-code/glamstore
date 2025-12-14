"""
Comando Django para cargar datos iniciales de productos, categorías, etc.
Uso: python manage.py load_initial_data
"""
from django.core.management.base import BaseCommand
from django.db import connection
from core.models import Categoria, Subcategoria, Producto
from decimal import Decimal


class Command(BaseCommand):
    help = 'Carga datos iniciales de productos, categorías y subcategorías'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos iniciales (upsert mode)...')
        
        # Mostrar estado actual
        productos_count = Producto.objects.count()
        if productos_count > 0:
            self.stdout.write(f'  Productos existentes: {productos_count} - se actualizarán si es necesario')
        
        try:
            # Primero cargar categorías
            self._load_categorias()
            
            # Luego subcategorías
            self._load_subcategorias()
            
            # Finalmente productos (sin FK constraints temporalmente)
            self._load_productos_raw()
            
            self.stdout.write(self.style.SUCCESS(
                f'✓ Datos cargados: {Categoria.objects.count()} categorías, '
                f'{Subcategoria.objects.count()} subcategorías, '
                f'{Producto.objects.count()} productos'
            ))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error cargando datos: {e}'))
            import traceback
            traceback.print_exc()
            # No hacer raise para que el build continúe

    def _load_categorias(self):
        """Cargar categorías usando SQL directo"""
        categorias_data = [
            (1, 'Rostro', 'Base, correctores, polvos compactos, rubores e iluminadores', 'categorias/rostro.avif'),
            (2, 'Ojos', 'Sombras, delineadores, pestaninas y cejas', 'categorias/ojos.jpg'),
            (3, 'Labios', 'Labiales, brillos y delineadores de labios', 'categorias/la.jpg'),
            (4, 'Unas', 'Esmaltes, tratamientos y accesorios para unas', 'categorias/unas.webp'),
            (5, 'Accesorios', 'Brochas, esponjas y herramientas de maquillaje', 'categorias/accessories_feb_main.jpg'),
            (9, 'Cuidado Facial', 'cremas,serums', 'categorias/cuidado_facial_T4konPk.jpg'),
        ]
        
        with connection.cursor() as cursor:
            for id_cat, nombre, desc, imagen in categorias_data:
                try:
                    cursor.execute("""
                        INSERT INTO categorias (idcategoria, nombrecategoria, descripcion, imagen)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (idcategoria) DO UPDATE SET
                            nombrecategoria = EXCLUDED.nombrecategoria,
                            descripcion = EXCLUDED.descripcion,
                            imagen = EXCLUDED.imagen
                    """, [id_cat, nombre, desc, imagen])
                except Exception as e:
                    self.stdout.write(f'  Error insertando categoria {id_cat}: {e}')
        
        self.stdout.write(f'  - {len(categorias_data)} categorias cargadas')


    def _load_subcategorias(self):
        """Cargar subcategorías usando SQL directo"""
        subcategorias_data = [
            (1, 'Base', 1),
            (2, 'Correctores', 1),
            (3, 'Polvos compactos', 1),
            (4, 'Rubores', 1),
            (5, 'Iluminadores', 1),
            (6, 'Sombras', 2),
            (7, 'Delineadores', 2),
            (8, 'Pestaninas', 2),
            (9, 'Cejas', 2),
            (10, 'Labiales', 3),
            (11, 'Brillos', 3),
            (12, 'Balsamos', 3),
            (13, 'Delineadores de labios', 3),
            (14, 'Esmaltes', 4),
            (15, 'Tratamientos', 4),
            (16, 'Accesorios unas', 4),
            (17, 'Brochas', 5),
            (18, 'Esponjas', 5),
            (19, 'Organizadores', 5),
            (27, 'Bronceadores', 1),
            (28, 'Serums', 9),
        ]
        
        with connection.cursor() as cursor:
            for id_sub, nombre, id_cat in subcategorias_data:
                try:
                    cursor.execute("""
                        INSERT INTO subcategorias (idsubcategoria, nombresubcategoria, idcategoria)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (idsubcategoria) DO UPDATE SET
                            nombresubcategoria = EXCLUDED.nombresubcategoria,
                            idcategoria = EXCLUDED.idcategoria
                    """, [id_sub, nombre, id_cat])
                except Exception as e:
                    self.stdout.write(f'  Error insertando subcategoria {id_sub}: {e}')
        
        self.stdout.write(f'  - {len(subcategorias_data)} subcategorias cargadas')

    def _load_productos_raw(self):
        """Cargar productos usando SQL directo"""
        # (id, nombre, precio, desc, stock, cat, subcat, imagen, precio_venta)
        productos_data = [
            (7700000000001, 'Rubor Rosado Glow', 34000, 'Rubor en polvo con acabado satinado y pigmento suave.', 469, 1, 4, 'productos/rubor.jpg', 44100),
            (7700000000002, 'Iluminador Perla Glam', 32000, 'Ilumina tus mejillas con un brillo nacarado y elegante.', 387, 1, 5, 'productos/ilumi_p.webp', 41500),
            (7700000000003, 'Corrector Liquido Soft Touch', 29000, 'Cobertura media con textura ligera y acabado natural.', 615, 1, 2, 'productos/corrector.avif', 37600),
            (7700000000004, 'Polvo Compacto Mate Glam', 38000, 'Controla el brillo con un acabado mate y aterciopelado.', 526, 1, 3, 'productos/base_polvo.webp', 49300),
            (7700000000005, 'Base Cushion Glow', 58000, 'Base ligera con esponja cushion y efecto luminoso.', 336, 1, 1, 'productos/base.png', 75250),
            (7700000000011, 'Sombra Cuarteto Rosa', 42000, 'Paleta de 4 tonos rosados con acabado satinado.', 101, 2, 6, 'productos/s.jpg', 54500),
            (7700000000012, 'Delineador Liquido Precision', 18000, 'Punta fina para trazos definidos y resistentes al agua.', 99, 2, 7, 'productos/delini.webp', 23350),
            (7700000000013, 'Pestanina Curvas Glam', 16000, 'Define y curva tus pestanas con formula ligera.', 45, 2, 8, 'productos/pestanina.webp', 20750),
            (7700000000014, 'Gel para Cejas Natural Brow', 20000, 'Fija y da forma a tus cejas con acabado natural.', 37, 2, 9, 'productos/pinta_cejaz.avif', 25950),
            (7700000000015, 'Sombra Liquida Glitter Pop', 25000, 'Brillo liquido para parpados con efecto multidimensional.', 45, 2, 6, 'productos/l.webp', 32450),
            (7700000000021, 'Brillo Labial Cristal', 22000, 'Gloss transparente con efecto volumen y aroma a vainilla.', 11, 3, 11, 'productos/ll.webp', 28550),
            (7700000000023, 'Balsamo Hidratante Berry Kiss', 18000, 'Hidratacion profunda con aroma a frutos rojos.', 44, 3, 12, 'productos/balsamo.webp', 23350),
            (7700000000024, 'Delineador de Labios Coral Chic', 15000, 'Define y realza con precision y suavidad.', 117, 3, 13, 'productos/dd.webp', 19450),
            (7700000000025, 'Labial Cremoso Fucsia Pop', 30000, 'Color vibrante con textura cremosa y humectante.', 13, 3, 10, 'productos/la.webp', 38900),
            (7700000000031, 'Esmalte Rosa Pastel', 12000, 'Color suave, formula vegana y secado rapido.', 11, 4, 14, 'productos/esm.webp', 15550),
            (7700000000032, 'Top Coat Brillo Extremo', 14000, 'Proteccion y brillo espejo para tus unas.', 5, 4, 15, 'productos/top.jpg', 18150),
            (7700000000033, 'Tratamiento Fortalecedor', 18000, 'Fortalece unas quebradizas con queratina y calcio.', 11, 4, 15, 'productos/tr.webp', 23350),
            (7700000000034, 'Esmalte Glitter Champagne', 15000, 'Brillo dorado para un acabado festivo y glamuroso.', 21, 4, 14, 'productos/ess.webp', 19450),
            (7700000000035, 'Kit Decoracion de Unas', 5000, 'Piedras, stickers y pinceles para disenos creativos.', 101, 4, 16, 'productos/ki.webp', 6500),
            (7700000000041, 'Set de Brochas Rosa Gold', 48000, '10 brochas suaves para rostro y ojos en estuche glam.', 12, 5, 17, 'productos/br.webp', 62250),
            (7700000000042, 'Esponja Blender Lavanda', 15000, 'Esponja suave para base y corrector, acabado uniforme.', 15, 5, 18, 'productos/esp.webp', 19450),
            (7700000000043, 'Pinza de Cejas Glam', 12000, 'Precision y diseno ergonomico en acabado metalico rosado.', 16, 5, 9, 'productos/pinzas.webp', 15550),
            (7700000000044, 'Organizador Acrilico Mini', 28000, 'Guarda tus productos con estilo y orden.', 14, 5, 19, 'productos/o.webp', 36300),
            (7700000000045, 'Espejo LED Glam', 35000, 'Espejo compacto con luz LED y aumento x5.', 55, 5, None, 'productos/es.jpg', 45400),
            (7701122334455, 'Labial Mate Velvet Glam', 5000, 'Color intenso, textura aterciopelada, larga duracion', 84, 3, 10, 'productos/red_velved.jpg', 6500),
            (7701234567890, 'Base Liquida HD Glam', 55000, 'Cobertura alta, acabado natural, ideal para piel mixta', 198, 1, 1, 'productos/otra_b.webp', 71350),
            (7709876543210, 'Pestanina Volumen Total Glam', 15000, 'Volumen extremo, resistente al agua, formula vegana', 15, 2, 8, 'productos/p.webp', 19450),
            (7709876543220, 'Bronceador trendy', 15000, 'Bronceador de trendy', 16, 1, 27, 'productos/bronceador.jpg', 19450),
            (7709876543221, 'Serum Centella Asiatica', 8500, 'Serum Centella Asiatica Antiedad Calmante Control Poros', 8, 9, 28, 'productos/serum.png', 11050),
        ]
        
        inserted = 0
        with connection.cursor() as cursor:
            for data in productos_data:
                id_prod, nombre, precio, desc, stock, id_cat, id_sub, imagen, precio_venta = data
                try:
                    cursor.execute("""
                        INSERT INTO productos (idproducto, nombreproducto, precio, descripcion, stock, 
                                               idcategoria, idsubcategoria, imagen, precio_venta, cantidaddisponible)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (idproducto) DO UPDATE SET
                            nombreproducto = EXCLUDED.nombreproducto,
                            precio = EXCLUDED.precio,
                            descripcion = EXCLUDED.descripcion,
                            stock = EXCLUDED.stock,
                            idcategoria = EXCLUDED.idcategoria,
                            idsubcategoria = EXCLUDED.idsubcategoria,
                            imagen = EXCLUDED.imagen,
                            precio_venta = EXCLUDED.precio_venta,
                            cantidaddisponible = EXCLUDED.cantidaddisponible
                    """, [id_prod, nombre, precio, desc, stock, id_cat, id_sub, imagen, precio_venta, stock])
                    inserted += 1
                except Exception as e:
                    self.stdout.write(f'  Error insertando producto {id_prod}: {e}')
        
        self.stdout.write(f'  - {inserted}/{len(productos_data)} productos cargados')
