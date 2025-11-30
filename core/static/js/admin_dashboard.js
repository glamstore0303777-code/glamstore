// Datos para los gráficos
const productosData = {
  labels: [],
  datasets: [{
    label: 'Unidades Vendidas',
    data: [],
    backgroundColor: ['#f48fb1', '#ec407a', '#e91e63', '#c2185b', '#ad1457'],
    borderColor: '#fff',
    borderWidth: 2
  }]
};

const clientesData = {
  labels: ['Semana Pasada', 'Esta Semana'],
  datasets: [{
    label: 'Nuevos Clientes',
    data: [0, 0],
    backgroundColor: ['#f8bbd0', '#f48fb1'],
    borderColor: '#c2185b',
    borderWidth: 2
  }]
};

const categoriasData = {
  labels: [],
  datasets: [{
    label: 'Ventas ($)',
    data: [],
    backgroundColor: ['#fce4ec', '#f8bbd0', '#f48fb1', '#ec407a', '#e91e63'],
    borderColor: '#c2185b',
    borderWidth: 1
  }]
};

// Configuración de gráficos
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        padding: 20,
        usePointStyle: true
      }
    }
  }
};

// Crear gráficos
document.addEventListener('DOMContentLoaded', function() {
  // Gráfico de productos más vendidos
  const productosCtx = document.getElementById('productosChart');
  if (productosCtx) {
    new Chart(productosCtx.getContext('2d'), {
      type: 'doughnut',
      data: productosData,
      options: chartOptions
    });
  }

  // Gráfico de clientes por semana
  const clientesCtx = document.getElementById('clientesChart');
  if (clientesCtx) {
    new Chart(clientesCtx.getContext('2d'), {
      type: 'bar',
      data: clientesData,
      options: {
        ...chartOptions,
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              stepSize: 1
            }
          }
        }
      }
    });
  }

  // Gráfico de ventas por categoría
  const categoriasCtx = document.getElementById('categoriasChart');
  if (categoriasCtx) {
    new Chart(categoriasCtx.getContext('2d'), {
      type: 'line',
      data: categoriasData,
      options: {
        ...chartOptions,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }
});
