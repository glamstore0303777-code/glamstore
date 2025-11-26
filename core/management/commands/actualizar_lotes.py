from django.core.management.base import BaseCommand
from django.db.models import Sum
from core.models.lotes import LoteProducto
from core.models.productos import Producto
from core.models.movimientos import MovimientoProducto


class Command(BaseCommand):
    help = 'Actualiza los lotes existentes con el código de lote real del producto'

    def handle(self, *args, **options):
        self.stdout.write('Actualizando lotes con datos reales de productos...')
        
        productos = Producto.objects.all()
        
        for producto in productos:
            lotes = list(LoteProducto.objects.filter(producto=producto).order_by('fecha_entrada'))
            
            if len(lotes) == 0:
                continue
            
            if len(lotes) > 1:
                # Consolidar múltiples lotes en uno solo
                primer_lote = lotes[0]
                otros_lotes_ids = [l.idLote for l in lotes[1:]]
                
                # Sumar cantidades
                cantidad_inicial = sum(l.cantidad_inicial for l in lotes)
                cantidad_disponible = sum(l.cantidad_disponible for l in lotes)
                
                # Reasignar movimientos al primer lote
                MovimientoProducto.objects.filter(lote_origen_id__in=otros_lotes_ids).update(lote_origen=primer_lote)
                
                # Eliminar lotes duplicados
                LoteProducto.objects.filter(idLote__in=otros_lotes_ids).delete()
                
                # Actualizar primer lote
                primer_lote.cantidad_inicial = cantidad_inicial
                primer_lote.cantidad_disponible = cantidad_disponible
                
                self.stdout.write(f'  {producto.nombreProducto}: consolidados {len(lotes)} lotes')
            else:
                primer_lote = lotes[0]
            
            # Actualizar con datos del producto
            if producto.lote:
                primer_lote.codigo_lote = producto.lote
            if producto.fechaVencimiento:
                primer_lote.fecha_vencimiento = producto.fechaVencimiento
            primer_lote.proveedor = None
            primer_lote.save()
            
            self.stdout.write(f'  {producto.nombreProducto}: lote = {primer_lote.codigo_lote}')
        
        # Actualizar movimientos con datos del lote
        movimientos = MovimientoProducto.objects.filter(lote_origen__isnull=False).select_related('lote_origen')
        for mov in movimientos:
            mov.lote = mov.lote_origen.codigo_lote
            mov.fecha_vencimiento = mov.lote_origen.fecha_vencimiento
            mov.save()
        
        self.stdout.write(self.style.SUCCESS('Actualización completada.'))
