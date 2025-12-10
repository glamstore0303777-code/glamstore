/* ============================================
   FUNCIONES GLOBALES DEL ADMIN
   ============================================ */

// Función para confirmar acciones
function confirmarAccion(mensaje) {
  return confirm(mensaje);
}

// Función para mostrar alertas
function mostrarAlerta(mensaje, tipo = 'info') {
  const alertDiv = document.createElement('div');
  alertDiv.className = `alert alert-${tipo}`;
  alertDiv.textContent = mensaje;
  alertDiv.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 1rem 1.5rem;
    border-radius: 10px;
    z-index: 10000;
    animation: slideIn 0.3s ease-out;
  `;

  if (tipo === 'success') {
    alertDiv.style.background = 'linear-gradient(135deg, #4caf50 0%, #45a049 100%)';
    alertDiv.style.color = 'white';
  } else if (tipo === 'error') {
    alertDiv.style.background = 'linear-gradient(135deg, #f44336 0%, #e53935 100%)';
    alertDiv.style.color = 'white';
  } else if (tipo === 'warning') {
    alertDiv.style.background = 'linear-gradient(135deg, #ff9800 0%, #f57c00 100%)';
    alertDiv.style.color = 'white';
  } else {
    alertDiv.style.background = 'linear-gradient(135deg, #2196f3 0%, #1976d2 100%)';
    alertDiv.style.color = 'white';
  }

  document.body.appendChild(alertDiv);

  setTimeout(() => {
    alertDiv.remove();
  }, 3000);
}

// Función para formatear moneda
function formatearMoneda(valor) {
  return new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(valor);
}

// Función para formatear fecha
function formatearFecha(fecha) {
  const opciones = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  };
  return new Date(fecha).toLocaleDateString('es-CO', opciones);
}

// Función para validar formulario
function validarFormulario(formId) {
  const form = document.getElementById(formId);
  if (!form) return false;

  const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
  let esValido = true;

  inputs.forEach(input => {
    if (!input.value.trim()) {
      input.style.borderColor = '#f44336';
      esValido = false;
    } else {
      input.style.borderColor = '#d8b4fe';
    }
  });

  return esValido;
}

// Función para limpiar formulario
function limpiarFormulario(formId) {
  const form = document.getElementById(formId);
  if (form) {
    form.reset();
    form.querySelectorAll('input, select, textarea').forEach(input => {
      input.style.borderColor = '#d8b4fe';
    });
  }
}

// Función para buscar en tabla
function buscarEnTabla(inputId, tableId) {
  const input = document.getElementById(inputId);
  const table = document.getElementById(tableId);

  if (!input || !table) return;

  const filtro = input.value.toUpperCase();
  const filas = table.getElementsByTagName('tr');

  for (let i = 1; i < filas.length; i++) {
    const fila = filas[i];
    const texto = fila.textContent || fila.innerText;

    if (texto.toUpperCase().indexOf(filtro) > -1) {
      fila.style.display = '';
    } else {
      fila.style.display = 'none';
    }
  }
}

// Función para ordenar tabla
function ordenarTabla(tableId, columnIndex, tipo = 'string') {
  const table = document.getElementById(tableId);
  if (!table) return;

  const tbody = table.querySelector('tbody');
  const filas = Array.from(tbody.querySelectorAll('tr'));

  filas.sort((a, b) => {
    const aValor = a.cells[columnIndex].textContent.trim();
    const bValor = b.cells[columnIndex].textContent.trim();

    if (tipo === 'number') {
      return parseFloat(aValor) - parseFloat(bValor);
    } else if (tipo === 'date') {
      return new Date(aValor) - new Date(bValor);
    } else {
      return aValor.localeCompare(bValor);
    }
  });

  filas.forEach(fila => tbody.appendChild(fila));
}

// Función para seleccionar/deseleccionar todos los checkboxes
function seleccionarTodos(checkboxId, containerSelector) {
  const checkbox = document.getElementById(checkboxId);
  const checkboxes = document.querySelectorAll(containerSelector);

  if (checkbox) {
    checkboxes.forEach(cb => {
      cb.checked = checkbox.checked;
    });
  }
}

// Función para contar checkboxes seleccionados
function contarSeleccionados(selector) {
  return document.querySelectorAll(selector + ':checked').length;
}

// Función para obtener valores de checkboxes seleccionados
function obtenerSeleccionados(selector) {
  return Array.from(document.querySelectorAll(selector + ':checked')).map(cb => cb.value);
}

// Función para mostrar/ocultar elemento
function alternarVisibilidad(elementId) {
  const elemento = document.getElementById(elementId);
  if (elemento) {
    elemento.style.display = elemento.style.display === 'none' ? 'block' : 'none';
  }
}

// Función para copiar al portapapeles
function copiarAlPortapapeles(texto) {
  navigator.clipboard.writeText(texto).then(() => {
    mostrarAlerta('Copiado al portapapeles', 'success');
  }).catch(() => {
    mostrarAlerta('Error al copiar', 'error');
  });
}

// Función para descargar archivo
function descargarArchivo(url, nombreArchivo) {
  const link = document.createElement('a');
  link.href = url;
  link.download = nombreArchivo;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// Función para hacer petición AJAX
function hacerPeticion(url, metodo = 'GET', datos = null) {
  return fetch(url, {
    method: metodo,
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': obtenerCSRFToken()
    },
    body: datos ? JSON.stringify(datos) : null
  }).then(response => response.json());
}

// Función para obtener token CSRF
function obtenerCSRFToken() {
  const nombre = 'csrftoken';
  let tokenValor = null;

  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, nombre.length + 1) === (nombre + '=')) {
        tokenValor = decodeURIComponent(cookie.substring(nombre.length + 1));
        break;
      }
    }
  }

  return tokenValor;
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
  // Agregar estilos de animación
  const style = document.createElement('style');
  style.textContent = `
    @keyframes slideIn {
      from {
        transform: translateX(400px);
        opacity: 0;
      }
      to {
        transform: translateX(0);
        opacity: 1;
      }
    }

    .alert {
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      border-radius: 10px;
    }
  `;
  document.head.appendChild(style);
});
