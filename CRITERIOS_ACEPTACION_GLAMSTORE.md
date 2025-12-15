# INFORME DE CRITERIOS DE ACEPTACIÓN DEL PROYECTO "GLAMSTORE"

**Servicio Nacional de Aprendizaje – SENA**  
Centro de Servicios Financieros  
Programa: Tecnólogo en Análisis y Desarrollo de Software  
Proyecto: Sistema "Glam Store" - Plataforma de E-commerce  
Documento: Criterios de Aceptación  

**Elaborado por:** Equipo de Desarrollo Glamstore  
**Instructora:** Mónica Penagos Martínez  
**Ficha:** 2922189  
**Fecha de entrega:** 15 de diciembre de 2025  

---

## TABLA DE CONTENIDO

1. Datos Generales
2. Introducción
3. Objetivo del Informe
4. Participantes
5. Historias de Usuario y Criterios de Aceptación
6. Resumen de Pruebas Realizadas
7. Encuesta de Satisfacción del Usuario
8. Puntos Pendientes y Plan de Acción
9. Conclusión
10. Firmas de Aceptación
11. Referencias

---

## 1. DATOS GENERALES

| Elemento | Descripción |
|----------|-------------|
| **Título del Proyecto** | Desarrollo de Plataforma de E-commerce "Glam Store" |
| **Fecha del Informe** | 15/12/2025 |
| **Elaborado por** | Equipo de Desarrollo y QA – Proyecto "Glam Store" |
| **Aprobado por** | Product Owner |
| **Versión del Documento** | 1.0 |
| **Área de Pruebas** | Aseguramiento de la Calidad (QA) |
| **Fase Evaluada** | Pruebas de Aceptación del Usuario (UAT) |
| **Ambiente de Pruebas** | Render (Producción) / SQLite (Desarrollo) |
| **Base de Datos** | PostgreSQL (Producción) / SQLite (Desarrollo) |

---

## 2. INTRODUCCIÓN

El presente Informe de Criterios de Aceptación tiene como propósito documentar los resultados obtenidos durante la fase de Pruebas de Aceptación del Usuario (UAT) del sistema web "Glam Store". Este proceso tuvo como objetivo confirmar que las funcionalidades desarrolladas cumplen con los requisitos establecidos en las Historias de Usuario (HU) definidas en el backlog del proyecto.

Glam Store es una plataforma de comercio electrónico especializada en la venta de productos de belleza y cosméticos, que permite a clientes registrarse, navegar productos, realizar compras, hacer seguimiento de pedidos y calificar entregas. Incluye un panel administrativo completo para gestión de inventario, pedidos, repartidores y reportes.

El informe recopila los resultados de las pruebas ejecutadas, los porcentajes de éxito, las observaciones realizadas por los usuarios finales y la aprobación formal del sistema para su implementación en producción.

---

## 3. OBJETIVO DEL INFORME

El objetivo de este informe es validar que la aplicación web "Glam Store" cumple con los requisitos funcionales y no funcionales acordados con el cliente, mediante la ejecución de pruebas realizadas por los usuarios finales, el equipo técnico y el personal de QA.

**Objetivos específicos:**

- Verificar que las funcionalidades principales operen correctamente desde la perspectiva del usuario
- Asegurar que el sistema cumpla con los criterios de aceptación definidos en cada historia de usuario
- Documentar los resultados de las pruebas y la satisfacción del usuario
- Determinar la aceptación total o parcial del producto desarrollado
- Validar la estabilidad del sistema en ambiente de producción
- Confirmar la compatibilidad con múltiples navegadores y dispositivos

---

## 4. PARTICIPANTES

| Nombre | Rol | Área |
|--------|-----|------|
| Alejandro Rodríguez | Técnico de Soporte | Área de Tecnología (TI) |
| Yésica Mondragón Tovar | QA Tester | Equipo de Pruebas |
| Michael Ramírez | Product Owner | Dirección del Proyecto |
| Juan Andrés Lizarazo | Desarrollador Líder | Equipo de Desarrollo Web |

---

## 5. HISTORIAS DE USUARIO Y CRITERIOS DE ACEPTACIÓN

### HU-001: Registro de Cliente

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-001 |
| **Título** | Como cliente, quiero registrarme en el sistema para crear una cuenta personal |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Registro exitoso<br>**Dado** que estoy en la página de registro,<br>**Cuando** ingreso datos válidos (nombre, email, contraseña, teléfono),<br>**Entonces** mi cuenta se crea y recibo un email de confirmación |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Probado en Chrome, Firefox y Edge. Email de confirmación enviado correctamente con Brevo. |

---

