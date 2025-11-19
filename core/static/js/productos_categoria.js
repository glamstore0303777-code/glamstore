document.addEventListener('DOMContentLoaded', () => {
  const formularios = document.querySelectorAll('.form-agregar');

  formularios.forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const formData = new FormData(form);
      const productoId = form.dataset.producto;
      const cantidadSeleccionada = parseInt(formData.get('cantidad'));

      try {
        const response = await fetch(form.action, {
          method: 'POST',
          headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
          },
          body: formData,
        });

        if (response.ok) {
          // Mostrar botón "Ver carrito"
          const botonCarrito = document.getElementById(`ver-carrito-${productoId}`);
          if (botonCarrito) {
            botonCarrito.style.display = 'block';
            botonCarrito.classList.add('animado');
          }

          // Mostrar mensaje pastel-glam
          mostrarMensaje(form, 'Producto agregado al carrito ✨', false);

          // Desactivar opción si se alcanzó el stock
          const select = document.getElementById(`cantidad-${productoId}`);
          if (select) {
            const opciones = select.options.length;
            if (cantidadSeleccionada >= opciones) {
              form.remove(); // o mostrar mensaje de agotado
              const agotado = document.createElement('p');
              agotado.textContent = 'Stock agotado o ya en carrito';
              agotado.className = 'agotado';
              form.parentElement.appendChild(agotado);
            }
          }
        } else {
          mostrarMensaje(form, 'Error al agregar al carrito', true);
        }
      } catch (error) {
        console.error('Error de red:', error);
        mostrarMensaje(form, 'Error de conexión', true);
      }
    });
  });

  function mostrarMensaje(form, texto, esError = false) {
    const mensaje = document.createElement('div');
    mensaje.textContent = texto;
    mensaje.className = esError ? 'mensaje-error' : 'mensaje-exito';
    form.appendChild(mensaje);

    setTimeout(() => {
      mensaje.remove();
    }, 3000);
  }
});