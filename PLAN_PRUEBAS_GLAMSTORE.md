# Plan de Pruebas de Software - Glam Store

## Documento: Plan de Pruebas de Software

**Proyecto:** Glam Store - Sistema de Tienda en Línea  
**Responsable de Pruebas:** Equipo QA  
**Fecha de inicio de pruebas:** 15/12/2025  
**Fecha estimada de finalización:** 30/12/2025  

---

## 1. Identificación del Proyecto

**Nombre del proyecto:** Glam Store  
**Descripción:** Sistema web de comercio electrónico para la venta de productos de belleza y cosméticos. Permite a clientes registrarse, navegar productos, realizar compras, hacer seguimiento de pedidos y calificar entregas. Incluye panel administrativo para gestión de inventario, pedidos, repartidores y reportes.

**Tecnología:** 
- Backend: Python (Django)
- Base de datos: PostgreSQL
- Frontend: HTML, CSS, JavaScript
- Hosting: Render (producción)

**Módulos principales:**
- Autenticación y gestión de usuarios
- Catálogo de productos
- Carrito de compras
- Gestión de pedidos
- Seguimiento de entregas
- Panel administrativo
- Gestión de inventario
- Reportes y análisis

---

## 2. Objetivo del Plan de Pruebas

El principal objetivo del Plan de Pruebas es garantizar que Glam Store cumpla con todos los requerimientos establecidos, tanto funcionales como no funcionales, antes de su implementación en producción.

**Objetivos específicos:**

- **Verificar funcionalidad:** Confirmar que todas las operaciones (registro, compra, seguimiento, etc.) se ejecuten correctamente
- **Evaluar confiabilidad:** Asegurar comportamiento estable ante datos incorrectos o acciones inesperadas
- **Garantizar usabilidad:** Comprobar que la interfaz sea amigable e intuitiva
- **Medir rendimiento:** Analizar tiempos de respuesta y capacidad del sistema
- **Verificar seguridad:** Comprobar manejo seguro de datos sensibles y control de acceso
- **Validar integración:** Asegurar que todos los módulos funcionen correctamente en conjunto

---

## 3. Alcance de las Pruebas

### Pruebas Funcionales

**Módulo de Autenticación:**
- Registro de nuevos usuarios
- Inicio de sesión con credenciales válidas e inválidas
- Recuperación de contraseña
- Cierre de sesión
- Control de acceso por roles (Cliente, Admin, Repartidor)

**Módulo de Productos:**
- Visualización de catálogo
- Búsqueda y filtrado de productos
- Visualización de detalles del producto
- Gestión de inventario (Admin)
- Cálculo de precio de venta

**Módulo de Carrito:**
- Agregar productos al carrito
- Actualizar cantidades
- Eliminar productos
- Vaciar carrito
- Cálculo de totales con IVA

**Módulo de Pedidos:**
- Crear nuevo pedido
- Visualizar historial de pedidos
- Seguimiento de estado del pedido
- Confirmación de recepción
- Calificación de entrega
- Reporte de problemas

**Módulo de Repartidores:**
- Asignación automática de pedidos
- Visualización de ruta de entregas
- Actualización de estado de entrega
- Generación de PDF de ruta

**Módulo de Reportes:**
- Generación de reportes de ventas
- Exportación a PDF y Excel
- Filtrado por fechas
- Análisis de datos

### Pruebas de Interfaz de Usuario (UI)

- Disposición y coherencia visual
- Legibilidad de textos
- Funcionalidad de botones y enlaces
- Adaptabilidad a diferentes tamaños de pantalla
- Compatibilidad con navegadores (Chrome, Firefox, Safari, Edge)

### Pruebas de Rendimiento

- Tiempo de carga de páginas (< 3 segundos)
- Tiempo de respuesta de API
- Capacidad de manejo de múltiples usuarios simultáneos
- Eficiencia de consultas a base de datos

### Pruebas de Seguridad

