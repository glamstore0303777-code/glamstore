import re

# Leer el archivo
with open(r'c:\ProyectoF\glamstore\core\Clientes\perfil\perfil.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar la sección del main content y agregar la sección sin_sesion al inicio
# Buscar: <div class="main-content">
# Agregar después del header la sección condicional

sin_sesion_section = '''
    <!-- Mensaje para usuarios sin sesión -->
    {% if sin_sesion %}
    <div class="content-card" style="text-align: center; padding: 3rem 2rem;">
      <h2 style="margin-bottom: 1.5rem;">Acceso al Perfil</h2>
      <p style="font-size: 1.1rem; color: #666; margin-bottom: 2rem;">
        Para acceder a tu perfil, necesitas:
      </p>
      <ul style="list-style: none; padding: 0; margin-bottom: 2.5rem; text-align: left; max-width: 500px; margin-left: auto; margin-right: auto;">
        <li style="padding: 0.8rem 0; border-bottom: 1px solid #f5f0fa;">
          <strong style="color: #8b7a9b;">Opción 1:</strong> Hacer una compra (puedes comprar sin registrarte)
        </li>
        <li style="padding: 0.8rem 0;">
          <strong style="color: #8b7a9b;">Opción 2:</strong> Crear una cuenta o iniciar sesión
        </li>
      </ul>
      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
        <a href="{% url 'tienda' %}" style="background: linear-gradient(135deg, #d4c5e0 0%, #c5b3d4 100%); color: white; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 500; box-shadow: 0 4px 12px rgba(212, 197, 224, 0.25); transition: all 0.3s;">
          Ir a la Tienda
        </a>
        <a href="{% url 'registro' %}" style="background: white; color: #8b7a9b; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 500; border: 2px solid #d4c5e0; transition: all 0.3s;">
          Registrarse
        </a>
        <a href="{% url 'login' %}" style="background: white; color: #8b7a9b; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 500; border: 2px solid #d4c5e0; transition: all 0.3s;">
          Iniciar Sesión
        </a>
      </div>
    </div>
    {% else %}
'''

# Buscar el patrón donde empieza el contenido principal después del header
pattern = r'(<div class="header">.*?</div>)\s*\n\s*<!-- Información Personal -->'

replacement = r'\1\n' + sin_sesion_section + '\n    <!-- Información Personal -->'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Agregar el cierre del {% else %} y {% endif %} antes del footer
# Buscar el patrón antes del footer
footer_pattern = r'(</div>\s*{% endif %}\s*</div>\s*<footer>)'
footer_replacement = r'\1'

# Primero, necesitamos agregar {% endif %} al final del contenido, antes del footer
# Buscar: </div>\n  </div>\n\n  <footer>
# Reemplazar con: </div>\n    {% endif %}\n  </div>\n\n  <footer>

content = re.sub(
    r'(</div>\s*{% endif %}\s*</div>\s*<footer>)',
    r'</div>\n    {% endif %}\n    {% endif %}\n  </div>\n\n  <footer>',
    content
)

# Guardar
with open(r'c:\ProyectoF\glamstore\core\Clientes\perfil\perfil.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Template perfil.html actualizado correctamente")
