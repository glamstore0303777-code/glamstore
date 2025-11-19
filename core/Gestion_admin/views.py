from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.db.models import Sum
from core.models.distribuidores import Distribuidor
from core.models.clientes import Cliente
from core.models.pedidos import Pedido
from core.models import Categoria, Subcategoria, Producto, Usuario, MovimientoProducto
from core.models.pedidos import DetallePedido
from django.contrib.auth import logout
from django.urls import reverse
from core.models.repartidores import Repartidor
from django.template.loader import get_template
from django.db.models import Count
from xhtml2pdf import pisa
from django.http import HttpResponse
from io import BytesIO
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.hashers import make_password
 


def index(request):
    return render(request, 'index.html')  # o cualquier plantilla que tengas
# Dashboard principal
def dashboard_admin_view(request):
    # Definir el umbral de tiempo
    una_semana_atras = datetime.now() - timedelta(days=7)
    
    # 1. Producto más vendido de la semana
    producto_mas_vendido = DetallePedido.objects.filter(
        idPedido__fechaCreacion__gte=una_semana_atras
    ).values(
        'idProducto__nombreProducto'
    ).annotate(
        total_vendido=Sum('cantidad')
    ).order_by('-total_vendido').first()

    # 2. Productos por surtir (ej. stock < 5)
    productos_por_surtir = Producto.objects.filter(stock__lt=5).order_by('stock')

    # 3. Clientes nuevos (registrados en la última semana)
    # Como no hay fecha de registro, mostramos los últimos 5 clientes creados.
    clientes_nuevos = Cliente.objects.all().order_by('-idCliente')[:5]

    # 4. Nuevos pedidos
    pedidos_nuevos = Pedido.objects.filter(fechaCreacion__gte=una_semana_atras).order_by('-fechaCreacion')

    context = {
        'producto_mas_vendido': producto_mas_vendido,
        'productos_por_surtir': productos_por_surtir,
        'clientes_nuevos': clientes_nuevos,
        'pedidos_nuevos': pedidos_nuevos,
    }
    return render(request, 'admin_dashboard.html', context)
# core/views.py

# Panel Admin
def admin_productos_view(request):
    return render(request, 'admin_productos.html')

def lista_admin_view(request):
    # Fetch only users with id_rol = 1 (assuming 1 is the admin role)
    admins = Usuario.objects.filter(id_rol=1).order_by('nombre')
    return render(request, 'lista_admin.html', {'admins': admins})

def admin_agregar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmar_password = request.POST.get('confirmar_password')

        if password != confirmar_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'admin_form.html', {'action': 'Agregar', 'input': request.POST})

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este correo electrónico ya está registrado.")
            return render(request, 'admin_form.html', {'action': 'Agregar', 'input': request.POST})

        try:
            with transaction.atomic():
                Usuario.objects.create(
                    nombre=nombre,
                    email=email,
                    password=make_password(password),
                    id_rol=1 # Set role to Admin
                )
            messages.success(request, "Administrador agregado exitosamente.")
            return redirect('lista_admin')
        except Exception as e:
            messages.error(request, f'Ocurrió un error: {e}')
            return render(request, 'admin_form.html', {'action': 'Agregar', 'input': request.POST})

    return render(request, 'admin_form.html', {'action': 'Agregar'})

def admin_editar_view(request, id):
    admin_user = get_object_or_404(Usuario, idUsuario=id, id_rol=1) # Ensure it's an admin
    if request.method == 'POST':
        admin_user.nombre = request.POST.get('nombre')
        admin_user.email = request.POST.get('email')
        new_password = request.POST.get('password')
        confirm_new_password = request.POST.get('confirmar_password')

        if new_password: # Only update password if provided
            if new_password != confirm_new_password:
                messages.error(request, "Las nuevas contraseñas no coinciden.")
                return render(request, 'admin_form.html', {'action': 'Editar', 'form_object': admin_user})
            admin_user.password = make_password(new_password)
        
        if Usuario.objects.filter(email=admin_user.email).exclude(idUsuario=admin_user.idUsuario).exists():
            messages.error(request, "Este correo electrónico ya está registrado por otro usuario.")
            return render(request, 'admin_form.html', {'action': 'Editar', 'form_object': admin_user})

        admin_user.save()
        messages.success(request, "Administrador actualizado exitosamente.")
        return redirect('lista_admin')
    return render(request, 'admin_form.html', {'form_object': admin_user, 'action': 'Editar'})