- Validación de credenciales
- Protección contra accesos no autorizados
- Manejo seguro de datos personales
- Validación de entrada (prevención de inyección SQL)
- Cifrado de contraseñas
- Control de sesiones

### Pruebas de Integración

- Integración entre módulos
- Sincronización de datos entre cliente y servidor
- Integración con servicio de email (Brevo)
- Integración con base de datos

**Alcance NO incluye:**
- Pruebas de compatibilidad con aplicaciones móviles nativas
- Pruebas de carga extrema (> 10,000 usuarios simultáneos)
- Pruebas de compatibilidad con navegadores obsoletos

---

## 4. Tipos de Pruebas

### Pruebas Unitarias
Validan el funcionamiento de componentes individuales (funciones, métodos, servicios) del sistema.

### Pruebas de Integración
Evalúan la interacción entre módulos, asegurando que los datos fluyan correctamente entre ellos.

### Pruebas del Sistema
Comprueban el comportamiento global del software como una unidad completa.

### Pruebas de Aceptación
Se realizan con el cliente para confirmar que el sistema cumple con las expectativas establecidas.

### Pruebas de Regresión
Se ejecutan cuando se realizan cambios en el código para garantizar que no generen nuevos errores.

### Pruebas de Caja Negra
Evalúan entradas y salidas sin analizar la estructura interna del código.

### Pruebas de Caja Blanca
Analizan la lógica interna del programa, estructuras de control y rutas del código.

### Pruebas de Humo (Smoke Testing)
Validación rápida de funcionalidades críticas después de cada deploy.

---

## 5. Criterios de Entrada

Antes de iniciar la ejecución de pruebas, deben cumplirse:

- ✅ Código fuente completo, compilado y libre de errores de sintaxis
- ✅ Todos los módulos integrados correctamente
- ✅ Base de datos configurada con datos de prueba representativos
- ✅ Documentación de requisitos validada y aprobada
- ✅ Entorno de pruebas completamente operativo (servidor, BD, navegadores)
- ✅ Herramientas de gestión de incidencias listas
- ✅ Acceso a credenciales de prueba
- ✅ Documentación de API disponible

---

## 6. Criterios de Salida

El proceso de pruebas se considerará finalizado cuando:

- ✅ Todos los casos de prueba hayan sido ejecutados
- ✅ Errores críticos o bloqueantes hayan sido corregidos y verificados
- ✅ Informe final de pruebas generado con resultados
- ✅ Cliente haya validado el sistema mediante pruebas de aceptación
- ✅ No existan errores abiertos que impidan funcionamiento correcto
- ✅ Cobertura de pruebas ≥ 80%
- ✅ Tiempo de respuesta < 3 segundos en 95% de transacciones
- ✅ Cero vulnerabilidades críticas de seguridad

---

## 7. Recursos Necesarios

### Equipo Humano

- **QA Lead:** Coordinación y supervisión de pruebas
- **QA Testers:** 2-3 personas para ejecución de pruebas funcionales
- **QA Automation:** 1 persona para automatización de pruebas
- **Desarrolladores:** Disponibles para corrección de defectos

### Recursos Tecnológicos

**Hardware:**
- Computadores con Windows 10/11 o macOS
- Mínimo 8GB RAM, 256GB SSD
- Conexión a internet estable

**Software:**
- Navegadores: Chrome, Firefox, Safari, Edge (versiones actuales)
- Herramientas de pruebas: Selenium, Postman, JMeter
- Herramientas de gestión: Jira, Trello
- Base de datos: PostgreSQL
- Servidor: Render (staging)

**Entorno:**
- Servidor de pruebas (staging) con configuración similar a producción
- Base de datos de pruebas con datos representativos
- Acceso a API de Brevo para pruebas de email

### Recursos Documentales

- Historias de usuario
- Requisitos funcionales y no funcionales
- Casos de uso
- Manual de usuario
- Documentación de API
- Diagrama de flujos

---