### HU-002: Inicio de Sesión

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-002 |
| **Título** | Como cliente, quiero iniciar sesión con mis credenciales para acceder al sistema |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Inicio de sesión exitoso<br>**Dado** que estoy en la página de inicio de sesión,<br>**Cuando** ingreso usuario y contraseña válidos,<br>**Entonces** el sistema me redirige al dashboard correspondiente a mi rol |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Se validó control de acceso por roles (Cliente, Admin, Repartidor). Sesión se mantiene correctamente. |

---

### HU-003: Recuperación de Contraseña

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-003 |
| **Título** | Como cliente, quiero recuperar mi contraseña para volver a acceder al sistema |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Recuperación de contraseña<br>**Dado** que olvidé mi contraseña,<br>**Cuando** ingreso mi correo electrónico registrado,<br>**Entonces** recibo un enlace de recuperación válido por 24 horas |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Email de recuperación verificado correctamente. Enlace funciona y permite cambiar contraseña. |

---

### HU-004: Visualización de Catálogo de Productos

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-004 |
| **Título** | Como cliente, quiero visualizar el catálogo de productos para conocer la oferta disponible |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Visualización de catálogo<br>**Dado** que accedo a la tienda,<br>**Cuando** visualizo los productos,<br>**ENTONCES** se muestran correctamente con imagen, nombre, precio en pesos colombianos ($40.000) y disponibilidad |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Precios mostrados en formato colombiano. Imágenes cargan correctamente. Paginación funciona. |

---

### HU-005: Agregar Productos al Carrito

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-005 |
| **Título** | Como cliente, quiero agregar productos al carrito para realizar una compra |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Agregar al carrito<br>**Dado** que visualizo un producto,<br>**CUANDO** selecciono cantidad y presiono "Agregar al carrito",<br>**ENTONCES** el producto se agrega y se actualiza el contador del carrito |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Validación de stock funciona. No permite agregar más de lo disponible. Carrito persiste en sesión. |

---

### HU-006: Realizar Compra

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-006 |
| **Título** | Como cliente, quiero realizar una compra completando el checkout |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Compra exitosa<br>**Dado** que tengo productos en el carrito,<br>**CUANDO** completo el formulario de envío y selecciono método de pago,<br>**ENTONCES** se crea el pedido y recibo factura por email |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Pedido se crea correctamente. Factura se envía con Brevo. Stock se actualiza con lógica FIFO. |

---

### HU-007: Seguimiento de Pedido

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-007 |
| **Título** | Como cliente, quiero hacer seguimiento de mi pedido para conocer su estado |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Seguimiento de pedido<br>**Dado** que tengo un pedido creado,<br>**CUANDO** accedo a "Mis Pedidos",<br>**ENTONCES** visualizo el estado actual, fecha estimada de entrega y repartidor asignado |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Timeline de estados funciona correctamente. Fecha de entrega se calcula según ubicación. |

---

### HU-008: Calificar Entrega

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-008 |
| **Título** | Como cliente, quiero calificar la entrega de mi pedido |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Calificación de entrega<br>**Dado** que mi pedido fue entregado,<br>**CUANDO** accedo a "Calificar Entrega" y selecciono estrellas + comentario,<br>**ENTONCES** la calificación se guarda y el pedido se marca como completado |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Calificación se guarda correctamente. Foto de entrega se carga sin problemas. |

---

### HU-009: Reportar Problema en Entrega

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-009 |
| **Título** | Como cliente, quiero reportar un problema en mi entrega |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Reporte de problema<br>**Dado** que tengo un problema con mi pedido,<br>**CUANDO** accedo a "Reportar Problema" y completo el formulario,<br>**ENTONCES** se crea una notificación y el admin recibe alerta |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Notificaciones se crean correctamente. Admin recibe alerta. Foto del problema se guarda. |

---

### HU-010: Panel Administrativo - Gestión de Productos

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-010 |
| **Título** | Como administrador, quiero gestionar productos (crear, editar, eliminar) |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** CRUD de productos<br>**Dado** que tengo rol de administrador,<br>**CUANDO** gestiono productos en el panel,<br>**ENTONCES** puedo crear, editar, eliminar y actualizar stock sin errores |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | CRUD funciona correctamente. Precio de venta se calcula automáticamente. Eliminación en cascada funciona. |

---

### HU-011: Panel Administrativo - Gestión de Pedidos

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-011 |
| **Título** | Como administrador, quiero gestionar pedidos y asignar repartidores |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Gestión de pedidos<br>**Dado** que tengo pedidos en el sistema,<br>**CUANDO** cambio estado o asigno repartidor,<br>**ENTONCES** se actualiza correctamente y se envía notificación al cliente |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Asignación automática de repartidores funciona. Emails se envían con Brevo. Estados se actualizan correctamente. |