def admin_pedidos_view(request):
    return render(request, 'admin_pedidos.html')

def admin_usuarios_view(request):
    return render(request, 'admin_usuarios.html')

def admin_distribuidores_view(request):
    return render(request, 'admin_distribuidores.html')

def admin_repartidores_view(request):
    return render(request, 'admin_repartidores.html')

def admin_detalles_view(request):
    return render(request, 'admin_detalles.html')

def admin_eliminar_view(request, id):
    admin_to_delete = get_object_or_404(Usuario, idUsuario=id, id_rol=1)
    
    if request.session.get('usuario_id') == admin_to_delete.idUsuario:
        messages.error(request, "No puedes eliminar tu propia cuenta de administrador.")
        return redirect('lista_admin')

    if request.method == 'POST':
        admin_to_delete.delete()
        messages.success(request, "Administrador eliminado exitosamente.")
    return redirect('lista_admin')

# Panel Cliente



def lista_clientes_view(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'lista_clientes.html', context)




def cliente_editar_view(request, id):
    cliente = get_object_or_404(Cliente, idCliente=id)  # usa tu campo real

    if request.method == "POST":
        cliente.cedula = request.POST.get("cedula")
        cliente.nombre = request.POST.get("nombre")
        cliente.email = request.POST.get("email")
        cliente.direccion = request.POST.get("direccion")
        cliente.telefono = request.POST.get("telefono")
        cliente.save()
        return redirect("lista_clientes")  # vuelve al listado

    return render(request, "cliente_editar.html", {"cliente": cliente})


def cliente_eliminar_view(request, id):
    cliente = get_object_or_404(Cliente, idCliente=id)
    cliente.delete()
    return redirect("lista_clientes")


# Panel Distribuidores
  # Asegúrate de que el modelo esté bien importado

def lista_distribuidores_view(request):
    distribuidores = Distribuidor.objects.all()
    return render(request, 'lista_distribuidores.html', {
        'distribuidores': distribuidores
    })


def distribuidor_agregar_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombreDistribuidor")
        contacto = request.POST.get("contacto")
 
        if nombre and contacto:
            Distribuidor.objects.create(
                nombreDistribuidor=nombre,
                contacto=contacto
            )
            return redirect("lista_distribuidores")
 
    return render(request, 'agregar_distribuidor.html')

def distribuidor_editar_view(request, id):
    distribuidor = get_object_or_404(Distribuidor, idDistribuidor=id)
    if request.method == "POST":
        distribuidor.nombreDistribuidor = request.POST.get("nombreDistribuidor")
        distribuidor.contacto = request.POST.get("contacto")
        distribuidor.save()
        return redirect("lista_distribuidores")
    return render(request, "distribuidor_editar.html", {"distribuidor": distribuidor})


def distribuidor_eliminar_view(request, id):
    distribuidor = get_object_or_404(Distribuidor, idDistribuidor=id)
    distribuidor.delete()
    return redirect("lista_distribuidores")

# Panel Productos
def lista_productos_view(request):
    productos = Producto.objects.all().order_by('nombreProducto')
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = productos.filter(idCategoria_id=categoria_id)

    # La ruta de la plantilla se corrige aquí
    return render(request, 'lista_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada_id': int(categoria_id) if categoria_id else None
    })

def producto_agregar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreProducto')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        id_categoria = request.POST.get('idCategoria')
        id_subcategoria = request.POST.get('idSubcategoria')
        imagen = request.FILES.get('imagen')

        categoria = get_object_or_404(Categoria, idCategoria=id_categoria)
        subcategoria = None
        if id_subcategoria:
            subcategoria = get_object_or_404(Subcategoria, idSubcategoria=id_subcategoria)

        nuevo_producto = Producto.objects.create(
            nombreProducto=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            idCategoria=categoria,
            idSubcategoria=subcategoria,
            imagen=imagen
        )
        
        MovimientoProducto.objects.create(
            producto=nuevo_producto,
            tipo_movimiento='ENTRADA_INICIAL',
            precio_unitario=precio,
            cantidad=stock,
            stock_anterior=0,
            stock_nuevo=stock,
            descripcion='Creación del producto'
        )
        return redirect('lista_productos')

    categorias = Categoria.objects.prefetch_related('subcategoria_set').all()
    return render(request, 'productos_agregar.html', {
        'categorias': categorias
    })

