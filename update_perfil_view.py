import re

# Leer el archivo
with open(r'c:\ProyectoF\glamstore\core\Clientes\views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar y reemplazar la función perfil
old_perfil = r'''# ✅ Vista del perfil del usuario \(puedes expandirla luego\)
def perfil\(request\):
    # Verificar si hay un usuario logueado o un cliente invitado
    usuario_id = request\.session\.get\('usuario_id'\)
    cliente_id = request\.session\.get\('cliente_id'\)
    
    if not usuario_id and not cliente_id:
        messages\.error\(request, "Debes iniciar sesión o hacer un pedido para ver tu perfil\."\)
        return redirect\('login'\)

    try:
        # Si hay usuario logueado, obtener el cliente desde el usuario
        if usuario_id:
            usuario = get_object_or_404\(Usuario, idUsuario=usuario_id\)
            cliente = get_object_or_404\(Cliente, idCliente=usuario\.idCliente\)
            tiene_usuario = True
        # Si solo hay cliente_id \(invitado\), obtener el cliente directamente
        else:
            cliente = get_object_or_404\(Cliente, idCliente=cliente_id\)
            tiene_usuario = False
        
        # Obtener los pedidos del cliente
        pedidos = Pedido\.objects\.filter\(idCliente=cliente\.idCliente\)\.order_by\('-fechaCreacion'\)
        
    except \(Usuario\.DoesNotExist, Cliente\.DoesNotExist, Http404\):
        messages\.error\(request, "No se pudo encontrar tu perfil de cliente\."\)
        return redirect\('tienda'\)

    context = \{
        'cliente': cliente,
        'pedidos': pedidos,
        'tiene_usuario': tiene_usuario  # Para mostrar opción de crear usuario en el template
    \}
    return render\(request, 'perfil\.html', context\)'''

new_perfil = '''# ✅ Vista del perfil del usuario
def perfil(request):
    # Verificar si hay un usuario logueado o un cliente invitado
    usuario_id = request.session.get('usuario_id')
    cliente_id = request.session.get('cliente_id')
    
    # Caso 1: Sin sesión - mostrar mensaje con opciones
    if not usuario_id and not cliente_id:
        context = {
            'sin_sesion': True
        }
        return render(request, 'perfil.html', context)

    try:
        # Caso 2: Usuario logueado - obtener el cliente desde el usuario
        if usuario_id:
            usuario = get_object_or_404(Usuario, idUsuario=usuario_id)
            cliente = get_object_or_404(Cliente, idCliente=usuario.idCliente)
            tiene_usuario = True
        # Caso 3: Cliente invitado - obtener el cliente directamente
        else:
            cliente = get_object_or_404(Cliente, idCliente=cliente_id)
            tiene_usuario = False
        
        # Obtener los pedidos del cliente
        pedidos = Pedido.objects.filter(idCliente=cliente.idCliente).order_by('-fechaCreacion')
        
    except (Usuario.DoesNotExist, Cliente.DoesNotExist, Http404):
        messages.error(request, "No se pudo encontrar tu perfil de cliente.")
        return redirect('tienda')

    context = {
        'cliente': cliente,
        'pedidos': pedidos,
        'tiene_usuario': tiene_usuario,  # Para mostrar opción de crear usuario en el template
        'sin_sesion': False
    }
    return render(request, 'perfil.html', context)'''

# Reemplazar
content = re.sub(old_perfil, new_perfil, content, flags=re.DOTALL)

# Guardar
with open(r'c:\ProyectoF\glamstore\core\Clientes\views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Archivo actualizado correctamente")