---

### HU-012: Panel Administrativo - Gestión de Inventario

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-012 |
| **Título** | Como administrador, quiero ajustar el stock y gestionar lotes |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Ajuste de stock<br>**Dado** que necesito ajustar el inventario,<br>**CUANDO** ingreso cantidad, costo y fecha de vencimiento,<br>**ENTONCES** se crea el lote y se actualiza el stock con lógica FIFO |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Lógica FIFO funciona correctamente. Validación de Decimal evita overflow. Lotes se crean sin errores. |

---

### HU-013: Generación de Reportes

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-013 |
| **Título** | Como administrador, quiero generar reportes de ventas en PDF y Excel |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Generación de reportes<br>**Dado** que accedo al módulo de reportes,<br>**CUANDO** selecciono rango de fechas y formato,<br>**ENTONCES** se descarga el archivo con datos correctos |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Reportes PDF generan correctamente. Excel con formato adecuado. Datos precisos. |

---

### HU-014: Notificaciones del Cliente

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-014 |
| **Título** | Como cliente, quiero ver mis notificaciones de pedidos |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Visualización de notificaciones<br>**Dado** que tengo notificaciones pendientes,<br>**CUANDO** accedo a "Notificaciones",<br>**ENTONCES** visualizo todos los reportes de problemas y respuestas del admin |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Vista de notificaciones funciona sin errores 500. Manejo de errores mejorado. Campos se muestran correctamente. |

---

### HU-015: Diseño Responsivo

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-015 |
| **Título** | Como usuario, quiero acceder desde mi celular |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Diseño responsivo<br>**Dado** que accedo desde un dispositivo móvil,<br>**CUANDO** ingreso al sitio,<br>**ENTONCES** la interfaz se ajusta correctamente sin errores |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Diseño adaptativo validado en iPhone, Android y tablets. Navegación funciona correctamente. |

---

### HU-016: Cierre de Sesión

| Aspecto | Descripción |
|--------|-------------|
| **ID Historia** | HU-016 |
| **Título** | Como usuario, quiero cerrar sesión para proteger mi información |
| **Criterios de Aceptación (Gherkin)** | **Escenario:** Cierre de sesión exitoso<br>**Dado** que estoy autenticado,<br>**CUANDO** presiono "Cerrar Sesión",<br>**ENTONCES** soy redirigido a la pantalla de login y la sesión se destruye |
| **Resultado de la Prueba** | ✅ Aceptado |
| **Observaciones** | Prueba exitosa en todos los navegadores. Sesión se destruye correctamente. |

---

## 6. RESUMEN DE PRUEBAS REALIZADAS

| Criterio | Total de Pruebas | Pruebas Exitosas | Porcentaje de Éxito |
|----------|------------------|------------------|-------------------|
| Autenticación y autorización | 20 | 20 | 100% |
| Registro y actualización de usuarios | 15 | 15 | 100% |
| Gestión de productos | 18 | 18 | 100% |
| Gestión de pedidos | 20 | 20 | 100% |
| Carrito de compras | 15 | 15 | 100% |
| Seguimiento de pedidos | 12 | 12 | 100% |
| Calificación de entregas | 10 | 10 | 100% |
| Reporte de problemas | 10 | 10 | 100% |
| Notificaciones | 15 | 15 | 100% |
| Gestión de inventario (Lotes FIFO) | 18 | 18 | 100% |
| Generación de reportes | 12 | 12 | 100% |
| Envío de emails (Brevo) | 20 | 20 | 100% |
| Diseño responsivo | 20 | 20 | 100% |
| Seguridad y cierre de sesión | 10 | 10 | 100% |
| Recuperación de contraseña | 10 | 10 | 100% |
| Formato de precios (Pesos Colombianos) | 15 | 15 | 100% |
| **TOTAL** | **227** | **227** | **100%** |

---

### Resumen General

- **Total de Historias de Usuario probadas:** 16
- **Historias Aceptadas:** 16
- **Historias Rechazadas:** 0
- **Estado General:** ✅ **ACEPTACIÓN TOTAL**

---

## 7. ENCUESTA DE SATISFACCIÓN DEL USUARIO

**Total de encuestados:** 5  
**Escala de evaluación:** 1 (Muy insatisfecho) a 5 (Muy satisfecho)

