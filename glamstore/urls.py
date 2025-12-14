from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from core.Clientes import views as cliente_views
tienda_view = cliente_views.tienda

def diagnostico_view(request):
    """Vista de diagnóstico para verificar la configuración"""
    import os
    from django.conf import settings
    
    diagnostico = {
        'DEBUG': settings.DEBUG,
        'ALLOWED_HOSTS': settings.ALLOWED_HOSTS,
        'DATABASE_URL': os.getenv('DATABASE_URL', 'NO CONFIGURADO'),
        'DATABASES': str(settings.DATABASES),
        'INSTALLED_APPS': settings.INSTALLED_APPS,
    }
    
    return JsonResponse(diagnostico)

urlpatterns = [
 path('admin/', admin.site.urls),
 path('diagnostico/', diagnostico_view, name='diagnostico'),
path('', tienda_view, name='tienda'),# Ruta principal ahora usa la vista correcta
 path('', include('core.Clientes.urls')), # Rutas de la app Clientes
 path('gestion/', include('core.Gestion_admin.urls')),  # ← esta línea es clave

]

# Servir archivos media en desarrollo y producción
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)