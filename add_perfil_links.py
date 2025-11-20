import re
import os

# Lista de archivos a modificar
archivos = [
    r'c:\ProyectoF\glamstore\core\Clientes\tienda\tienda.html',
    r'c:\ProyectoF\glamstore\core\Clientes\productos_categoria\productos_categoria.html',
    r'c:\ProyectoF\glamstore\core\Clientes\carrito\carrito.html',
    r'c:\ProyectoF\glamstore\core\Clientes\seguimiento_pedidos\checkout.html',
    r'c:\ProyectoF\glamstore\core\Clientes\registrar_usuario\login.html'
]

# Enlace a agregar
perfil_link = '<li><a href="{% url \'perfil\' %}">Mi Perfil</a></li>'

for archivo in archivos:
    if not os.path.exists(archivo):
        print(f"Archivo no encontrado: {archivo}")
        continue
    
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar el patrón del menú de navegación
        # Patrón 1: Buscar después de "Carrito" y antes de cualquier cierre de lista o sección
        pattern1 = r'(<li><a href="{% url \'ver_carrito\' %}">.*?Carrito.*?</a></li>)'
        
        if re.search(pattern1, content):
            # Agregar después del enlace del carrito
            content = re.sub(
                pattern1,
                r'\1\n      ' + perfil_link,
                content,
                count=1
            )
            
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"OK - Actualizado: {os.path.basename(archivo)}")
        else:
            print(f"WARN - No se encontro el patron en: {os.path.basename(archivo)}")
    
    except Exception as e:
        print(f"ERROR en {os.path.basename(archivo)}: {str(e)}")

print("\nProceso completado!")
