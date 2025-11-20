with open('core/Clientes/seguimiento_pedidos/checkout.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Eliminar el campo "Tipo de documento" y cambiar "Documento" por "Cédula"
old_documento_section = '''        <label>Tipo de documento</label>
        <select name="tipo_documento" required>
          <option value="">Elige una opción...</option>
          <option value="CC">Cédula</option>
          <option value="TI">Tarjeta de Identidad</option>
          <option value="CE">Cédula Extranjera</option>
        </select>

        <label>Documento</label>
        <input type="text" name="documento" required>'''

new_documento_section = '''        <label>Cédula</label>
        <input type="text" name="cedula" required placeholder="Número de cédula">'''

content = content.replace(old_documento_section, new_documento_section)

# 2. Agregar campo dinámico de Localidad/Comuna después del campo Municipio
old_municipio_section = '''        <label>Municipio</label>
        <select name="municipio" required>
          <option value="">Selecciona tu municipio</option>
          <option value="Soacha">Soacha</option>
          <option value="Bogotá">Bogotá</option>
        </select>

        <label>Dirección</label>'''

new_municipio_section = '''        <label>Municipio</label>
        <select name="municipio" id="municipio" required>
          <option value="">Selecciona tu municipio</option>
          <option value="Soacha">Soacha</option>
          <option value="Bogotá">Bogotá</option>
        </select>

        <label id="label-localidad-comuna" style="display: none;">Localidad/Comuna</label>
        <select name="localidad_comuna" id="localidad-comuna" style="display: none;">
          <option value="">Selecciona...</option>
        </select>

        <label>Dirección</label>'''

content = content.replace(old_municipio_section, new_municipio_section)

# 3. Agregar JavaScript para manejar el cambio dinámico de localidades/comunas
old_script_start = '''  <!-- JS para mostrar secciones progresivamente -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {'''

new_script_start = '''  <!-- JS para mostrar secciones progresivamente -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Localidades de Bogotá
      const localidadesBogota = [
        'Usaquén', 'Chapinero', 'Santa Fe', 'San Cristóbal', 'Usme',
        'Tunjuelito', 'Bosa', 'Kennedy', 'Fontibón', 'Engativá',
        'Suba', 'Barrios Unidos', 'Teusaquillo', 'Los Mártires', 'Antonio Nariño',
        'Puente Aranda', 'La Candelaria', 'Rafael Uribe Uribe', 'Ciudad Bolívar', 'Sumapaz'
      ];

      // Comunas de Soacha
      const comunasSoacha = [
        'Comuna 1 - Compartir',
        'Comuna 2 - La Despensa',
        'Comuna 3 - Soacha Centro',
        'Comuna 4 - Cazucá',
        'Comuna 5 - San Mateo',
        'Comuna 6 - San Humberto'
      ];

      const municipioSelect = document.getElementById('municipio');
      const localidadComunaSelect = document.getElementById('localidad-comuna');
      const labelLocalidadComuna = document.getElementById('label-localidad-comuna');

      municipioSelect.addEventListener('change', function() {
        const municipio = this.value;
        
        // Limpiar opciones anteriores
        localidadComunaSelect.innerHTML = '<option value="">Selecciona...</option>';
        
        if (municipio === 'Bogotá') {
          // Mostrar campo y cambiar label
          labelLocalidadComuna.textContent = 'Localidad';
          labelLocalidadComuna.style.display = 'block';
          localidadComunaSelect.style.display = 'block';
          localidadComunaSelect.required = true;
          
          // Agregar localidades de Bogotá
          localidadesBogota.forEach(localidad => {
            const option = document.createElement('option');
            option.value = localidad;
            option.textContent = localidad;
            localidadComunaSelect.appendChild(option);
          });
        } else if (municipio === 'Soacha') {
          // Mostrar campo y cambiar label
          labelLocalidadComuna.textContent = 'Comuna';
          labelLocalidadComuna.style.display = 'block';
          localidadComunaSelect.style.display = 'block';
          localidadComunaSelect.required = true;
          
          // Agregar comunas de Soacha
          comunasSoacha.forEach(comuna => {
            const option = document.createElement('option');
            option.value = comuna;
            option.textContent = comuna;
            localidadComunaSelect.appendChild(option);
          });
        } else {
          // Ocultar campo si no hay municipio seleccionado
          labelLocalidadComuna.style.display = 'none';
          localidadComunaSelect.style.display = 'none';
          localidadComunaSelect.required = false;
        }
      });

      // Código existente para métodos de pago'''

content = content.replace(old_script_start, new_script_start)

with open('core/Clientes/seguimiento_pedidos/checkout.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Checkout actualizado exitosamente!")
print("- Eliminado campo 'Tipo de documento'")
print("- Campo 'Documento' cambiado a 'Cedula'")
print("- Agregado selector dinamico de Localidad/Comuna")
print("- Bogota: 20 localidades")
print("- Soacha: 6 comunas")
