from django.core.management.base import BaseCommand
from core.models import Producto


class Command(BaseCommand):
    help = 'Calcula y actualiza el precio_venta para todos los productos'

    def handle(self, *args, **options):
        productos = Producto.objects.all()
        
        if not productos.exists():
            self.stdout.write(self.style.WARNING('No hay productos en la base de datos'))
            return
        
        actualizados = 0
        for producto in productos:
            if not producto.precio_venta or producto.precio_venta == 0:
                producto.precio_venta = producto.calcular_precio_venta()
                producto.save()
                actualizados += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Producto {producto.idProducto} ({producto.nombreProducto}): '
                        f'precio_venta = ${producto.precio_venta}'
                    )
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Total de productos actualizados: {actualizados}')
        )