## 8. Casos de Prueba

### Módulo de Autenticación

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-001 | Registro de usuario | Registrar nuevo usuario con datos válidos | Email, nombre, contraseña | Usuario creado, email de confirmación enviado | Pendiente |
| CP-002 | Registro duplicado | Intentar registrar con email existente | Email duplicado | Mensaje de error: "Email ya registrado" | Pendiente |
| CP-003 | Inicio de sesión válido | Iniciar sesión con credenciales correctas | Email y contraseña válidos | Acceso autorizado, redirección a tienda | Pendiente |
| CP-004 | Inicio de sesión inválido | Iniciar sesión con contraseña incorrecta | Email válido, contraseña incorrecta | Mensaje de error: "Credenciales inválidas" | Pendiente |
| CP-005 | Recuperar contraseña | Solicitar recuperación de contraseña | Email registrado | Email con enlace de recuperación enviado | Pendiente |
| CP-006 | Cierre de sesión | Cerrar sesión correctamente | Clic en "Cerrar sesión" | Redirección a login, sesión terminada | Pendiente |
| CP-007 | Control de acceso - Cliente | Cliente accede solo a funciones permitidas | Usuario cliente autenticado | No puede acceder a panel admin | Pendiente |
| CP-008 | Control de acceso - Admin | Admin accede a todas las funciones | Usuario admin autenticado | Acceso a panel administrativo completo | Pendiente |

### Módulo de Productos

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-009 | Visualizar catálogo | Ver lista de productos disponibles | Acceso a tienda | Se muestran productos con imagen, nombre, precio | Pendiente |
| CP-010 | Buscar producto | Buscar producto por nombre | Término de búsqueda | Se muestran productos coincidentes | Pendiente |
| CP-011 | Filtrar por categoría | Filtrar productos por categoría | Seleccionar categoría | Se muestran solo productos de esa categoría | Pendiente |
| CP-012 | Ver detalle producto | Ver información completa del producto | Clic en producto | Se muestra descripción, precio, stock, calificaciones | Pendiente |
| CP-013 | Precio de venta calculado | Verificar que precio_venta se calcula correctamente | Crear nuevo producto | precio_venta = costo * (1 + margen) | Pendiente |
| CP-014 | Stock actualizado | Verificar que stock se actualiza al crear lote | Crear lote de entrada | Stock del producto aumenta | Pendiente |

### Módulo de Carrito

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-015 | Agregar al carrito | Agregar producto al carrito | Producto, cantidad | Producto aparece en carrito | Pendiente |
| CP-016 | Actualizar cantidad | Cambiar cantidad de producto en carrito | Nueva cantidad | Cantidad actualizada, total recalculado | Pendiente |
| CP-017 | Eliminar del carrito | Eliminar producto del carrito | Clic en eliminar | Producto removido del carrito | Pendiente |
| CP-018 | Vaciar carrito | Vaciar todos los productos | Clic en "Vaciar carrito" | Carrito vacío | Pendiente |
| CP-019 | Cálculo de totales | Verificar cálculo correcto de subtotal, IVA, total | Productos en carrito | Subtotal + IVA = Total correcto | Pendiente |
| CP-020 | Costo de envío | Verificar que costo de envío se suma correctamente | Carrito con productos | Total incluye $10.000 de envío | Pendiente |

### Módulo de Pedidos

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-021 | Crear pedido | Crear nuevo pedido desde carrito | Carrito con productos | Pedido creado, estado "Confirmado" | Pendiente |
| CP-022 | Confirmación de recepción | Cliente confirma recepción de pedido | Pedido en estado "En Camino" | Pedido cambia a "Completado" | Pendiente |
| CP-023 | Calificar entrega | Cliente califica entrega con estrellas | Pedido entregado, calificación 1-5 | Calificación guardada, ConfirmacionEntrega creada | Pendiente |
| CP-024 | Reportar problema | Cliente reporta problema con entrega | Descripción del problema, foto | NotificacionProblema creada, admin notificado | Pendiente |
| CP-025 | Ver historial pedidos | Ver lista de pedidos del cliente | Cliente autenticado | Se muestran todos los pedidos del cliente | Pendiente |
| CP-026 | Seguimiento de pedido | Ver estado actual del pedido | Pedido ID | Se muestra estado, repartidor, fecha estimada | Pendiente |

