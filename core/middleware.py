import os
from django.http import FileResponse
from django.conf import settings

class MediaFilesMiddleware:
    """Middleware para servir archivos media en producción"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Si la URL comienza con /media/, intentar servir el archivo
        if request.path.startswith('/media/'):
            file_path = request.path[7:]  # Remover '/media/'
            full_path = os.path.join(settings.MEDIA_ROOT, file_path)
            
            # Verificar que el archivo existe y está dentro de MEDIA_ROOT
            if os.path.exists(full_path) and os.path.isfile(full_path):
                try:
                    return FileResponse(open(full_path, 'rb'))
                except Exception:
                    pass
        
        return self.get_response(request)
