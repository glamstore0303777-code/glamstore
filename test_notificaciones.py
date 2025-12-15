#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import NotificacionProblema

print("Intentando obtener notificaciones...")
try:
    notificaciones = NotificacionProblema.objects.select_related(
        'idPedido__idCliente',
        'idPedido__idRepartidor'
    ).order_by('-fechaReporte')
    
    print(f"✓ Query ejecutada correctamente")
    print(f"  Total: {notificaciones.count()}")
    
    for notif in notificaciones[:5]:
        print(f"  - {notif.idNotificacion}: {notif.fechaReporte}")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