### Módulo de Repartidores

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-027 | Asignación automática | Asignar pedidos a repartidores automáticamente | Pedidos sin asignar | Pedidos distribuidos equitativamente | Pendiente |
| CP-028 | Generar PDF ruta | Generar PDF con ruta de entregas | Repartidor, fecha | PDF descargado con información de pedidos | Pendiente |
| CP-029 | Enviar plan semanal | Enviar plan semanal a repartidor por email | Repartidor con pedidos | Email recibido con detalles de entregas | Pendiente |
| CP-030 | Actualizar estado entrega | Repartidor actualiza estado de entrega | Nuevo estado | Estado del pedido actualizado | Pendiente |

### Módulo de Reportes

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-031 | Generar reporte PDF | Generar reporte de ventas en PDF | Rango de fechas | PDF descargado correctamente | Pendiente |
| CP-032 | Generar reporte Excel | Generar reporte de ventas en Excel | Rango de fechas | Excel descargado correctamente | Pendiente |
| CP-033 | Filtrar por fechas | Filtrar datos de reporte por rango de fechas | Fecha inicio, fecha fin | Se muestran solo datos del rango | Pendiente |
| CP-034 | Datos completos | Verificar que reporte incluye todos los datos | Generar reporte | Incluye: pedidos, clientes, montos, estados | Pendiente |

### Pruebas de Rendimiento

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-035 | Tiempo de carga tienda | Verificar tiempo de carga de página principal | Acceso a tienda | Carga en < 3 segundos | Pendiente |
| CP-036 | Tiempo de búsqueda | Verificar tiempo de respuesta de búsqueda | Búsqueda de producto | Resultados en < 2 segundos | Pendiente |
| CP-037 | Tiempo de checkout | Verificar tiempo de proceso de compra | Completar compra | Confirmación en < 5 segundos | Pendiente |
| CP-038 | Usuarios simultáneos | Verificar sistema con 100 usuarios simultáneos | Carga de 100 usuarios | Sistema responde sin errores | Pendiente |

### Pruebas de Seguridad

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-039 | Inyección SQL | Intentar inyección SQL en búsqueda | Entrada maliciosa: `'; DROP TABLE--` | Entrada sanitizada, sin error | Pendiente |
| CP-040 | XSS | Intentar inyección de script | Script en campo de entrada | Script no se ejecuta, se muestra como texto | Pendiente |
| CP-041 | CSRF | Verificar protección CSRF | Token CSRF en formularios | Solicitudes sin token rechazadas | Pendiente |
| CP-042 | Acceso no autorizado | Intentar acceder a recursos sin permiso | URL directa a recurso protegido | Redirección a login | Pendiente |
| CP-043 | Cifrado de contraseña | Verificar que contraseñas están cifradas | Revisar BD | Contraseñas no están en texto plano | Pendiente |

### Pruebas de Interfaz

| ID | Nombre | Descripción | Entrada | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| CP-044 | Responsive mobile | Verificar diseño en dispositivos móviles | Acceso desde móvil | Diseño se adapta correctamente | Pendiente |
| CP-045 | Responsive tablet | Verificar diseño en tablets | Acceso desde tablet | Diseño se adapta correctamente | Pendiente |
| CP-046 | Compatibilidad Chrome | Verificar en Chrome | Abrir en Chrome | Funciona correctamente | Pendiente |
| CP-047 | Compatibilidad Firefox | Verificar en Firefox | Abrir en Firefox | Funciona correctamente | Pendiente |
| CP-048 | Compatibilidad Safari | Verificar en Safari | Abrir en Safari | Funciona correctamente | Pendiente |