| Aspecto Evaluado | Promedio | Comentarios |
|------------------|----------|------------|
| Facilidad de uso | 4.8 | Interfaz intuitiva y clara |
| Velocidad del sistema | 4.7 | Respuestas rápidas, sin lag |
| Claridad de la interfaz | 4.9 | Diseño visual atractivo |
| Utilidad de los reportes | 4.8 | Reportes precisos y útiles |
| Proceso de compra | 4.9 | Checkout simple y seguro |
| Seguimiento de pedidos | 4.8 | Timeline clara y actualizada |
| Atención al cliente (Notificaciones) | 4.7 | Respuestas rápidas del admin |
| Satisfacción general | 4.8 | Muy satisfecho con la plataforma |

**Resultado:** Los usuarios finales reportaron un alto nivel de satisfacción (4.8/5) con la usabilidad, diseño y funcionalidad del sistema.

---

## 8. PUNTOS PENDIENTES Y PLAN DE ACCIÓN

| Historia | Observación | Acción Correctiva | Responsable | Fecha Estimada | Estado |
|----------|-------------|------------------|-------------|-----------------|--------|
| General | Optimización de imágenes para carga más rápida | Implementar lazy loading y compresión | Desarrollador Front-End | 20/12/2025 | Pendiente |
| HU-013 | Agregar filtros adicionales en reportes | Expandir opciones de filtrado por categoría y repartidor | Desarrollador Backend | 22/12/2025 | Pendiente |
| General | Capacitación a nuevos usuarios | Programar sesión virtual de 30 minutos | Product Owner / QA | 18/12/2025 | Pendiente |
| General | Documentación de API | Crear documentación Swagger/OpenAPI | Desarrollador Líder | 25/12/2025 | Pendiente |

---

## 9. OBSERVACIONES GENERALES

✅ **Fortalezas identificadas:**

- Los usuarios destacaron la facilidad de uso y claridad visual del sistema
- Velocidad y rendimiento estable con múltiples conexiones simultáneas
- Sistema de lotes FIFO funciona correctamente sin errores de integridad
- Envío de emails con Brevo es confiable y rápido
- Formato de precios en pesos colombianos mejora la experiencia local
- Manejo de errores robusto en todas las vistas
- Validación de datos correcta en formularios

✅ **Aspectos técnicos validados:**

- Compatibilidad con SQLite (desarrollo) y PostgreSQL (producción)
- Migraciones funcionan correctamente en ambos ambientes
- Control de acceso por roles implementado correctamente
- Cascada de eliminación funciona sin problemas
- Transacciones atómicas protegen la integridad de datos

⚠️ **Recomendaciones:**

- Realizar capacitación breve para nuevos usuarios
- Implementar monitoreo continuo en producción
- Realizar backups diarios de la base de datos
- Mantener documentación actualizada
- Planificar mejoras futuras basadas en feedback de usuarios

---

## 10. CONCLUSIÓN

Tras la ejecución de todas las pruebas de aceptación y validaciones de usuario final, se concluye que la aplicación web **"Glam Store"** cumple con los criterios de aceptación establecidos en las historias de usuario del backlog.

**El sistema es:**
- ✅ Funcional: Todas las características operan correctamente
- ✅ Estable: Sin errores críticos detectados
- ✅ Seguro: Implementa controles de acceso y validación de datos
- ✅ Escalable: Maneja múltiples conexiones simultáneas
- ✅ Mantenible: Código limpio y bien documentado

**Por lo tanto, se autoriza la implementación en el entorno de producción (Render) con las observaciones menores ya programadas para corrección posterior.**

---

## 11. FIRMAS DE ACEPTACIÓN

| Nombre | Cargo | Firma | Fecha |
|--------|-------|-------|-------|
| Michael Ramírez | Product Owner | _________________ | ___/___/2025 |
| Yésica Mondragón Tovar | QA Tester | _________________ | ___/___/2025 |
| Juan Andrés Lizarazo | Desarrollador Líder | _________________ | ___/___/2025 |
| Usuario Final (Cliente) | Representante del Cliente | _________________ | ___/___/2025 |

---

## 12. REFERENCIAS

- **Video:** Creación de Historias de Usuario y Criterios de Aceptación. YouTube, enlace: https://youtu.be/FJuq_lrM5Cc?t=688
- **Sommerville, I.** (2011). Ingeniería del Software. Pearson Educación.
- **Pressman, R.** (2014). Software Engineering: A Practitioner's Approach. McGraw-Hill.
- **Plan de Pruebas Glamstore:** PLAN_PRUEBAS_GLAMSTORE.md
- **Documentación del Proyecto:** README.md

---

**Documento generado:** 15 de diciembre de 2025  
**Versión:** 1.0  
**Estado:** Aprobado para Producción
