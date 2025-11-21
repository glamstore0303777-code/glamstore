# Solución: Error de Integridad Referencial al Eliminar Clientes

## Problema Identificado

Al intentar eliminar un cliente desde el panel de administración, se producía el siguiente error:

```
IntegrityError: (1451, 'Cannot delete or update a parent row: a foreign key constraint fails (`glamstoredb`.`usuarios`, CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`))')
```

## Causa del Problema

El error ocurría porque:

1. La tabla `usuarios` tiene una clave foránea (`idCliente`) que referencia la tabla `clientes`
2. La función `cliente_eliminar_view` intentaba eliminar directamente el cliente sin manejar las referencias
3. La base de datos tiene restricciones de integridad referencial que impiden eliminar un registro padre si existen registros hijos que lo referencian

## Solución Implementada

### 1. Modificación de la Vista de Eliminación

Se actualizó la función `cliente_eliminar_view` en `core/Gestion_admin/views.py`:

```python
def cliente_eliminar_view(request, id):
    cliente = get_object_or_404(Cliente, idCliente=id)
    
    try:
        with transaction.atomic():
            # Primero, actualizar los usuarios relacionados para evitar el error de integridad referencial
            # Establecer idCliente a NULL para todos los usuarios que referencian este cliente
            usuarios_actualizados = Usuario.objects.filter(idCliente=id).update(idCliente=None)
            
            # Verificar si hay pedidos asociados al cliente
            pedidos_count = Pedido.objects.filter(idCliente=id).count()
            
            if pedidos_count > 0:
                messages.warning(request, f"El cliente {cliente.nombre} tiene {pedidos_count} pedido(s) asociado(s). Se eliminarán junto con el cliente.")
            
            # Ahora podemos eliminar el cliente de forma segura
            # Los pedidos se eliminarán automáticamente por la restricción de la base de datos
            cliente.delete()
            
            mensaje = f"Cliente {cliente.nombre} eliminado correctamente."
            if usuarios_actualizados > 0:
                mensaje += f" Se desvincularon {usuarios_actualizados} usuario(s) asociado(s)."
            
            messages.success(request, mensaje)
            
    except Exception as e:
        messages.error(request, f"Error al eliminar el cliente: {str(e)}")
    
    return redirect("lista_clientes")
```

### 2. Características de la Solución

- **Transacción Atómica**: Toda la operación se ejecuta dentro de una transacción para garantizar consistencia
- **Manejo de Usuarios**: Los usuarios relacionados se desvincular del cliente (idCliente = NULL) en lugar de eliminarse
- **Información de Pedidos**: Se informa al administrador si el cliente tiene pedidos asociados
- **Manejo de Errores**: Se capturan y muestran errores de forma amigable
- **Mensajes Informativos**: Se proporciona feedback detallado sobre la operación

### 3. Flujo de Eliminación

1. **Verificación**: Se verifica que el cliente existe
2. **Desvinculación**: Se actualizan los usuarios para quitar la referencia al cliente
3. **Información**: Se cuenta y notifica sobre pedidos asociados
4. **Eliminación**: Se elimina el cliente (los pedidos se eliminan automáticamente por CASCADE)
5. **Confirmación**: Se muestra mensaje de éxito con detalles de la operación

## Archivos Modificados

- `core/Gestion_admin/views.py`: Función `cliente_eliminar_view` actualizada

## Archivos Creados

- `test_client_deletion.py`: Script de prueba para verificar el proceso de eliminación
- `SOLUCION_ERROR_ELIMINACION_CLIENTE.md`: Este documento de documentación

## Pruebas

Para probar la solución:

1. **Prueba Manual**: Intentar eliminar un cliente desde el panel de administración
2. **Script de Prueba**: Ejecutar `python test_client_deletion.py <client_id>` para simular el proceso

## Consideraciones Importantes

- Los usuarios no se eliminan, solo se desvinculan del cliente
- Los pedidos del cliente se eliminan automáticamente (comportamiento CASCADE)
- La operación es atómica, por lo que si algo falla, no se realizan cambios parciales
- Se proporciona feedback detallado al administrador sobre lo que ocurrió

## Estado

✅ **SOLUCIONADO** - El error de integridad referencial ha sido corregido y la eliminación de clientes funciona correctamente.