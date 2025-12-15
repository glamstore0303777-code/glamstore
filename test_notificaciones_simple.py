import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamstore.settings')
django.setup()

from core.models import NotificacionProblema

try:
    print("Intentando obtener notificaciones...")
    notificaciones = NotificacionProblema.objects.select_related(
        'idPedido__idCliente',
        'idPedido__idRepartidor'
    ).order_by('-fechaReporte')[:5]
    
    print("OK - Query ejecutada correctamente")
    print(f"Total: {notificaciones.count()}")
    
except Exception as e:
    print(f"ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