def producto_editar_view(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    stock_original = producto.stock

    if request.method == 'POST':
        producto.nombreProducto = request.POST.get('nombreProducto')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        nuevo_stock = int(request.POST.get('stock'))

        if nuevo_stock != stock_original:
            diferencia = nuevo_stock - stock_original
            tipo_movimiento = 'AJUSTE_MANUAL_ENTRADA' if diferencia > 0 else 'AJUSTE_MANUAL_SALIDA'
            MovimientoProducto.objects.create(
                producto=producto,
                tipo_movimiento=tipo_movimiento,
                precio_unitario=producto.precio,
                cantidad=abs(diferencia),
                stock_anterior=stock_original,
                stock_nuevo=nuevo_stock,
                descripcion='Ajuste manual desde el panel de edición'
            )
        
        producto.stock = nuevo_stock
        producto.idCategoria = get_object_or_404(Categoria, idCategoria=request.POST.get('idCategoria'))
        
        id_subcategoria = request.POST.get('idSubcategoria')
        producto.idSubcategoria = get_object_or_404(Subcategoria, idSubcategoria=id_subcategoria) if id_subcategoria else None

        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        
        producto.save()
        return redirect('lista_productos')

    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    return render(request, 'productos_editar.html', {'producto': producto, 'categorias': categorias, 'subcategorias': subcategorias})

def producto_eliminar_view(request, id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, idProducto=id)
        producto.delete()
        messages.success(request, f"El producto '{producto.nombreProducto}' ha sido eliminado.")
    return redirect('lista_productos')

def movimientos_producto_view(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    movimientos = producto.movimientos.all().select_related('id_pedido')
    return render(request, 'movimientos_producto.html', {
        'producto': producto,
        'movimientos': movimientos
    })

def ajustar_stock_view(request, id):
    if request.method != 'POST':
        return redirect('movimientos_producto', id=id)

    producto = get_object_or_404(Producto, idProducto=id)
    
    try:
        cantidad = int(request.POST.get('cantidad'))
        tipo_ajuste = request.POST.get('tipo_ajuste')
        costo_unitario = request.POST.get('costo_unitario', 0)
        descripcion = request.POST.get('descripcion', 'Ajuste manual')

        if cantidad <= 0:
            messages.error(request, "La cantidad debe ser un número positivo.")
            return redirect('movimientos_producto', id=id)

        stock_anterior = producto.stock
        diferencia = cantidad if tipo_ajuste == 'entrada' else -cantidad
        stock_nuevo = stock_anterior + diferencia

        tipo_movimiento = 'AJUSTE_MANUAL_ENTRADA' if tipo_ajuste == 'entrada' else 'AJUSTE_MANUAL_SALIDA'

        costo_a_registrar = 0
        if tipo_ajuste == 'entrada':
            costo_a_registrar = float(costo_unitario) if costo_unitario else 0

        MovimientoProducto.objects.create(
            producto=producto, tipo_movimiento=tipo_movimiento, cantidad=cantidad,
            stock_anterior=stock_anterior, stock_nuevo=stock_nuevo, descripcion=descripcion,
            costo_unitario=costo_a_registrar, precio_unitario=producto.precio
        )
        producto.stock = stock_nuevo
        producto.save()
        messages.success(request, "El stock ha sido ajustado correctamente.")
    except (ValueError, TypeError):
        messages.error(request, "Por favor, introduce una cantidad válida.")
    
    return redirect('movimientos_producto', id=id)
# Panel Pedidos


def lista_pedidos_view(request):
    pedidos = Pedido.objects.all().order_by('-fechaCreacion') # Asegúrate que 'fechaCreacion' exista en el modelo Pedido
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def pedido_agregar_view(request):
    if request.method == 'POST':
        # Lógica para agregar un nuevo pedido
        return redirect('lista_pedidos')
    return render(request, 'pedidos_agregar.html')

def pedido_editar_view(request, id):
    pedido = get_object_or_404(Pedido, idPedido=id)
    repartidores_disponibles = Repartidor.objects.filter(estado_turno='Disponible')

    if request.method == 'POST':
        # Comprobar si se está asignando un repartidor
        if 'asignar_repartidor' in request.POST:
            repartidor_id = request.POST.get('repartidor_id')
            repartidor_a_asignar = get_object_or_404(Repartidor, idRepartidor=repartidor_id)
            pedido.idRepartidor = repartidor_a_asignar
            pedido.save()
            # Opcional: Cambiar estado del repartidor a "En Ruta"
            # repartidor_a_asignar.estado_turno = 'En Ruta'
            # repartidor_a_asignar.save()
        else: # Si no, se está actualizando el estado del pedido
            pedido.estado = request.POST.get('estado')
            pedido.save()
        return redirect('editar_pedido', id=id) # Recargar la misma página
    return render(request, 'pedidos_editar.html', {'pedido': pedido, 'repartidores': repartidores_disponibles})

def pedido_eliminar_view(request, id):
    pedido = get_object_or_404(Pedido, idPedido=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'pedidos_eliminar.html', {'pedido': pedido})


def pedido_detalle_view(request, id):
    pedido = get_object_or_404(Pedido, idPedido=id)
    detalles = DetallePedido.objects.filter(idPedido=id)
    return render(request, 'pedidos_detalle.html', {
        'pedido': pedido,
        'detalles': detalles
    })

# Panel Repartidores
def lista_repartidores_view(request):
    repartidores = Repartidor.objects.all().order_by('nombreRepartidor')
    # Pedidos que no tienen repartidor asignado y están en un estado que permite asignación
    # Consideramos pedidos con estado 'Pago Completo' o 'Pago Parcial' como asignables
    pedidos_pendientes = Pedido.objects.filter(
        idRepartidor__isnull=True,
        estado__in=['Pago Completo', 'Pago Parcial']
    ).order_by('fechaCreacion')

    # Pedidos que ya tienen un repartidor asignado
    pedidos_asignados = Pedido.objects.filter(
        idRepartidor__isnull=False
    ).select_related('idCliente', 'idRepartidor').order_by('-fechaCreacion')
    
    return render(request, 'lista_repartidores.html', {
        'repartidores': repartidores,
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_asignados': pedidos_asignados,
    })

def repartidor_agregar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreRepartidor')
        telefono = request.POST.get('telefono')
        estado = request.POST.get('estado_turno')
        
        # Validación básica
        if not nombre or not telefono or not estado:
            # Puedes añadir un mensaje de error aquí
            return render(request, 'repartidores_agregar.html', {'error_message': 'Todos los campos son obligatorios.'})

        Repartidor.objects.create(
            nombreRepartidor=nombre,
            telefono=telefono,
            estado_turno=estado
        )
        return redirect('lista_repartidores')
    return render(request, 'repartidores_agregar.html')

def repartidor_editar_view(request, id):
    repartidor = get_object_or_404(Repartidor, idRepartidor=id)
    if request.method == 'POST':
        repartidor.nombreRepartidor = request.POST.get('nombreRepartidor')
        repartidor.telefono = request.POST.get('telefono')
        repartidor.estado_turno = request.POST.get('estado_turno')
        
        # Validación básica
        if not repartidor.nombreRepartidor or not repartidor.telefono or not repartidor.estado_turno:
            return render(request, 'repartidores_editar.html', {'repartidor': repartidor, 'error_message': 'Todos los campos son obligatorios.'})
        repartidor.save()
        return redirect('lista_repartidores')
    return render(request, 'repartidores_editar.html', {'repartidor': repartidor})

def repartidor_eliminar_view(request, id):
    if request.method == 'POST':
        repartidor = get_object_or_404(Repartidor, idRepartidor=id)
        repartidor.delete()
    return redirect('lista_repartidores')

def asignar_pedido_repartidor_view(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        repartidor_id = request.POST.get('repartidor_id')

        pedido = get_object_or_404(Pedido, idPedido=pedido_id)
        repartidor = get_object_or_404(Repartidor, idRepartidor=repartidor_id)

        # Asignar el repartidor al pedido
        pedido.idRepartidor = repartidor
        pedido.save()

        # Opcional: Cambiar el estado del repartidor a "En Ruta" si se desea
        # repartidor.estado_turno = 'En Ruta'
        # repartidor.save()

        # messages.success(request, f"Pedido #{pedido.idPedido} asignado a {repartidor.nombreRepartidor}.")
        return redirect('lista_repartidores')
    return redirect('lista_repartidores') # Redirigir si se accede por GET

def desasignar_repartidor_view(request, id_pedido):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, idPedido=id_pedido)
        pedido.idRepartidor = None
        pedido.save()
        # messages.success(request, f"Se ha desasignado el repartidor del pedido #{id_pedido}.")
    return redirect('lista_repartidores')

def descargar_pedido_pdf_view(request, id_pedido):
    pedido = get_object_or_404(Pedido.objects.select_related('idCliente', 'idRepartidor'), idPedido=id_pedido)
    detalles = DetallePedido.objects.filter(idPedido=id_pedido).select_related('idProducto')

    # Nota: El campo 'quien recibe' no se está guardando en el modelo Pedido actualmente.
    # Para incluirlo, se debería añadir un campo al modelo Pedido y guardarlo durante el checkout.

    context = {
        'pedido': pedido,
        'detalles': detalles,
    }

    template_path = 'pedido_pdf_template.html'
    template = get_template(template_path)
    html = template.render(context)

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Ocurrió un error al generar el PDF.', status=500)

# Panel Detalles
def lista_detalles_view(request):   
    return render(request, 'lista_detalles.html')   




def logout_view(request):
    logout(request)                
    request.session.flush()       
    response = redirect('login')  
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Panel Categorías
def lista_categorias_view(request):
    categorias = Categoria.objects.annotate(num_productos=Count('producto')).order_by('nombreCategoria')
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def categoria_agregar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreCategoria')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')
        
        Categoria.objects.create(
            nombreCategoria=nombre, 
            descripcion=descripcion,
            imagen=imagen
        )
        return redirect('lista_categorias')
    return render(request, 'categoria_form.html', {'action': 'Agregar'})

def categoria_editar_view(request, id):
    categoria = get_object_or_404(Categoria, idCategoria=id)
    if request.method == 'POST':
        categoria.nombreCategoria = request.POST.get('nombreCategoria')
        categoria.descripcion = request.POST.get('descripcion')
        if 'imagen' in request.FILES:
            categoria.imagen = request.FILES['imagen']
        categoria.save()
        return redirect('lista_categorias')
    return render(request, 'categoria_form.html', {'form_object': categoria, 'action': 'Editar'})

def categoria_eliminar_view(request, id):
    if request.method == 'POST':
        categoria = get_object_or_404(Categoria, idCategoria=id)
        # Contar productos antes de eliminar
        if categoria.producto_set.count() > 0:
            print("No se puede eliminar: La categoría tiene productos asociados.") # Mensaje para depuración
        else:
            categoria.delete()
    return redirect('lista_categorias')

# Panel Subcategorías
def lista_subcategorias_view(request):
    subcategorias = Subcategoria.objects.all().select_related('categoria')
    return render(request, 'lista_subcategorias.html', {'subcategorias': subcategorias})

def subcategoria_agregar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreSubcategoria')
        id_categoria = request.POST.get('idCategoria')
        categoria_obj = get_object_or_404(Categoria, idCategoria=id_categoria)
        Subcategoria.objects.create(nombreSubcategoria=nombre, categoria=categoria_obj)
        return redirect('lista_subcategorias')
    categorias = Categoria.objects.all()
    return render(request, 'subcategoria_form.html', {'categorias': categorias, 'action': 'Agregar'})

def subcategoria_editar_view(request, id):
    subcategoria = get_object_or_404(Subcategoria, idSubcategoria=id)
    if request.method == 'POST':
        subcategoria.nombreSubcategoria = request.POST.get('nombreSubcategoria')
        id_categoria = request.POST.get('idCategoria')
        subcategoria.categoria = get_object_or_404(Categoria, idCategoria=id_categoria)
        subcategoria.save()
        return redirect('lista_subcategorias')
    categorias = Categoria.objects.all()
    return render(request, 'subcategoria_form.html', {'form_object': subcategoria, 'categorias': categorias, 'action': 'Editar'})

def subcategoria_eliminar_view(request, id):
    if request.method == 'POST':
        subcategoria = get_object_or_404(Subcategoria, idSubcategoria=id)
        subcategoria.delete()
    return redirect('lista_subcategorias')