---

## 9. Riesgos Identificados

| Riesgo | Descripción | Impacto | Probabilidad | Plan de Mitigación |
|---|---|---|---|---|
| Retraso en correcciones | Desarrolladores no corrigen defectos a tiempo | Alto | Medio | Establecer SLA de 24 horas para correcciones críticas |
| Cambios de requisitos | Cliente modifica funciones durante pruebas | Alto | Alto | Mantener control de versiones, comunicación semanal |
| Fallos en BD | Errores de configuración o caídas de BD | Alto | Bajo | Tener BD de respaldo, backups automáticos diarios |
| Pérdida de datos | Corrupción de datos de prueba | Alto | Bajo | Realizar respaldos antes de cada ciclo de pruebas |
| Problemas de rendimiento | Sistema lento bajo carga | Medio | Medio | Realizar pruebas de carga temprano, optimizar queries |
| Incompatibilidad navegadores | Funcionalidad no funciona en ciertos navegadores | Medio | Bajo | Probar en múltiples navegadores desde inicio |
| Falta de comunicación | Descoordinación entre QA y desarrollo | Medio | Medio | Usar Jira, reuniones diarias de 15 minutos |
| Limitaciones de hardware | Equipos lentos afectan ejecución | Bajo | Bajo | Usar equipos con especificaciones mínimas requeridas |
| Problemas de email | Emails de Brevo no llegan | Medio | Bajo | Probar integración de Brevo temprano |
| Datos insuficientes | Datos de prueba no representativos | Medio | Medio | Crear dataset completo con casos reales |

---

## 10. Cronograma Tentativo

| Actividad | Descripción | Fecha Inicio | Fecha Fin | Responsable |
|---|---|---|---|---|
| Preparación del entorno | Configuración de BD, servidor, herramientas | 15/12/2025 | 16/12/2025 | QA Lead |
| Diseño de casos de prueba | Elaboración de matrices y documentación | 16/12/2025 | 18/12/2025 | QA Lead |
| Pruebas funcionales | Ejecución de pruebas de módulos principales | 18/12/2025 | 24/12/2025 | QA Testers |
| Pruebas de rendimiento | Pruebas de carga y tiempo de respuesta | 22/12/2025 | 25/12/2025 | QA Team |
| Pruebas de seguridad | Validación de seguridad y vulnerabilidades | 23/12/2025 | 26/12/2025 | QA Lead |
| Registro de defectos | Documentación sistemática de errores | 18/12/2025 | 27/12/2025 | QA Testers |
| Corrección de errores | Ajuste y verificación de defectos | 24/12/2025 | 28/12/2025 | Desarrolladores |
| Pruebas de regresión | Verificar que correcciones no rompan nada | 27/12/2025 | 29/12/2025 | QA Testers |
| Pruebas de aceptación | Validación con cliente | 28/12/2025 | 29/12/2025 | Cliente + QA |
| Informe final | Consolidación y aprobación de resultados | 29/12/2025 | 30/12/2025 | QA Lead |

---

## 11. Métricas de Éxito

- **Cobertura de pruebas:** ≥ 80% de funcionalidades probadas
- **Defectos críticos:** 0 defectos críticos sin resolver
- **Defectos mayores:** ≤ 5 defectos mayores sin resolver
- **Tiempo de respuesta:** 95% de transacciones < 3 segundos
- **Disponibilidad:** 99.5% uptime durante pruebas
- **Tasa de aprobación:** ≥ 95% de casos de prueba pasados
- **Vulnerabilidades:** 0 vulnerabilidades críticas

---

## 12. Aprobaciones

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| QA Lead | | | |
| Project Manager | | | |
| Cliente | | | |
| Desarrollador Lead | | | |

---

**Documento preparado por:** Equipo QA  
**Fecha de elaboración:** 15/12/2025  
**Versión:** 1.0
