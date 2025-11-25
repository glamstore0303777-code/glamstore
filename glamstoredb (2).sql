-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-11-2025 a las 02:51:39
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `glamstoredb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add cliente', 7, 'add_cliente'),
(26, 'Can change cliente', 7, 'change_cliente'),
(27, 'Can delete cliente', 7, 'delete_cliente'),
(28, 'Can view cliente', 7, 'view_cliente'),
(29, 'Can add repartidor', 8, 'add_repartidor'),
(30, 'Can change repartidor', 8, 'change_repartidor'),
(31, 'Can delete repartidor', 8, 'delete_repartidor'),
(32, 'Can view repartidor', 8, 'view_repartidor'),
(33, 'Can add rol', 9, 'add_rol'),
(34, 'Can change rol', 9, 'change_rol'),
(35, 'Can delete rol', 9, 'delete_rol'),
(36, 'Can view rol', 9, 'view_rol'),
(37, 'Can add usuario', 10, 'add_usuario'),
(38, 'Can change usuario', 10, 'change_usuario'),
(39, 'Can delete usuario', 10, 'delete_usuario'),
(40, 'Can view usuario', 10, 'view_usuario'),
(41, 'Can add pedido', 11, 'add_pedido'),
(42, 'Can change pedido', 11, 'change_pedido'),
(43, 'Can delete pedido', 11, 'delete_pedido'),
(44, 'Can view pedido', 11, 'view_pedido'),
(45, 'Can add producto', 12, 'add_producto'),
(46, 'Can change producto', 12, 'change_producto'),
(47, 'Can delete producto', 12, 'delete_producto'),
(48, 'Can view producto', 12, 'view_producto'),
(49, 'Can add categoria', 13, 'add_categoria'),
(50, 'Can change categoria', 13, 'change_categoria'),
(51, 'Can delete categoria', 13, 'delete_categoria'),
(52, 'Can view categoria', 13, 'view_categoria'),
(53, 'Can add distribuidor', 14, 'add_distribuidor'),
(54, 'Can change distribuidor', 14, 'change_distribuidor'),
(55, 'Can delete distribuidor', 14, 'delete_distribuidor'),
(56, 'Can view distribuidor', 14, 'view_distribuidor'),
(57, 'Can add distribuidor producto', 15, 'add_distribuidorproducto'),
(58, 'Can change distribuidor producto', 15, 'change_distribuidorproducto'),
(59, 'Can delete distribuidor producto', 15, 'delete_distribuidorproducto'),
(60, 'Can view distribuidor producto', 15, 'view_distribuidorproducto'),
(61, 'Can add mensaje contacto', 16, 'add_mensajecontacto'),
(62, 'Can change mensaje contacto', 16, 'change_mensajecontacto'),
(63, 'Can delete mensaje contacto', 16, 'delete_mensajecontacto'),
(64, 'Can view mensaje contacto', 16, 'view_mensajecontacto'),
(65, 'Can add profile', 17, 'add_profile'),
(66, 'Can change profile', 17, 'change_profile'),
(67, 'Can delete profile', 17, 'delete_profile'),
(68, 'Can view profile', 17, 'view_profile'),
(69, 'Can add detalle pedido', 18, 'add_detallepedido'),
(70, 'Can change detalle pedido', 18, 'change_detallepedido'),
(71, 'Can delete detalle pedido', 18, 'delete_detallepedido'),
(72, 'Can view detalle pedido', 18, 'view_detallepedido'),
(73, 'Can add notificacion', 19, 'add_notificacion'),
(74, 'Can change notificacion', 19, 'change_notificacion'),
(75, 'Can delete notificacion', 19, 'delete_notificacion'),
(76, 'Can view notificacion', 19, 'view_notificacion'),
(77, 'Can add pedido producto', 20, 'add_pedidoproducto'),
(78, 'Can change pedido producto', 20, 'change_pedidoproducto'),
(79, 'Can delete pedido producto', 20, 'delete_pedidoproducto'),
(80, 'Can view pedido producto', 20, 'view_pedidoproducto'),
(81, 'Can add subcategoria', 21, 'add_subcategoria'),
(82, 'Can change subcategoria', 21, 'change_subcategoria'),
(83, 'Can delete subcategoria', 21, 'delete_subcategoria'),
(84, 'Can view subcategoria', 21, 'view_subcategoria'),
(85, 'Can add movimiento producto', 22, 'add_movimientoproducto'),
(86, 'Can change movimiento producto', 22, 'change_movimientoproducto'),
(87, 'Can delete movimiento producto', 22, 'delete_movimientoproducto'),
(88, 'Can view movimiento producto', 22, 'view_movimientoproducto'),
(89, 'Can add notificacion problema', 23, 'add_notificacionproblema'),
(90, 'Can change notificacion problema', 23, 'change_notificacionproblema'),
(91, 'Can delete notificacion problema', 23, 'delete_notificacionproblema'),
(92, 'Can view notificacion problema', 23, 'view_notificacionproblema');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$fuC3u5YxeZidYXW7wwnSGP$Lh3N7ccFjYGXMD5lGEk8lxrNDuRwHtc154YBiL8DEpA=', NULL, 1, 'lauren samanta', '', '', 'laurensamanta0.r@gmail.com', 1, 1, '2025-11-05 18:55:12.012073'),
(2, 'pbkdf2_sha256$600000$ouGFhpOpJpoenXf23VgHHF$6dtSgXYWfcDhK1gicdsYrzd9uMo/ueUE/OYjjQLpzWE=', NULL, 1, 'lauren o', '', '', 'laurensamanta0.r@gmail.com', 1, 1, '2025-11-05 18:56:53.161260'),
(3, 'pbkdf2_sha256$600000$TBb8BeLASfOa3VDAO9RUU5$3otJZeKf3LWeuSdqoRWDocO44LH6ZZJqFhQ0bxMqUug=', NULL, 1, 'lauren s o', '', '', 'laurensamanta0.r@gmail.com', 1, 1, '2025-11-05 19:07:03.983906'),
(4, 'pbkdf2_sha256$600000$eVapBQU4k6hm38umXtc0CB$m89+Y+2flsr8jb+TYpiAR2wDw7z84tjnEZKren6AZwE=', NULL, 1, 'lauren sama', '', '', 'lausamanta2024@gmail.com', 1, 1, '2025-11-05 19:09:17.520694'),
(5, 'pbkdf2_sha256$600000$Dh5b5qMETiYRuBOvFB2w5o$v0ljQMznCEDfoXCVPvSTIsiyFOM3Jfhh7J2SqWCXa6M=', NULL, 1, 'lauren sam o', '', '', 'lausamanta2024@gmail.com', 1, 1, '2025-11-05 19:14:36.406095'),
(6, 'pbkdf2_sha256$600000$kT2F7owFSa9otjqSx96chS$p4I1CisHXfo76Etgfx+Ra3h5ia0YRKk+6p0uj8eh/Bo=', NULL, 1, 'laurem', '', '', 'lausamanta2024@gmail.com', 1, 1, '2025-11-05 19:15:27.186846'),
(7, 'pbkdf2_sha256$600000$sek4ueXhKoy4lTfFlEsuzu$77CuMjbdoE+VzvV2eTHOn2M/+vFw4ry8S5thj1JYP4g=', NULL, 1, 'leo', '', '', 'lausamanta2024@gmail.com', 1, 1, '2025-11-05 19:18:04.790263'),
(8, 'pbkdf2_sha256$600000$45DvRAXE6aMclDDz98v681$1xQbkF09WAxmt5dkYgkJHpKgi1I70DalqlRa+pv0+IQ=', NULL, 1, 'lauren primero', '', '', 'lausamanta2024@gmail.com', 1, 1, '2025-11-05 19:21:06.132387'),
(9, 'pbkdf2_sha256$600000$DVzXBqEhBpBp3CfHDhyszp$hlk/YfaN69RlOi94K6FCjAzsvdCeqziTAiXTf1JdYfA=', NULL, 1, 'nose', '', '', 'lausamanta2024@gmail.com', 1, 1, '2025-11-05 19:29:27.677923'),
(10, 'pbkdf2_sha256$600000$hQnXxaaYLbTIKTpPigfoJy$N85A3gM0JKZdeHdQbkat7YkbmYyZcWtfgKaAw0BQYUY=', NULL, 1, 'lau', '', '', 'lausamanta2024@gmail.com', 1, 1, '2025-11-05 19:34:55.465552'),
(11, 'pbkdf2_sha256$600000$9l5EUMdf7qOhelMDP9FloC$sCDpSFg4vzfC8emCWoE++alAUTH6xK55ReqOf9JsE3E=', NULL, 1, 'bobo', '', '', 'bob.glam@glamstore.com', 1, 1, '2025-11-05 21:33:48.277178'),
(12, 'pbkdf2_sha256$600000$RmyZRxoNvcQI7O2Vuaer74$W//91Xi+D1eo12O7SL4c4rSuQN6Bq3H7roUXP3Cj6Vk=', NULL, 1, 'bob', '', '', 'bob.glam@glamstore.com', 1, 1, '2025-11-05 21:38:39.869552');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `idCategoria` int(11) NOT NULL,
  `nombreCategoria` varchar(20) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`idCategoria`, `nombreCategoria`, `descripcion`, `imagen`) VALUES
(1, 'Rostro', 'Base, correctores, polvos compactos, rubores e iluminadores', 'categorias/rostro.avif'),
(2, 'Ojos', 'Sombras, delineadores, pesta?inas y cejas', 'categorias/ojos.jpg'),
(3, 'Labios', 'Labiales, brillos y delineadores de labios', 'categorias/la.jpg'),
(4, 'Uñas', 'Esmaltes, tratamientos y accesorios para uñas', 'categorias/uñas.webp'),
(5, 'Accesorios', 'Brochas, esponjas y herramientas de maquillaje', 'categorias/accessories_feb_main.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `idCliente` int(11) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`idCliente`, `cedula`, `nombre`, `email`, `direccion`, `telefono`) VALUES
(1, '12345678', 'Nombre Actualizado', 'nuevo_email@test.com', 'Nueva dirección de prueba', '3001234567'),
(2, '10002', 'Laura Gómez', 'laura.gomez@gmail.com', 'Carrera 45 #12-34 Montería', '2147483647'),
(13, '7410852', 'william fontecha', 'carlos@gmail.com', '58bis, Rafael Uribe Uribe, Bogotá, Bogotá D.C. (9-49)', '3115176388'),
(15, '441515', 'lalaa ortega', 'lala@gmail.com', 'carrera 19a 11a 67, Puente Aranda, Bogotá, Bogotá D.C. (9-49)', '3024892804'),
(17, '441515', 'laura torres', 'lauratorres@gmail.com', 'carrera 19a 11a 67, Engativá, Bogotá, Bogotá D.C. (9-49)', '3024892804'),
(18, '458527', 'laura tibaque', 'lauratibaque@gmail.com', 'carrera 19a 11a 67, Comuna 4 - Cazucá, Soacha, Cundinamarca (9-49)', '3025458285'),
(20, '1027520667', 'lauren ortiz', 'laurensamanta0.r@gmail.com', 'carrera 19a 11a 67, Comuna 6 - San Humberto, Soacha, Cundinamarca (9-49)', '3024892804'),
(22, '111111122222', 'michael   ', 'michael@gmail.com', 'calle123#12-14, Comuna 1 - Compartir, Soacha, Cundinamarca (soacha), Comuna 4 - Cazucá, Soacha, Cundinamarca (soacha), Antonio Nariño, Bogotá, Bogotá D.C. (barrio antonio nariño)', '3025858545'),
(23, '2025561653', 'alejandro rodriguez ', 'alejandro@gmail.com', 'calle123#4-5, Suba, Bogotá, Bogotá D.C. (suba ), Suba, Bogotá, Bogotá D.C. (suba )', '30254646254'),
(24, '123456789', 'Cliente Test', 'test@example.com', 'Calle Test 123, Bogotá', '3001234567'),
(25, '2452785278', 'magda maria', 'lausamanta2024cha@gmail.com', 'Calle 19a #11a-67', '3024892804'),
(26, '111111122222', 'maria magdalena ', 'lauren.20031028@gmail.com', 'calle123#4-5, Comuna 3 - Ciudad Verde, Soacha, Cundinamarca (soacha)', '30254646254');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_notificacion`
--

CREATE TABLE `core_notificacion` (
  `id` bigint(20) NOT NULL,
  `mensaje` longtext NOT NULL,
  `leida` tinyint(1) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `core_notificacion`
--

INSERT INTO `core_notificacion` (`id`, `mensaje`, `leida`, `fecha`, `usuario_id`) VALUES
(1, 'Nuevo pedido desde soacha, Cundinamarca.', 0, '2025-11-07 07:54:00.290765', 1),
(2, 'Nuevo pedido desde soacha, Cundinamarca.', 0, '2025-11-07 07:59:13.501034', 1),
(3, 'Nuevo pedido #11 de Cliente1 desde Calle Principal #123.', 0, '2025-11-07 08:37:56.186601', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_profile`
--

CREATE TABLE `core_profile` (
  `id` bigint(20) NOT NULL,
  `token_recuperacion` varchar(64) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `core_profile`
--

INSERT INTO `core_profile` (`id`, `token_recuperacion`, `user_id`) VALUES
(1, NULL, 1),
(2, NULL, 2),
(3, NULL, 3),
(4, NULL, 4),
(5, NULL, 5),
(6, NULL, 6),
(7, NULL, 7),
(8, NULL, 8),
(9, NULL, 9),
(10, NULL, 10),
(11, NULL, 11),
(12, NULL, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallepedido`
--

CREATE TABLE `detallepedido` (
  `idDetalle` int(11) NOT NULL,
  `idPedido` int(11) NOT NULL,
  `idProducto` bigint(20) DEFAULT NULL,
  `cantidad` int(10) UNSIGNED DEFAULT 1,
  `precio_unitario` decimal(10,2) NOT NULL,
  `subtotal` decimal(12,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detallepedido`
--

INSERT INTO `detallepedido` (`idDetalle`, `idPedido`, `idProducto`, `cantidad`, `precio_unitario`, `subtotal`) VALUES
(1, 2, 7701234567890, 2, 55000.00, 110000.00),
(2, 2, 7709876543210, 2, 18500.00, 37000.00),
(3, 3, 7701122334455, 2, 22500.00, 45000.00),
(6, 4, 7701122334455, 2, 22500.00, 45000.00),
(7, 2, 7701122334455, 2, 22500.00, 45000.00),
(8, 6, 7701234567890, 3, 55000.00, 165000.00),
(10, 2, 7709876543210, 1, 15000.00, 15000.00),
(12, 5, 7701122334455, 1, 22500.00, 22500.00),
(14, 9, 7700000000034, 1, 15000.00, 15000.00),
(15, 9, 7700000000013, 1, 16000.00, 16000.00),
(16, 10, 7700000000034, 1, 15000.00, 15000.00),
(17, 10, 7700000000013, 1, 16000.00, 16000.00),
(20, 14, 7700000000001, 1, 32000.00, 32000.00),
(21, 15, 7700000000002, 2, 38000.00, 76000.00),
(22, 15, 7700000000003, 1, 29000.00, 29000.00),
(23, 16, 7700000000043, 1, 12000.00, 12000.00),
(24, 17, 7700000000001, 1, 32000.00, 32000.00),
(25, 18, 7700000000001, 1, 32000.00, 32000.00),
(26, 18, 7700000000003, 1, 29000.00, 29000.00),
(27, 18, 7700000000004, 1, 34000.00, 34000.00),
(28, 18, 7700000000002, 1, 38000.00, 38000.00),
(32, 20, 7700000000012, 1, 18000.00, 18000.00),
(33, 21, 7700000000001, 1, 32000.00, 32000.00),
(34, 22, 7700000000001, 1, 32000.00, 32000.00),
(35, 23, 7700000000042, 1, 15000.00, 15000.00),
(36, 24, 7700000000032, 1, 14000.00, 14000.00),
(37, 25, 7700000000001, 1, 32000.00, 32000.00),
(38, 26, 7700000000002, 1, 38000.00, 38000.00),
(39, 27, 7700000000001, 1, 32000.00, 32000.00),
(40, 28, 7700000000032, 1, 14000.00, 14000.00),
(46, 33, 7700000000003, 1, 29000.00, 29000.00),
(47, 33, 7700000000004, 1, 34000.00, 34000.00),
(48, 34, 7700000000012, 1, 18000.00, 18000.00),
(49, 35, 7700000000004, 1, 34000.00, 34000.00),
(50, 36, 7700000000012, 1, 18000.00, 18000.00),
(51, 37, 7701234567890, 1, 55000.00, 55000.00),
(52, 38, 7700000000023, 1, 18000.00, 18000.00),
(53, 38, 7700000000021, 1, 22000.00, 22000.00),
(54, 39, 7700000000012, 1, 18000.00, 18000.00),
(55, 39, 7700000000013, 1, 16000.00, 16000.00),
(56, 40, 7700000000011, 1, 42000.00, 42000.00),
(60, 43, 7700000000012, 1, 18000.00, 18000.00),
(61, 43, 7700000000002, 1, 38000.00, 38000.00),
(62, 43, 7700000000003, 1, 29000.00, 29000.00),
(63, 43, 7700000000004, 1, 34000.00, 34000.00),
(64, 44, 7700000000012, 2, 18000.00, 36000.00),
(65, 45, 7700000000012, 2, 18000.00, 36000.00),
(66, 45, 7700000000013, 1, 16000.00, 16000.00),
(67, 46, 7700000000024, 1, 15000.00, 15000.00),
(68, 46, 7700000000025, 1, 30000.00, 30000.00),
(69, 46, 7700000000001, 1, 32000.00, 32000.00),
(70, 47, 7700000000001, 1, 32000.00, 32000.00),
(71, 48, 7700000000012, 1, 18000.00, 18000.00),
(74, 52, 7700000000001, 1, 32000.00, 32000.00),
(75, 52, 7700000000002, 1, 38000.00, 38000.00),
(76, 53, 7700000000001, 1, 32000.00, 32000.00),
(77, 53, 7700000000002, 1, 38000.00, 38000.00),
(78, 54, 7700000000003, 1, 29000.00, 29000.00),
(79, 55, 7700000000003, 1, 29000.00, 29000.00),
(80, 55, 7700000000004, 1, 34000.00, 34000.00),
(81, 56, 7700000000012, 1, 18000.00, 18000.00),
(82, 56, 7700000000011, 1, 42000.00, 42000.00),
(83, 57, 7700000000024, 1, 15000.00, 15000.00),
(84, 57, 7700000000023, 1, 18000.00, 18000.00),
(85, 58, 7700000000013, 1, 16000.00, 16000.00),
(86, 58, 7700000000014, 1, 20000.00, 20000.00),
(87, 59, 7700000000002, 1, 38000.00, 38000.00),
(88, 59, 7700000000003, 2, 29000.00, 58000.00),
(89, 60, 7700000000013, 1, 16000.00, 16000.00),
(90, 60, 7700000000012, 2, 18000.00, 36000.00),
(91, 61, 7701234567890, 2, 55000.00, 110000.00),
(92, 61, 7700000000011, 2, 42000.00, 84000.00),
(93, 62, 7700000000032, 1, 14000.00, 14000.00),
(94, 62, 7700000000031, 1, 12000.00, 12000.00),
(95, 63, 7700000000001, 1, 32000.00, 32000.00),
(96, 64, 7700000000002, 2, 38000.00, 76000.00),
(97, 64, 7700000000003, 1, 29000.00, 29000.00),
(98, 64, 7700000000001, 1, 32000.00, 32000.00),
(99, 65, 7700000000032, 1, 18200.00, 18200.00),
(100, 65, 7700000000033, 2, 23400.00, 46800.00),
(111, 74, 7700000000002, 1, 49400.00, 49400.00),
(112, 74, 7700000000044, 1, 36400.00, 36400.00),
(113, 74, 7700000000043, 2, 15600.00, 31200.00),
(114, 75, 7700000000005, 1, 75400.00, 75400.00),
(115, 75, 7700000000041, 1, 62400.00, 62400.00),
(116, 75, 7700000000042, 2, 19500.00, 39000.00),
(117, 76, 7700000000043, 2, 15600.00, 31200.00),
(118, 76, 7700000000042, 2, 19500.00, 39000.00),
(119, 76, 7700000000041, 2, 62400.00, 124800.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `distribuidores`
--

CREATE TABLE `distribuidores` (
  `idDistribuidor` int(11) NOT NULL,
  `nombreDistribuidor` varchar(30) DEFAULT NULL,
  `contacto` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `distribuidores`
--

INSERT INTO `distribuidores` (`idDistribuidor`, `nombreDistribuidor`, `contacto`) VALUES
(1, 'Proveedor Central ', '214748364'),
(7, 'Proveedor Central tt', '214748364755');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `distribuidorproducto`
--

CREATE TABLE `distribuidorproducto` (
  `idDistribuidor` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `distribuidorproducto`
--

INSERT INTO `distribuidorproducto` (`idDistribuidor`, `idProducto`) VALUES
(1, 1),
(1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(13, 'core', 'categoria'),
(7, 'core', 'cliente'),
(18, 'core', 'detallepedido'),
(14, 'core', 'distribuidor'),
(15, 'core', 'distribuidorproducto'),
(16, 'core', 'mensajecontacto'),
(22, 'core', 'movimientoproducto'),
(19, 'core', 'notificacion'),
(23, 'core', 'notificacionproblema'),
(11, 'core', 'pedido'),
(20, 'core', 'pedidoproducto'),
(12, 'core', 'producto'),
(17, 'core', 'profile'),
(8, 'core', 'repartidor'),
(9, 'core', 'rol'),
(21, 'core', 'subcategoria'),
(10, 'core', 'usuario'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-10-24 03:20:47.874567'),
(2, 'auth', '0001_initial', '2025-10-24 03:20:48.743453'),
(3, 'admin', '0001_initial', '2025-10-24 03:20:48.928893'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-10-24 03:20:48.939201'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-24 03:20:48.950214'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-10-24 03:20:49.030487'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-10-24 03:20:49.118988'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-10-24 03:20:49.142315'),
(9, 'auth', '0004_alter_user_username_opts', '2025-10-24 03:20:49.153530'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-10-24 03:20:49.215674'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-10-24 03:20:49.231239'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-10-24 03:20:49.235980'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-10-24 03:20:49.251292'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-10-24 03:20:49.266590'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-10-24 03:20:49.285854'),
(16, 'auth', '0011_update_proxy_permissions', '2025-10-24 03:20:49.301392'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-10-24 03:20:49.316915'),
(19, 'sessions', '0001_initial', '2025-10-24 03:20:49.667817'),
(23, 'core', '0001_initial', '2025-11-05 13:34:17.000000'),
(24, 'core', '0002_alter_usuario_options', '2025-11-05 21:43:09.057265'),
(25, 'core', '0003_alter_usuario_options', '2025-11-05 21:47:17.168330'),
(26, 'core', '0004_pedido_requiere_verificacion_pago', '2025-11-07 06:26:04.941682'),
(27, 'core', '0005_notificacion', '2025-11-07 07:42:30.092191'),
(28, 'core', '0002_alter_producto_options', '2025-11-09 09:27:39.215604'),
(29, 'core', '0003_producto_idcategoria_producto_idsubcategoria', '2025-11-09 09:32:39.927851'),
(30, 'core', '0004_alter_pedido_options', '2025-11-11 12:32:47.559560'),
(31, 'core', '0004_cliente_distribuidor_distribuidorproducto_repartidor_and_more', '2025-11-13 08:28:35.959682'),
(32, 'core', '0005_alter_categoria_options', '2025-11-13 08:53:56.428850'),
(33, 'core', '0006_categoria_imagen', '2025-11-13 08:56:42.951534'),
(34, 'core', '0007_movimientoproducto', '2025-11-13 12:27:27.093798'),
(35, 'core', '0008_movimientoproducto_precio_unitario', '2025-11-13 12:45:24.702391'),
(36, 'core', '0009_movimientoproducto_costo_unitario', '2025-11-13 12:52:30.896121'),
(37, 'core', '0010_notificacionproblema_delete_notificacion', '2025-11-21 00:10:53.250878'),
(38, 'core', '0011_notificacionproblema_fecha_respuesta_and_more', '2025-11-21 00:56:00.230509'),
(40, 'core', '0012_add_estado_fields', '2025-11-22 02:27:00.861390'),
(41, 'core', '0012_add_estado_fields_sql', '2025-11-22 02:30:23.696860'),
(42, 'core', '0013_alter_detallepedido_options_alter_pedido_options_and_more', '2025-11-24 22:12:21.771331'),
(43, 'core', '0014_repartidor_email', '2025-11-24 22:39:35.498162'),
(44, 'core', '0015_alter_repartidor_telefono', '2025-11-24 23:37:46.749415');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1ofml2vngq04ufspkh6n7glaqcods9lc', 'e30:1vMcsc:40C7WG9FUlqYEsmirrNoX0z7ZD_ZoBYmUXs9W6aYP7M', '2025-12-06 01:57:38.565879'),
('9ldcrjet1dmnb530p42ldcj31zcb41rc', '.eJyrViotLk0sysyPz0xRsjLUgXPz8nOTilKVrJRyEkuLUvOUEDJF-TlAlbUAayMUyg:1vNh8C:eBbKVRmo2Nb8Wcd0qjWaQMOOVa8B_4EpfGXpFihlO58', '2025-12-09 00:42:08.666163'),
('b72iptc762mpqkm89tk5wjf1hsjeekgw', 'e30:1vMcsb:0JHZJ70dRmUm8N1Ipu6CLAw1He5zQEj2Azce_8a7ibI', '2025-12-06 01:57:37.145277'),
('ic5qwsppvyb2a4ot3lgp7fo13es0d80u', '.eJyrViotLk0sysyPz0xRsjLUgXPz8nOTilKVrJRyEkuLUvOUEDJF-TlAlbUAayMUyg:1vNhP9:rcva9vRR4w8I7YAQWK1gIO6BiIRhJReasgbTMSUE_DA', '2025-12-09 00:59:39.024090'),
('l5900uvny2bedhbazs6j6j4x1dan99zf', '.eJyrVkpOLCrKLMlXsqpWMjc3gAFDIyUrQx0UEWOgSG0tAER1C_A:1vLrXM:LxqIck_4vhkHBeBGiSXlT-_SFABF0LwAY-Tanau3tb0', '2025-12-03 23:24:32.718893'),
('tpaasu0iccukacp3q24jsj4gimlci6m5', '.eJyrViotLk0sysyPz0xRsjLUgXPz8nOTilKVrJRyEkuLUvOUEDJF-TlAlbUAayMUyg:1vJWWz:_eaifUz35kpwBBbdR2ByLo2ruRlLwPHY9wTo3GRj2vk', '2025-11-27 12:34:29.154577');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturas`
--

CREATE TABLE `facturas` (
  `idFactura` int(11) NOT NULL,
  `idPedido` int(11) DEFAULT NULL,
  `montoTotal` decimal(10,2) DEFAULT NULL,
  `fechaEmision` timestamp NOT NULL DEFAULT current_timestamp(),
  `estado` varchar(20) DEFAULT 'Pendiente',
  `idMetodoPago` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `facturas`
--

INSERT INTO `facturas` (`idFactura`, `idPedido`, `montoTotal`, `fechaEmision`, `estado`, `idMetodoPago`) VALUES
(2, 2, 45000.00, '2025-10-21 15:57:06', 'Pagada', 1),
(3, 5, 45000.00, '2025-10-23 02:45:38', 'Pendiente', 1),
(4, 6, 45000.00, '2025-10-23 02:47:56', 'Pendiente', 1),
(5, 3, 45000.00, '2025-10-23 02:48:44', 'Pendiente', 1),
(6, 4, 45000.00, '2025-10-23 02:52:24', 'Pendiente', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajecontacto`
--

CREATE TABLE `mensajecontacto` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `mensaje` longtext NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `leido` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajes`
--

CREATE TABLE `mensajes` (
  `idMensaje` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mensaje` longtext NOT NULL,
  `fecha` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodospago`
--

CREATE TABLE `metodospago` (
  `idMetodoPago` int(11) NOT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `metodospago`
--

INSERT INTO `metodospago` (`idMetodoPago`, `tipo`, `descripcion`) VALUES
(1, 'Nequi', 'Pago desde la app Nequi con n?mero de celular asociado.'),
(2, 'Daviplata', 'Pago directo por Daviplata.'),
(3, 'Transferencia Bancaria', 'Transferencia desde cuentas bancarias a las apps indicadas.'),
(4, 'Efectivo', 'Pago en efectivo al recibir el pedido.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimientos_producto`
--

CREATE TABLE `movimientos_producto` (
  `idMovimiento` int(11) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `tipo_movimiento` varchar(50) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `stock_anterior` int(11) NOT NULL,
  `stock_nuevo` int(11) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `idPedido` int(11) DEFAULT NULL,
  `producto_id` bigint(20) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `costo_unitario` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `movimientos_producto`
--

INSERT INTO `movimientos_producto` (`idMovimiento`, `fecha`, `tipo_movimiento`, `cantidad`, `stock_anterior`, `stock_nuevo`, `descripcion`, `idPedido`, `producto_id`, `precio_unitario`, `costo_unitario`) VALUES
(1, '2025-11-13 12:28:33.741663', 'AJUSTE_MANUAL_ENTRADA', 100, 0, 100, 'Ajuste manual desde el panel de edición', NULL, 7700000000002, 0.00, 0.00),
(2, '2025-11-13 12:28:50.373593', 'AJUSTE_MANUAL_ENTRADA', 95, 5, 100, 'Ajuste manual desde el panel de edición', NULL, 7700000000023, 0.00, 0.00),
(3, '2025-11-13 12:29:01.429167', 'AJUSTE_MANUAL_ENTRADA', 97, 3, 100, 'Ajuste manual desde el panel de edición', NULL, 7700000000005, 0.00, 0.00),
(4, '2025-11-13 12:29:17.450394', 'AJUSTE_MANUAL_ENTRADA', 100, 0, 100, 'Ajuste manual desde el panel de edición', NULL, 7700000000001, 0.00, 0.00),
(5, '2025-11-13 12:29:32.805905', 'AJUSTE_MANUAL_ENTRADA', 97, 3, 100, 'Ajuste manual desde el panel de edición', NULL, 7700000000004, 0.00, 0.00),
(6, '2025-11-13 12:34:16.259831', 'SALIDA_VENTA', 1, 100, 99, 'Venta en pedido #19', NULL, 7700000000001, 0.00, 0.00),
(7, '2025-11-13 12:34:16.270438', 'SALIDA_VENTA', 1, 100, 99, 'Venta en pedido #19', NULL, 7700000000002, 0.00, 0.00),
(8, '2025-11-13 12:34:16.276011', 'SALIDA_VENTA', 1, 2, 1, 'Venta en pedido #19', NULL, 7700000000003, 0.00, 0.00),
(9, '2025-11-13 12:38:58.681016', 'AJUSTE_MANUAL_ENTRADA', 10, 99, 109, 'entrada de distribuidor', NULL, 7700000000001, 0.00, 0.00),
(10, '2025-11-13 12:39:21.372703', 'AJUSTE_MANUAL_SALIDA', 1, 100, 99, 'prueba', NULL, 7700000000005, 0.00, 0.00),
(11, '2025-11-13 12:40:25.332975', 'AJUSTE_MANUAL_ENTRADA', 100, 109, 209, 'prueba', NULL, 7700000000001, 0.00, 0.00),
(12, '2025-11-13 12:40:37.399236', 'AJUSTE_MANUAL_SALIDA', 100, 209, 109, 'prueba', NULL, 7700000000001, 0.00, 0.00),
(13, '2025-11-13 12:56:24.602070', 'AJUSTE_MANUAL_ENTRADA', 10, 99, 109, 'prueba', NULL, 7700000000005, 58000.00, 58000.00),
(14, '2025-11-13 12:56:34.874003', 'AJUSTE_MANUAL_ENTRADA', 5, 109, 114, 'prueba', NULL, 7700000000005, 58000.00, 58000.00),
(15, '2025-11-13 12:57:48.109245', 'AJUSTE_MANUAL_SALIDA', 1, 114, 113, 'prueba', NULL, 7700000000005, 58000.00, 0.00),
(16, '2025-11-13 13:00:13.600803', 'AJUSTE_MANUAL_ENTRADA', 2, 100, 102, 'prueba', NULL, 7700000000023, 18000.00, 18000.00),
(17, '2025-11-13 13:00:29.558824', 'AJUSTE_MANUAL_ENTRADA', 2, 102, 104, 'prueba', NULL, 7700000000023, 18000.00, 18000.00),
(18, '2025-11-13 13:01:10.339158', 'AJUSTE_MANUAL_SALIDA', 2, 104, 102, 'prueba', NULL, 7700000000023, 18000.00, 0.00),
(19, '2025-11-13 13:04:03.794447', 'AJUSTE_MANUAL_ENTRADA', 3, 102, 105, 'prueba', NULL, 7700000000023, 18000.00, 18000.00),
(20, '2025-11-20 13:14:45.561114', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #20', 20, 7700000000012, 18000.00, 0.00),
(21, '2025-11-20 13:27:44.052706', 'SALIDA_VENTA', 1, 109, 108, 'Venta en pedido #21', 21, 7700000000001, 32000.00, 0.00),
(22, '2025-11-20 13:30:46.793123', 'SALIDA_VENTA', 1, 108, 107, 'Venta en pedido #22', 22, 7700000000001, 32000.00, 0.00),
(23, '2025-11-20 15:26:58.003613', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #23', 23, 7700000000042, 15000.00, 0.00),
(24, '2025-11-20 15:28:42.041296', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #24', 24, 7700000000032, 14000.00, 0.00),
(25, '2025-11-20 15:53:40.103658', 'SALIDA_VENTA', 1, 107, 106, 'Venta en pedido #25', 25, 7700000000001, 32000.00, 0.00),
(26, '2025-11-20 16:13:31.403608', 'SALIDA_VENTA', 1, 99, 98, 'Venta en pedido #26', 26, 7700000000002, 38000.00, 0.00),
(27, '2025-11-20 18:59:45.574361', 'SALIDA_VENTA', 1, 106, 105, 'Venta en pedido #27', 27, 7700000000001, 32000.00, 0.00),
(28, '2025-11-20 19:03:10.921162', 'SALIDA_VENTA', 1, 4, 3, 'Venta en pedido #28', 28, 7700000000032, 14000.00, 0.00),
(30, '2025-11-20 19:05:52.159280', 'SALIDA_VENTA', 1, 105, 104, 'Venta en pedido #30', NULL, 7700000000001, 32000.00, 0.00),
(31, '2025-11-20 19:05:52.172165', 'SALIDA_VENTA', 1, 98, 97, 'Venta en pedido #30', NULL, 7700000000002, 38000.00, 0.00),
(32, '2025-11-20 19:16:22.798062', 'SALIDA_VENTA', 1, 4, 3, 'Venta en pedido #31', NULL, 7700000000012, 18000.00, 0.00),
(33, '2025-11-20 19:26:15.688884', 'SALIDA_VENTA', 1, 100, 99, 'Venta en pedido #32', NULL, 7700000000004, 34000.00, 0.00),
(34, '2025-11-20 19:54:27.680061', 'SALIDA_VENTA', 1, 1, 0, 'Venta en pedido #33', 33, 7700000000003, 29000.00, 0.00),
(35, '2025-11-20 19:54:27.680061', 'SALIDA_VENTA', 1, 99, 98, 'Venta en pedido #33', 33, 7700000000004, 34000.00, 0.00),
(36, '2025-11-20 20:05:09.793704', 'SALIDA_VENTA', 1, 3, 2, 'Venta en pedido #34', 34, 7700000000012, 18000.00, 0.00),
(37, '2025-11-20 20:12:06.100814', 'SALIDA_VENTA', 1, 98, 97, 'Venta en pedido #35', 35, 7700000000004, 34000.00, 0.00),
(38, '2025-11-20 20:20:36.869797', 'SALIDA_VENTA', 1, 2, 1, 'Venta en pedido #36', 36, 7700000000012, 18000.00, 0.00),
(39, '2025-11-20 22:14:43.399303', 'AJUSTE_MANUAL_ENTRADA', 10, 105, 115, 'prueba', NULL, 7700000000023, 18000.00, 18000.00),
(40, '2025-11-20 22:14:56.045460', 'AJUSTE_MANUAL_ENTRADA', 10, 115, 125, 'prueba', NULL, 7700000000023, 18000.00, 18000.00),
(41, '2025-11-21 00:32:13.268537', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #37', 37, 7701234567890, 55000.00, 0.00),
(42, '2025-11-21 01:06:53.778433', 'SALIDA_VENTA', 1, 125, 124, 'Venta en pedido #38', 38, 7700000000023, 18000.00, 0.00),
(43, '2025-11-21 01:06:53.781496', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #38', 38, 7700000000021, 22000.00, 0.00),
(44, '2025-11-21 01:08:27.631875', 'SALIDA_VENTA', 1, 1, 0, 'Venta en pedido #39', 39, 7700000000012, 18000.00, 0.00),
(45, '2025-11-21 01:08:27.639980', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #39', 39, 7700000000013, 16000.00, 0.00),
(46, '2025-11-21 01:13:13.395294', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #40', 40, 7700000000011, 42000.00, 0.00),
(47, '2025-11-21 01:19:04.299014', 'SALIDA_VENTA', 1, 4, 3, 'Venta en pedido #41', NULL, 7700000000013, 16000.00, 0.00),
(48, '2025-11-21 01:19:04.302065', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #41', NULL, 7700000000014, 20000.00, 0.00),
(49, '2025-11-21 01:21:28.466923', 'AJUSTE_MANUAL_ENTRADA', 100, 0, 100, 'prueba', NULL, 7700000000003, 29000.00, 29000.00),
(50, '2025-11-21 01:21:53.614000', 'AJUSTE_MANUAL_ENTRADA', 10, 0, 10, 'prueba', NULL, 7700000000012, 18000.00, 18000.00),
(53, '2025-11-21 23:11:41.101027', 'AJUSTE_MANUAL_ENTRADA', 10, 3, 13, '111', NULL, 7700000000013, 16000.00, 16000.00),
(56, '2025-11-21 23:30:06.085382', 'AJUSTE_MANUAL_ENTRADA', 1, 113, 114, 'prueba', NULL, 7700000000005, 58000.00, 58000.00),
(57, '2025-11-21 23:56:53.042792', 'AJUSTE_MANUAL_ENTRADA', 50, 104, 154, 'Reabastecimiento desde Excel - Rostro', NULL, 7700000000001, 32000.00, 32000.00),
(58, '2025-11-21 23:56:53.042792', 'AJUSTE_MANUAL_ENTRADA', 35, 97, 132, 'Reabastecimiento desde Excel - Rostro', NULL, 7700000000002, 38000.00, 38000.00),
(59, '2025-11-21 23:56:53.059442', 'AJUSTE_MANUAL_ENTRADA', 40, 100, 140, 'Reabastecimiento desde Excel - Rostro', NULL, 7700000000003, 29000.00, 29000.00),
(60, '2025-11-21 23:56:53.074528', 'AJUSTE_MANUAL_ENTRADA', 45, 97, 142, 'Reabastecimiento desde Excel - Rostro', NULL, 7700000000004, 34000.00, 34000.00),
(61, '2025-11-21 23:56:53.085753', 'AJUSTE_MANUAL_ENTRADA', 30, 114, 144, 'Reabastecimiento desde Excel - Rostro', NULL, 7700000000005, 58000.00, 58000.00),
(62, '2025-11-21 23:56:53.096264', 'AJUSTE_MANUAL_ENTRADA', 25, 4, 29, 'Reabastecimiento desde Excel - Rostro', NULL, 7701234567890, 55000.00, 55000.00),
(63, '2025-11-21 23:59:34.790142', 'AJUSTE_MANUAL_ENTRADA', 40, 13, 53, 'Reabastecimiento desde Excel - Ojos', NULL, 7700000000013, 16000.00, 16000.00),
(64, '2025-11-21 23:59:34.806346', 'AJUSTE_MANUAL_ENTRADA', 35, 4, 39, 'Reabastecimiento desde Excel - Ojos', NULL, 7700000000014, 20000.00, 20000.00),
(65, '2025-11-22 00:20:40.738720', 'AJUSTE_MANUAL_ENTRADA', 10, 124, 134, 'prueba', NULL, 7700000000023, 18000.00, 18000.00),
(66, '2025-11-22 00:20:54.820926', 'AJUSTE_MANUAL_SALIDA', 11, 134, 123, 'prueba', NULL, 7700000000023, 18000.00, 0.00),
(67, '2025-11-22 00:24:13.500283', 'AJUSTE_MANUAL_ENTRADA', 5, 154, 159, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000001, 32000.00, 32000.00),
(68, '2025-11-22 00:24:13.500283', 'AJUSTE_MANUAL_ENTRADA', 5, 132, 137, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000002, 38000.00, 38000.00),
(69, '2025-11-22 00:24:13.518238', 'AJUSTE_MANUAL_ENTRADA', 5, 140, 145, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000003, 29000.00, 29000.00),
(70, '2025-11-22 00:24:13.518238', 'AJUSTE_MANUAL_ENTRADA', 5, 142, 147, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000004, 34000.00, 34000.00),
(71, '2025-11-22 00:24:13.534368', 'AJUSTE_MANUAL_ENTRADA', 5, 144, 149, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000005, 58000.00, 58000.00),
(72, '2025-11-22 00:24:13.534368', 'AJUSTE_MANUAL_ENTRADA', 5, 29, 34, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7701234567890, 55000.00, 55000.00),
(73, '2025-11-22 00:25:22.684095', 'AJUSTE_MANUAL_ENTRADA', 5, 159, 164, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000001, 32000.00, 32000.00),
(74, '2025-11-22 00:25:22.685092', 'AJUSTE_MANUAL_ENTRADA', 5, 137, 142, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000002, 38000.00, 38000.00),
(75, '2025-11-22 00:25:22.699481', 'AJUSTE_MANUAL_ENTRADA', 5, 145, 150, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000003, 29000.00, 29000.00),
(76, '2025-11-22 00:25:22.716467', 'AJUSTE_MANUAL_ENTRADA', 5, 147, 152, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000004, 34000.00, 34000.00),
(77, '2025-11-22 00:25:22.716467', 'AJUSTE_MANUAL_ENTRADA', 5, 149, 154, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7700000000005, 58000.00, 58000.00),
(78, '2025-11-22 00:25:22.735871', 'AJUSTE_MANUAL_ENTRADA', 5, 34, 39, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central ', NULL, 7701234567890, 55000.00, 55000.00),
(79, '2025-11-22 00:49:26.361237', 'SALIDA_VENTA', 1, 123, 122, 'Venta en pedido #42', NULL, 7700000000023, 18000.00, 0.00),
(80, '2025-11-22 00:53:43.040008', 'SALIDA_VENTA', 1, 10, 9, 'Venta en pedido #43', 43, 7700000000012, 18000.00, 0.00),
(81, '2025-11-22 00:53:43.040008', 'SALIDA_VENTA', 1, 142, 141, 'Venta en pedido #43', 43, 7700000000002, 38000.00, 0.00),
(82, '2025-11-22 00:53:43.040008', 'SALIDA_VENTA', 1, 150, 149, 'Venta en pedido #43', 43, 7700000000003, 29000.00, 0.00),
(83, '2025-11-22 00:53:43.040008', 'SALIDA_VENTA', 1, 152, 151, 'Venta en pedido #43', 43, 7700000000004, 34000.00, 0.00),
(84, '2025-11-22 00:58:29.241807', 'SALIDA_VENTA', 2, 9, 7, 'Venta en pedido #44', 44, 7700000000012, 18000.00, 0.00),
(85, '2025-11-22 01:01:37.447823', 'AJUSTE_MANUAL_ENTRADA', 10, 3, 13, 'prueba', NULL, 7700000000032, 14000.00, 14000.00),
(86, '2025-11-22 01:12:30.721732', 'SALIDA_VENTA', 2, 7, 5, 'Venta en pedido #45', 45, 7700000000012, 18000.00, 0.00),
(87, '2025-11-22 01:12:30.726137', 'SALIDA_VENTA', 1, 53, 52, 'Venta en pedido #45', 45, 7700000000013, 16000.00, 0.00),
(88, '2025-11-22 01:21:06.674728', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #46', 46, 7700000000024, 15000.00, 0.00),
(89, '2025-11-22 01:21:06.680291', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #46', 46, 7700000000025, 30000.00, 0.00),
(90, '2025-11-22 01:21:06.682890', 'SALIDA_VENTA', 1, 164, 163, 'Venta en pedido #46', 46, 7700000000001, 32000.00, 0.00),
(91, '2025-11-22 01:35:57.527914', 'SALIDA_VENTA', 1, 163, 162, 'Venta en pedido #47', 47, 7700000000001, 32000.00, 0.00),
(92, '2025-11-22 01:36:36.788043', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #48', 48, 7700000000012, 18000.00, 0.00),
(93, '2025-11-22 01:52:10.707185', 'SALIDA_VENTA', 1, 122, 121, 'Venta en pedido #49', NULL, 7700000000023, 18000.00, 0.00),
(94, '2025-11-22 01:52:10.711768', 'SALIDA_VENTA', 1, 4, 3, 'Venta en pedido #49', NULL, 7700000000021, 22000.00, 0.00),
(95, '2025-11-22 02:52:36.233724', 'SALIDA_VENTA', 1, 162, 161, 'Venta en pedido #52', 52, 7700000000001, 32000.00, 0.00),
(96, '2025-11-22 02:52:36.239913', 'SALIDA_VENTA', 1, 141, 140, 'Venta en pedido #52', 52, 7700000000002, 38000.00, 0.00),
(97, '2025-11-22 02:56:08.765820', 'AJUSTE_MANUAL_ENTRADA', 10, 3, 13, 'prueba', NULL, 7700000000021, 22000.00, 22000.00),
(98, '2025-11-24 08:16:01.669467', 'SALIDA_VENTA', 1, 161, 160, 'Venta en pedido #53', 53, 7700000000001, 32000.00, 0.00),
(99, '2025-11-24 08:16:01.669467', 'SALIDA_VENTA', 1, 140, 139, 'Venta en pedido #53', 53, 7700000000002, 38000.00, 0.00),
(100, '2025-11-24 08:27:11.397872', 'SALIDA_VENTA', 1, 149, 148, 'Venta en pedido #54', 54, 7700000000003, 29000.00, 0.00),
(101, '2025-11-24 08:32:20.544862', 'AJUSTE_MANUAL_ENTRADA', 10, 160, 170, 'prueba', NULL, 7700000000001, 32000.00, 32000.00),
(102, '2025-11-24 08:33:05.002504', 'AJUSTE_MANUAL_ENTRADA', 100, 4, 104, 'prueba', NULL, 7700000000011, 42000.00, 42000.00),
(104, '2025-11-24 08:42:03.048175', 'SALIDA_VENTA', 1, 148, 147, 'Venta en pedido #55', 55, 7700000000003, 29000.00, 0.00),
(105, '2025-11-24 08:42:03.061125', 'SALIDA_VENTA', 1, 151, 150, 'Venta en pedido #55', 55, 7700000000004, 34000.00, 0.00),
(106, '2025-11-24 08:47:46.261052', 'SALIDA_VENTA', 1, 4, 3, 'Venta en pedido #56', 56, 7700000000012, 18000.00, 0.00),
(107, '2025-11-24 08:47:46.270376', 'SALIDA_VENTA', 1, 104, 103, 'Venta en pedido #56', 56, 7700000000011, 42000.00, 0.00),
(108, '2025-11-24 08:52:55.995817', 'SALIDA_VENTA', 1, 4, 3, 'Venta en pedido #57', 57, 7700000000024, 15000.00, 0.00),
(109, '2025-11-24 08:52:56.012791', 'SALIDA_VENTA', 1, 121, 120, 'Venta en pedido #57', 57, 7700000000023, 18000.00, 0.00),
(110, '2025-11-24 08:59:34.693504', 'AJUSTE_MANUAL_ENTRADA', 100, 3, 103, 'prueba', NULL, 7700000000012, 18000.00, 18000.00),
(111, '2025-11-24 11:22:15.120089', 'AJUSTE_MANUAL_ENTRADA', 5, 170, 175, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central tt', NULL, 7700000000001, 32000.00, 32000.00),
(112, '2025-11-24 11:22:15.138184', 'AJUSTE_MANUAL_ENTRADA', 5, 139, 144, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central tt', NULL, 7700000000002, 38000.00, 38000.00),
(113, '2025-11-24 11:22:15.154524', 'AJUSTE_MANUAL_ENTRADA', 5, 147, 152, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central tt', NULL, 7700000000003, 29000.00, 29000.00),
(114, '2025-11-24 11:22:15.169805', 'AJUSTE_MANUAL_ENTRADA', 5, 150, 155, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central tt', NULL, 7700000000004, 34000.00, 34000.00),
(115, '2025-11-24 11:22:15.183521', 'AJUSTE_MANUAL_ENTRADA', 5, 154, 159, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central tt', NULL, 7700000000005, 58000.00, 58000.00),
(116, '2025-11-24 11:22:15.195781', 'AJUSTE_MANUAL_ENTRADA', 5, 39, 44, 'Reabastecimiento desde Excel - Rostro - Proveedor: Proveedor Central tt', NULL, 7701234567890, 55000.00, 55000.00),
(117, '2025-11-24 11:38:41.759902', 'SALIDA_VENTA', 1, 52, 51, 'Venta en pedido #58', 58, 7700000000013, 16000.00, 0.00),
(118, '2025-11-24 11:38:41.764406', 'SALIDA_VENTA', 1, 39, 38, 'Venta en pedido #58', 58, 7700000000014, 20000.00, 0.00),
(119, '2025-11-24 19:45:28.043405', 'SALIDA_VENTA', 1, 144, 143, 'Venta en pedido #59', 59, 7700000000002, 38000.00, 0.00),
(120, '2025-11-24 19:45:28.044522', 'SALIDA_VENTA', 2, 152, 150, 'Venta en pedido #59', 59, 7700000000003, 29000.00, 0.00),
(121, '2025-11-24 19:46:43.704560', 'SALIDA_VENTA', 1, 51, 50, 'Venta en pedido #60', 60, 7700000000013, 16000.00, 0.00),
(122, '2025-11-24 19:46:43.715312', 'SALIDA_VENTA', 2, 103, 101, 'Venta en pedido #60', 60, 7700000000012, 18000.00, 0.00),
(123, '2025-11-24 20:07:39.848625', 'SALIDA_VENTA', 2, 44, 42, 'Venta en pedido #61', 61, 7701234567890, 55000.00, 0.00),
(124, '2025-11-24 20:07:39.852046', 'SALIDA_VENTA', 2, 103, 101, 'Venta en pedido #61', 61, 7700000000011, 42000.00, 0.00),
(125, '2025-11-24 20:11:05.527152', 'SALIDA_VENTA', 1, 13, 12, 'Venta en pedido #62', 62, 7700000000032, 14000.00, 0.00),
(126, '2025-11-24 20:11:05.527152', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #62', 62, 7700000000031, 12000.00, 0.00),
(127, '2025-11-24 21:42:51.369365', 'SALIDA_VENTA', 2, 143, 141, 'Venta en pedido #64', 64, 7700000000002, 38000.00, 0.00),
(128, '2025-11-24 21:42:51.383839', 'SALIDA_VENTA', 1, 150, 149, 'Venta en pedido #64', 64, 7700000000003, 29000.00, 0.00),
(129, '2025-11-24 21:42:51.385395', 'SALIDA_VENTA', 1, 175, 174, 'Venta en pedido #64', 64, 7700000000001, 32000.00, 0.00),
(130, '2025-11-24 22:07:17.543187', 'SALIDA_VENTA', 1, 12, 11, 'Venta en pedido #65', 65, 7700000000032, 18200.00, 0.00),
(131, '2025-11-24 22:07:17.547090', 'SALIDA_VENTA', 2, 5, 3, 'Venta en pedido #65', 65, 7700000000033, 23400.00, 0.00),
(132, '2025-11-25 00:38:59.249498', 'SALIDA_VENTA', 1, 141, 140, 'Venta en pedido #74', 74, 7700000000002, 49400.00, 0.00),
(133, '2025-11-25 00:38:59.263462', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #74', 74, 7700000000044, 36400.00, 0.00),
(134, '2025-11-25 00:38:59.266461', 'SALIDA_VENTA', 2, 4, 2, 'Venta en pedido #74', 74, 7700000000043, 15600.00, 0.00),
(135, '2025-11-25 00:51:27.482416', 'SALIDA_VENTA', 1, 159, 158, 'Venta en pedido #75', 75, 7700000000005, 75400.00, 0.00),
(136, '2025-11-25 00:51:27.482416', 'SALIDA_VENTA', 1, 5, 4, 'Venta en pedido #75', 75, 7700000000041, 62400.00, 0.00),
(137, '2025-11-25 00:51:27.482416', 'SALIDA_VENTA', 2, 4, 2, 'Venta en pedido #75', 75, 7700000000042, 19500.00, 0.00),
(138, '2025-11-25 00:58:41.658609', 'SALIDA_VENTA', 2, 2, 0, 'Venta en pedido #76', 76, 7700000000043, 15600.00, 0.00),
(139, '2025-11-25 00:58:41.658609', 'SALIDA_VENTA', 2, 2, 0, 'Venta en pedido #76', 76, 7700000000042, 19500.00, 0.00),
(140, '2025-11-25 00:58:41.675256', 'SALIDA_VENTA', 2, 4, 2, 'Venta en pedido #76', 76, 7700000000041, 62400.00, 0.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notificaciones_problema`
--

CREATE TABLE `notificaciones_problema` (
  `idNotificacion` int(11) NOT NULL,
  `motivo` longtext NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `fechaReporte` datetime(6) NOT NULL,
  `leida` tinyint(1) NOT NULL,
  `idPedido` int(11) NOT NULL,
  `fecha_respuesta` datetime(6) DEFAULT NULL,
  `respuesta_admin` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `notificaciones_problema`
--

INSERT INTO `notificaciones_problema` (`idNotificacion`, `motivo`, `foto`, `fechaReporte`, `leida`, `idPedido`, `fecha_respuesta`, `respuesta_admin`) VALUES
(1, 'no', 'problemas_entrega/27_06.png', '2025-11-21 00:45:05.004077', 1, 4, '2025-11-21 00:58:47.157933', 'lamentamos las molestias por favor tendra respuesta en su correo sobre devolucion o lo que paso con su pedido\r\n'),
(2, 'no lo recibi', 'problemas_entrega/2025-09-08_3.png', '2025-11-21 01:16:15.574291', 1, 17, '2025-11-21 01:17:26.133613', 'lamentamos que no lo haya recibido noscomunicaremos a su correo con una respuesta de resmbolso o mas informacion de lo sucedido'),
(3, 'nolo recibi', 'problemas_entrega/pestanina.webp', '2025-11-22 01:41:59.492834', 0, 16, NULL, NULL),
(4, 'll', 'problemas_entrega/pestanina_gY7pDjL.webp', '2025-11-22 01:42:53.306070', 0, 13, NULL, NULL),
(5, 'no recibi mi pedido', 'problemas_entrega/pinta_cejaz.avif', '2025-11-24 08:30:31.920104', 1, 36, '2025-11-24 08:54:53.131555', 'lo sentimis muvho'),
(6, 'no recibi mi pedido', 'problemas_entrega/p.webp', '2025-11-24 13:03:29.320505', 1, 37, '2025-11-24 13:05:02.104185', 'lamentamos los inconvenientes nos contactaremos contigo por correo para hacer el reembolso de tu pedido');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidoproducto`
--

CREATE TABLE `pedidoproducto` (
  `idPedido` int(11) NOT NULL,
  `idProducto` bigint(20) NOT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `idPedido` int(11) NOT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `fechaCreacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `fechaEntrega` date DEFAULT NULL,
  `estado` varchar(20) DEFAULT 'Pendiente',
  `total` decimal(12,2) DEFAULT NULL,
  `requiere_verificacion_pago` tinyint(1) DEFAULT 0,
  `idRepartidor` int(11) DEFAULT NULL,
  `direccionEntrega` varchar(30) DEFAULT NULL,
  `estado_pago` varchar(20) NOT NULL DEFAULT 'Pago Completo',
  `estado_pedido` varchar(20) NOT NULL DEFAULT 'Confirmado',
  `fechaVencimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`idPedido`, `idCliente`, `fechaCreacion`, `fechaEntrega`, `estado`, `total`, `requiere_verificacion_pago`, `idRepartidor`, `direccionEntrega`, `estado_pago`, `estado_pedido`, `fechaVencimiento`) VALUES
(2, 1, '2025-10-21 15:38:00', '2025-10-22', 'aprobado', 256330.00, 0, 17, NULL, 'Pago Completo', 'Entregado', '2025-10-24'),
(3, 1, '2025-10-21 16:27:00', NULL, 'aprobado', 63550.00, 0, 17, NULL, 'Pago Completo', 'Entregado', '2025-10-24'),
(4, 1, '2025-10-23 02:10:55', NULL, 'Problema en Entrega', 63550.00, 0, 17, NULL, 'Pago Completo', 'Entregado', '2025-10-27'),
(5, 1, '2025-10-23 02:12:25', NULL, 'Problema en Entrega', 36775.00, 0, 17, NULL, 'Pago Completo', 'Entregado', '2025-10-27'),
(6, 1, '2025-10-23 02:22:00', NULL, 'aprobado', 206350.00, 0, 17, NULL, 'Pago Completo', 'Entregado', '2025-10-27'),
(9, 1, '2025-11-07 13:30:58', NULL, 'pendiente', 46890.00, 1, 15, 'Calle Principal #123', 'Pago Completo', 'Entregado', '2025-11-12'),
(10, 1, '2025-11-07 13:31:21', NULL, 'pendiente', 36890.00, 1, 15, 'Calle Principal #123', 'Pago Parcial', 'Entregado', '2025-11-12'),
(12, 1, '2025-11-13 04:31:37', NULL, 'Pago Completo', 10000.00, 0, 15, NULL, 'Pago Completo', 'Entregado', '2025-11-17'),
(13, 1, '2025-11-13 06:22:56', NULL, 'Problema en Entrega', 10000.00, 0, 15, NULL, 'Pago Completo', 'Entregado', '2025-11-18'),
(14, 1, '2025-11-13 07:21:37', NULL, 'Pago Completo', 48080.00, 0, 16, NULL, 'Pago Completo', 'Entregado', '2025-11-18'),
(15, 1, '2025-11-13 07:37:00', NULL, 'Pago Completo', 134950.00, 0, 16, NULL, 'Pago Completo', 'Entregado', '2025-11-18'),
(16, 1, '2025-11-13 07:37:53', NULL, 'Problema en Entrega', 24280.00, 0, 16, NULL, 'Pago Completo', 'Entregado', '2025-11-18'),
(17, 1, '2025-11-13 11:19:28', NULL, 'Problema en Entrega', 48080.00, 0, 16, NULL, 'Pago Completo', 'Entregado', '2025-11-18'),
(18, 1, '2025-11-13 11:48:54', NULL, 'Completado', 168270.00, 0, 16, NULL, 'Pago Completo', 'Entregado', '2025-11-18'),
(20, 13, '2025-11-20 13:14:00', NULL, 'Pago Parcial', 21420.00, 0, 16, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(21, 13, '2025-11-20 13:27:44', NULL, 'Pago Parcial', 38080.00, 0, 16, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(22, 13, '2025-11-20 13:30:46', NULL, 'Pago Parcial', 38080.00, 0, 16, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(23, 13, '2025-11-20 15:26:57', NULL, 'Pago Parcial', 17850.00, 0, 5, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(24, 13, '2025-11-20 15:28:42', NULL, 'Pago Parcial', 16660.00, 0, 5, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(25, 13, '2025-11-20 15:53:40', NULL, 'Pago Parcial', 38080.00, 0, 5, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(26, 13, '2025-11-20 16:13:31', NULL, 'Pago Parcial', 45220.00, 0, 5, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(27, 13, '2025-11-20 18:59:45', NULL, 'Pago Parcial', 38080.00, 0, 5, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(28, 13, '2025-11-20 19:03:10', NULL, 'Pago Parcial', 16660.00, 0, 4, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(33, 15, '2025-11-20 19:54:00', NULL, 'Pago Parcial', 74970.00, 0, 4, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(34, 15, '2025-11-20 20:05:09', NULL, 'Pago Parcial', 21420.00, 0, 4, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(35, 15, '2025-11-20 20:12:06', NULL, 'Pago Parcial', 40460.00, 0, 4, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(36, 15, '2025-11-20 20:20:36', NULL, 'Pago Parcial', 21420.00, 0, 4, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(37, 17, '2025-11-21 00:32:13', NULL, 'Pago Parcial', 65450.00, 0, 15, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(38, 17, '2025-11-21 01:06:53', NULL, 'En Camino', 57600.00, 0, 15, NULL, 'Pago Completo', 'Entregado', '2025-11-25'),
(39, 18, '2025-11-21 01:08:27', NULL, 'Pago Parcial', 40460.00, 0, 15, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(40, 18, '2025-11-21 01:13:13', NULL, 'Pago Parcial', 49980.00, 0, 15, NULL, 'Pago Parcial', 'Entregado', '2025-11-25'),
(43, 20, '2025-11-22 00:53:43', NULL, 'Pago Parcial', 141610.00, 0, 15, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(44, 20, '2025-11-22 00:58:29', NULL, 'Pago Parcial', 42840.00, 0, 15, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(45, 20, '2025-11-22 01:12:30', NULL, 'Pago Parcial', 61880.00, 0, 15, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(46, 20, '2025-11-22 01:21:06', NULL, 'Pago Parcial', 91630.00, 0, 15, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(47, 20, '2025-11-22 01:35:57', NULL, 'Pago Parcial', 38080.00, 0, 18, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(48, 20, '2025-11-22 01:36:36', NULL, 'Pago Parcial', 21420.00, 0, 18, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(50, 1, '2025-11-22 02:07:26', NULL, 'Pago Parcial', 0.00, 0, 18, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(51, 1, '2025-11-22 02:07:26', NULL, 'Pago Parcial', 0.00, 0, 18, NULL, 'Pago Parcial', 'Entregado', '2025-11-26'),
(52, 20, '2025-11-22 02:52:36', NULL, 'Pago Parcial', 93300.00, 0, 18, NULL, 'Pago Completo', 'Entregado', '2025-11-26'),
(53, 22, '2025-11-24 08:16:01', NULL, 'Pago Parcial', 93300.00, 0, 2, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(54, 22, '2025-11-24 08:27:11', NULL, 'Pago Completo', 44510.00, 0, 2, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(55, 22, '2025-11-24 08:42:02', NULL, 'Pago Parcial', 84970.00, 0, 2, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(56, 22, '2025-11-24 08:47:46', NULL, 'Confirmado', 71400.00, 0, 2, NULL, 'Pago Parcial', 'En Camino', '2025-11-27'),
(57, 22, '2025-11-24 08:52:55', NULL, 'Confirmado', 39270.00, 0, 4, NULL, 'Pago Parcial', 'En Camino', '2025-11-27'),
(58, 23, '2025-11-24 11:38:41', NULL, 'Confirmado', 42840.00, 0, 4, NULL, 'Pago Parcial', 'En Camino', '2025-11-27'),
(59, 23, '2025-11-24 19:45:27', NULL, 'Confirmado', 124240.00, 0, 4, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(60, 23, '2025-11-24 19:46:43', NULL, 'Confirmado', 61880.00, 0, 4, NULL, 'Pago Parcial', 'En Camino', '2025-11-27'),
(61, 23, '2025-11-24 20:07:39', NULL, 'Confirmado', 240860.00, 0, 5, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(62, 23, '2025-11-24 20:11:05', NULL, 'Confirmado', 40940.00, 0, 5, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(63, 24, '2025-11-24 21:40:36', NULL, 'Confirmado', 48080.00, 0, 5, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(64, 23, '2025-11-24 21:42:51', NULL, 'Confirmado', 173030.00, 0, 5, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(65, 23, '2025-11-24 22:07:17', NULL, 'Confirmado', 77350.00, 0, 15, NULL, 'Pago Parcial', 'En Camino', '2025-11-27'),
(74, 25, '2025-11-25 00:38:59', NULL, 'Confirmado', 139230.00, 0, 15, NULL, 'Pago Parcial', 'En Camino', '2025-11-27'),
(75, 26, '2025-11-25 00:51:27', NULL, 'Confirmado', 220392.00, 0, 15, NULL, 'Pago Completo', 'En Camino', '2025-11-27'),
(76, 26, '2025-11-25 00:58:41', NULL, 'Confirmado', 232050.00, 0, 19, NULL, 'Pago Parcial', 'En Camino', '2025-11-27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

CREATE TABLE `perfil` (
  `idProfile` int(11) NOT NULL,
  `usuario` int(11) NOT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `descripcion` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `idProducto` bigint(20) NOT NULL,
  `nombreProducto` varchar(50) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `lote` varchar(20) DEFAULT NULL,
  `cantidadDisponible` int(11) DEFAULT 0,
  `fechaIngreso` timestamp NOT NULL DEFAULT current_timestamp(),
  `fechaVencimiento` date DEFAULT NULL,
  `idCategoria` int(11) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `idSubcategoria` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`idProducto`, `nombreProducto`, `precio`, `descripcion`, `lote`, `cantidadDisponible`, `fechaIngreso`, `fechaVencimiento`, `idCategoria`, `imagen`, `idSubcategoria`, `stock`) VALUES
(7700000000001, 'Rubor Rosado Glow', 32000.00, 'Rubor en polvo con acabado satinado y pigmento suave.', 'L2025-11', 50, '2025-11-07 07:01:07', '2027-11-01', 1, 'productos/rubor.jpg', 4, 174),
(7700000000002, 'Iluminador Perla Glam', 38000.00, 'Ilumina tus mejillas con un brillo nacarado y elegante.', 'L2025-11', 35, '2025-11-07 07:01:07', '2027-11-01', 1, 'productos/ilumi_p.webp', 5, 140),
(7700000000003, 'Corrector Liquido Soft Touch', 29000.00, 'Cobertura media con textura ligera y acabado natural.', 'L2025-11', 40, '2025-11-07 07:01:07', '2027-11-01', 1, 'productos/corrector.avif', 2, 149),
(7700000000004, 'Polvo Compacto Mate Glam', 34000.00, 'Controla el brillo con un acabado mate y aterciopelado.', 'L2025-11', 45, '2025-11-07 07:01:07', '2027-11-01', 1, 'productos/base_polvo.webp', 3, 155),
(7700000000005, 'Base Cushion Glo', 58000.00, 'Base ligera con esponja cushion y efecto luminoso.', 'L2025-11', 30, '2025-11-07 07:01:07', '2027-11-01', 1, 'productos/base.png', 1, 158),
(7700000000011, 'Sombra Cuarteto Rosa', 42000.00, 'Paleta de 4 tonos rosados con acabado satinado.', 'L2025-11', 50, '2025-11-07 07:01:16', '2027-11-01', 2, 'productos/s.jpg', 6, 101),
(7700000000012, 'Delineador Liquido Precisio', 18000.00, 'Punta fina para trazos definidos y resistentes al agua.', 'L2025-11', 60, '2025-11-07 07:01:16', '2027-11-01', 2, 'productos/delini.webp', 7, 101),
(7700000000013, 'Pestañina Curvas Glam', 16000.00, 'Define y curva tus pesta?as con f?rmula ligera.', 'L2025-11', 40, '2025-11-07 07:01:16', '2026-11-01', 2, 'productos/pestanina.webp', 8, 50),
(7700000000014, 'Gel para Cejas Natural Brow', 20000.00, 'Fija y da forma a tus cejas con acabado natural.', 'L2025-11', 35, '2025-11-07 07:01:16', '2027-11-01', 2, 'productos/pinta_cejaz.avif', 9, 38),
(7700000000015, 'Sombra Liquida Glitter Pop', 25000.00, 'Brillo liquido para parpados con efecto multidimensional.', 'L2025-11', 30, '2025-11-07 07:01:16', '2027-11-01', 2, 'productos/l.webp', 6, 5),
(7700000000021, 'Brillo Labial Cristal', 22000.00, 'Gloss transparente con efecto volumen y aroma a vainilla.', 'L2025-11', 50, '2025-11-07 07:01:25', '2027-11-01', 3, 'productos/ll.webp', 11, 13),
(7700000000023, 'Balsamo Hidratante Berry Kis', 18000.00, 'Hidratacion profunda con aroma a frutos rojos.', 'L2025-11', 60, '2025-11-07 07:01:25', '2027-11-01', 3, 'productos/balsamo.webp', 12, 120),
(7700000000024, 'Delineador de Labios Coral Chic', 15000.00, 'Define y realza con precisi?n y suavidad.', 'L2025-11', 35, '2025-11-07 07:01:25', '2027-11-01', 3, 'productos/dd.webp', 13, 3),
(7700000000025, 'Labial Cremoso Fucsia Pop', 30000.00, 'Color vibrante con textura cremosa y humectante.', 'L2025-11', 45, '2025-11-07 07:01:25', '2027-11-01', 3, 'productos/la.webp', 10, 4),
(7700000000031, 'Esmalte Rosa Pastel', 12000.00, 'Color suave, f?rmula vegana y secado r?pido.', 'L2025-11', 50, '2025-11-07 07:01:33', '2027-11-01', 4, 'productos/esm.webp', 14, 4),
(7700000000032, 'Top Coat Brillo Extremo', 14000.00, 'Protecci?n y brillo espejo para tus u?as.', 'L2025-11', 40, '2025-11-07 07:01:33', '2027-11-01', 4, 'productos/top.jpg', 15, 11),
(7700000000033, 'Tratamiento Fortalecedor', 18000.00, 'Fortalece u?as quebradizas con queratina y calcio.', 'L2025-11', 30, '2025-11-07 07:01:33', '2027-11-01', 4, 'productos/tr.webp', 15, 3),
(7700000000034, 'Esmalte Glitter Champagne', 15000.00, 'Brillo dorado para un acabado festivo y glamuroso.', 'L2025-11', 35, '2025-11-07 07:01:33', '2027-11-01', 4, 'productos/ess.webp', 14, 5),
(7700000000035, 'Kit Decoracion de Uñas', 5000.00, 'Piedras, stickers y pinceles para dise?os creativos.', 'L2025-11', 20, '2025-11-07 07:01:33', '2027-11-01', 4, 'productos/ki.webp', 16, 5),
(7700000000041, 'Set de Brochas Rosa Gold', 48000.00, '10 brochas suaves para rostro y ojos en estuche glam.', 'L2025-11', 25, '2025-11-07 07:01:41', '2028-01-01', 5, 'productos/br.webp', 17, 2),
(7700000000042, 'Esponja Blender Lavanda', 15000.00, 'Esponja suave para base y corrector, acabado uniforme.', 'L2025-11', 40, '2025-11-07 07:01:41', '2028-01-01', 5, 'productos/esp.webp', 18, 0),
(7700000000043, 'Pinza de Cejas Glam', 12000.00, 'Precision y diseño ergonomico en acabado metalico rosado.', 'L2025-11', 50, '2025-11-07 07:01:41', '2028-01-01', 5, 'productos/pinzas.webp', 9, 0),
(7700000000044, 'Organizador Acrilico Mini', 28000.00, 'Guarda tus productos con estilo y orden.', 'L2025-11', 30, '2025-11-07 07:01:41', '2028-01-01', 5, 'productos/o.webp', 19, 4),
(7700000000045, 'Espejo LED Glam', 35000.00, 'Espejo compacto con luz LED y aumento x5.', 'L2025-11', 20, '2025-11-07 07:01:41', '2028-01-01', 5, 'productos/es.jpg', NULL, 5),
(7701122334455, 'Labial Mate Velvet Glam', 5000.00, 'Color intenso, textura aterciopelada, larga duraci?n', 'L2025-11', 40, '2025-11-05 15:45:00', '2027-05-05', 3, 'productos/red_velved.jpg', 10, 5),
(7701234567890, 'Base Liquida HD Glam', 55000.00, 'Cobertura alta, acabado natural, ideal para piel mixta', 'L2025-10', 25, '2025-11-05 15:45:00', '2027-11-05', 1, 'productos/otra_b.webp', 1, 42),
(7709876543210, 'Pestañina Volumen Total Gla', 15000.00, 'Volumen extremo, resistente al agua, f?rmula vegana', 'L2025-11', 30, '2025-11-05 15:45:00', '2026-11-05', 2, 'productos/p.webp', 8, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `repartidores`
--

CREATE TABLE `repartidores` (
  `idRepartidor` int(11) NOT NULL,
  `nombreRepartidor` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `estado_turno` varchar(20) DEFAULT 'Disponible',
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `repartidores`
--

INSERT INTO `repartidores` (`idRepartidor`, `nombreRepartidor`, `telefono`, `estado_turno`, `email`) VALUES
(2, 'Juan Pérez', '3001112222', 'Disponible', NULL),
(4, 'Carlos Martínez', '3005556666', 'En Ruta', NULL),
(5, 'Ana Torre', '3007778888', 'En Ruta', NULL),
(15, 'lauren', '3024892804', 'En Ruta', 'laurensamanta0.r@gmail.com'),
(16, 'michael ', '3024892804', 'En Ruta', 'michaeldaramirez117@gmail.com'),
(17, 'lauren oo', '+573024892804', 'En Ruta', 'lausamanta2024cha@gmail.com'),
(18, 'lauren sam', '3024892804', 'En Ruta', 'lauren.20031028@gmail.com'),
(19, 'william', '315156165984', 'En Ruta', 'fontequin@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `nombre_rol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `nombre_rol`) VALUES
(1, 'Administrador'),
(2, 'Cliente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subcategorias`
--

CREATE TABLE `subcategorias` (
  `idSubcategoria` int(11) NOT NULL,
  `nombreSubcategoria` varchar(50) NOT NULL,
  `idCategoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `subcategorias`
--

INSERT INTO `subcategorias` (`idSubcategoria`, `nombreSubcategoria`, `idCategoria`) VALUES
(1, 'Base', 1),
(2, 'Correctores', 1),
(3, 'Polvos compactos', 1),
(4, 'Rubores', 1),
(5, 'Iluminadores', 1),
(6, 'Sombras', 2),
(7, 'Delineadores', 2),
(8, 'Pestañas', 2),
(9, 'Cejas', 2),
(10, 'Labiales', 3),
(11, 'Brillos', 3),
(12, 'B?lsamos', 3),
(13, 'Delineadores de labios', 3),
(14, 'Esmaltes', 4),
(15, 'Tratamientos', 4),
(16, 'Decoraci?n', 4),
(17, 'Brochas', 5),
(18, 'Esponjas', 5),
(19, 'Organizadores', 5),
(25, 'espejo', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `id_rol` int(11) NOT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `fechaCreacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `nombre` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(50) DEFAULT NULL,
  `reset_token` varchar(255) DEFAULT NULL,
  `reset_token_expires` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `email`, `password`, `id_rol`, `idCliente`, `fechaCreacion`, `nombre`, `telefono`, `direccion`, `reset_token`, `reset_token_expires`) VALUES
(1, 'admin@glamstore.com', 'pbkdf2_sha256$600000$v0KrjVeHKRquT0I2cEMaFM$69UwlerF+a3XiYIroFZyYoW+/O/U+r4GSFFJn47QqwQ=', 1, NULL, '2025-10-21 15:03:52', 'lauren', '3024892804', 'calle 123 #12b -15', NULL, NULL),
(4, 'nuevo_email@test.com', 'pbkdf2_sha256$600000$2GjwPnRqbBwsf0Hh4D2jSk$Wp7kO4brpIjZhwsF1DB2TMVZull6U3lwuGqGnvwlJag=', 2, 1, '2025-10-21 15:05:26', 'Cliente Uno', '3001234567', 'Calle 45 #10-20', NULL, NULL),
(10, 'glamstore0303777@gmail.com', 'pbkdf2_sha256$600000$a0L7aDK80j1CLRTR5RJvIp$qdik3hQ6NXt2Av4wMn6hdWjeQYltQOEZ0BHIIfjvz20=', 1, NULL, '2025-11-11 05:42:06', 'Admin Glam Stor', '3000000000', 'Calle Glam 123', NULL, NULL),
(12, 'cliente3@gmail.com', 'pbkdf2_sha256$600000$8TudOY3FCiujKwuPYT4umM$NbSsig85Vt7P+5S15Y9nc/d926fI/jZA33WRDanzi3U=', 2, NULL, '2025-11-13 12:31:42', 'lauren', NULL, NULL, NULL, NULL),
(13, 'carlos@gmail.com', 'pbkdf2_sha256$600000$8mg0LPZXcRLCP6QcLKJMt5$kr7LUCH3bhJPNvCwRGJuvc6RS4pkkeIkKe1VAP0WLRk=', 2, 13, '2025-11-20 15:29:27', 'william fontecha', NULL, NULL, NULL, NULL),
(15, 'lala@gmail.com', 'pbkdf2_sha256$600000$7Y5ziRSkMs2SgM2s4IsVTU$7ZGOqbaaiOZHsjC5ADJxvB2oNFpdqNFtyer3CrOCsHY=', 2, 15, '2025-11-20 20:00:54', 'lala', NULL, NULL, NULL, NULL),
(16, 'lauratorres@gmail.com', 'pbkdf2_sha256$600000$eKBznW1t5RuW3ZvGjZC272$bGZtIpV1xV2d4l9gb1I/xtV7hSmEQccz8RtWMJRfSsY=', 2, 17, '2025-11-21 00:31:04', 'Laura Torres', NULL, NULL, NULL, NULL),
(17, 'lauratibaque@gmail.com', 'pbkdf2_sha256$600000$EW31JEdw1CAM0cSH6HrGGZ$Hw70/NF/XmEC+L9Xm09yk8zshMutit2l9iLeVG2/wfc=', 2, 18, '2025-11-21 01:09:23', 'laura tibaque', NULL, NULL, NULL, NULL),
(18, 'laurensamanta0.r@gmail.com', 'pbkdf2_sha256$600000$rXISs5aJsAVneqcIUur5PV$142Pz/E/o7i6bh5hOUjFFkpQMhbgrjFzxd4l1HXW5o8=', 2, 20, '2025-11-22 00:54:06', 'Lauren Samanta Ortiz ', NULL, NULL, NULL, NULL),
(19, 'jeimycontreras11@gmail.com', 'pbkdf2_sha256$600000$sG1heKNYr9XL6z9WpFCfFJ$ZMphBsfGupL0S58xJHh0FNH0YqU9++MNsi6CyBUGl00=', 2, NULL, '2025-11-22 01:51:09', 'jeimy contreras', NULL, NULL, NULL, NULL),
(20, 'michael@gmail.com', 'pbkdf2_sha256$600000$OcTE5rXFLSMYvikPwl5PK7$34sWZ+wh8y3HeSf3mEHXcxyRudjPlfuLMbtRX1x0yP8=', 2, 22, '2025-11-24 08:27:50', 'michael', NULL, NULL, NULL, NULL),
(21, 'admin123@glamstore.com', 'pbkdf2_sha256$600000$fEst2PshhAQj6hXXxFFlwB$M5PfFmSqRIhwdJEpSI3gGYJv3tol6P6PSxMzfneB/Gc=', 1, NULL, '2025-11-24 13:40:20', 'Lauren Samanta Ortiz ', NULL, NULL, NULL, NULL),
(22, 'alejandro@gmail.com', 'pbkdf2_sha256$600000$jIQApXMzVsRBNRzOiyu37G$GOX1jX5vNWHYTuWQE93jz1odB8uG+AL/RYRQvo3qUMk=', 2, 23, '2025-11-24 11:39:59', 'alejandro', NULL, NULL, NULL, NULL),
(23, 'lausamanta2024cha@gmail.com', 'pbkdf2_sha256$600000$SbH8Xv3ygscunBND2Xpfiy$HBSa3J1cJb6j9hhUT4zQge5qXs3UBYgNxIWkxbsRoEk=', 2, 25, '2025-11-25 00:40:58', 'magda maria', NULL, NULL, NULL, NULL),
(24, 'lauren.20031028@gmail.com', 'pbkdf2_sha256$600000$0BxMzoPQJOENk4LUDgqAYd$Yzjlza/jvRWSvkr/XT7C/3soNIMuX9dVy1fqy3OIRzg=', 2, 26, '2025-11-25 00:52:39', 'maria magdalena', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_facturas_detalladas`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_facturas_detalladas` (
`idFactura` int(11)
,`fechaEmision` timestamp
,`estado_factura` varchar(20)
,`montoTotal` decimal(10,2)
,`idPedido` int(11)
,`cliente` varchar(100)
,`correo_cliente` varchar(100)
,`metodo_pago` varchar(50)
,`descripcion` text
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_historial_cliente`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_historial_cliente` (
`idCliente` int(1)
,`cliente` int(1)
,`email` int(1)
,`idPedido` int(1)
,`fechaCreacion` int(1)
,`fechaEntrega` int(1)
,`estado` int(1)
,`total` int(1)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_pedidos_distribuidores`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_pedidos_distribuidores` (
`idDistribuidor` int(1)
,`distribuidor` int(1)
,`idPedido` int(1)
,`fechaCreacion` int(1)
,`fechaEntrega` int(1)
,`estado_pedido` int(1)
,`idCliente` int(1)
,`cliente` int(1)
,`direccion_cliente` int(1)
,`idProducto` int(1)
,`producto` int(1)
,`cantidad` int(1)
,`precio` int(1)
,`subtotal` int(1)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_pedidos_repartidor`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_pedidos_repartidor` (
`idRepartidor` int(1)
,`repartidor` int(1)
,`telefono_repartidor` int(1)
,`idPedido` int(1)
,`cliente` int(1)
,`telefono_cliente` int(1)
,`direccion_entrega` int(1)
,`estado_pedido` int(1)
,`monto_total` int(1)
,`fechaEntrega` int(1)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_productos_categoria`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_productos_categoria` (
`idProducto` int(1)
,`nombreProducto` int(1)
,`precio` int(1)
,`descripcion` int(1)
,`cantidadDisponible` int(1)
,`categoria` int(1)
,`descripcionCategoria` int(1)
,`fechaIngreso` int(1)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_productos_distribuidor`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_productos_distribuidor` (
`idDistribuidor` int(1)
,`distribuidor` int(1)
,`idProducto` int(1)
,`producto` int(1)
,`precio` int(1)
,`stock` int(1)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_facturas_detalladas`
--
DROP TABLE IF EXISTS `vista_facturas_detalladas`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_facturas_detalladas`  AS SELECT `f`.`idFactura` AS `idFactura`, `f`.`fechaEmision` AS `fechaEmision`, `f`.`estado` AS `estado_factura`, `f`.`montoTotal` AS `montoTotal`, `p`.`idPedido` AS `idPedido`, `c`.`nombre` AS `cliente`, `c`.`email` AS `correo_cliente`, `m`.`tipo` AS `metodo_pago`, `m`.`descripcion` AS `descripcion` FROM (((`facturas` `f` join `pedidos` `p` on(`f`.`idPedido` = `p`.`idPedido`)) join `clientes` `c` on(`p`.`idCliente` = `c`.`idCliente`)) left join `metodospago` `m` on(`f`.`idMetodoPago` = `m`.`idMetodoPago`)) ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_historial_cliente`
--
DROP TABLE IF EXISTS `vista_historial_cliente`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_historial_cliente`  AS SELECT 1 AS `idCliente`, 1 AS `cliente`, 1 AS `email`, 1 AS `idPedido`, 1 AS `fechaCreacion`, 1 AS `fechaEntrega`, 1 AS `estado`, 1 AS `total` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_pedidos_distribuidores`
--
DROP TABLE IF EXISTS `vista_pedidos_distribuidores`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_pedidos_distribuidores`  AS SELECT 1 AS `idDistribuidor`, 1 AS `distribuidor`, 1 AS `idPedido`, 1 AS `fechaCreacion`, 1 AS `fechaEntrega`, 1 AS `estado_pedido`, 1 AS `idCliente`, 1 AS `cliente`, 1 AS `direccion_cliente`, 1 AS `idProducto`, 1 AS `producto`, 1 AS `cantidad`, 1 AS `precio`, 1 AS `subtotal` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_pedidos_repartidor`
--
DROP TABLE IF EXISTS `vista_pedidos_repartidor`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_pedidos_repartidor`  AS SELECT 1 AS `idRepartidor`, 1 AS `repartidor`, 1 AS `telefono_repartidor`, 1 AS `idPedido`, 1 AS `cliente`, 1 AS `telefono_cliente`, 1 AS `direccion_entrega`, 1 AS `estado_pedido`, 1 AS `monto_total`, 1 AS `fechaEntrega` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_productos_categoria`
--
DROP TABLE IF EXISTS `vista_productos_categoria`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_productos_categoria`  AS SELECT 1 AS `idProducto`, 1 AS `nombreProducto`, 1 AS `precio`, 1 AS `descripcion`, 1 AS `cantidadDisponible`, 1 AS `categoria`, 1 AS `descripcionCategoria`, 1 AS `fechaIngreso` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_productos_distribuidor`
--
DROP TABLE IF EXISTS `vista_productos_distribuidor`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_productos_distribuidor`  AS SELECT 1 AS `idDistribuidor`, 1 AS `distribuidor`, 1 AS `idProducto`, 1 AS `producto`, 1 AS `precio`, 1 AS `stock` ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`idCategoria`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`idCliente`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `core_notificacion`
--
ALTER TABLE `core_notificacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_notificacion_usuario_id_f14c4107_fk_auth_user_id` (`usuario_id`);

--
-- Indices de la tabla `core_profile`
--
ALTER TABLE `core_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `detallepedido`
--
ALTER TABLE `detallepedido`
  ADD PRIMARY KEY (`idDetalle`),
  ADD KEY `idPedido` (`idPedido`),
  ADD KEY `detallepedido_ibfk_2` (`idProducto`);

--
-- Indices de la tabla `distribuidores`
--
ALTER TABLE `distribuidores`
  ADD PRIMARY KEY (`idDistribuidor`);

--
-- Indices de la tabla `distribuidorproducto`
--
ALTER TABLE `distribuidorproducto`
  ADD PRIMARY KEY (`idDistribuidor`,`idProducto`),
  ADD KEY `idProducto` (`idProducto`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD PRIMARY KEY (`idFactura`),
  ADD KEY `idPedido` (`idPedido`),
  ADD KEY `idMetodoPago` (`idMetodoPago`);

--
-- Indices de la tabla `mensajecontacto`
--
ALTER TABLE `mensajecontacto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  ADD PRIMARY KEY (`idMensaje`);

--
-- Indices de la tabla `metodospago`
--
ALTER TABLE `metodospago`
  ADD PRIMARY KEY (`idMetodoPago`);

--
-- Indices de la tabla `movimientos_producto`
--
ALTER TABLE `movimientos_producto`
  ADD PRIMARY KEY (`idMovimiento`),
  ADD KEY `movimientos_producto_idPedido_f819b66b_fk_pedidos_idPedido` (`idPedido`),
  ADD KEY `movimientos_producto_producto_id_a133645f_fk_productos` (`producto_id`);

--
-- Indices de la tabla `notificaciones_problema`
--
ALTER TABLE `notificaciones_problema`
  ADD PRIMARY KEY (`idNotificacion`),
  ADD KEY `notificaciones_problema_idPedido_2316d01a_fk_pedidos_idPedido` (`idPedido`);

--
-- Indices de la tabla `pedidoproducto`
--
ALTER TABLE `pedidoproducto`
  ADD PRIMARY KEY (`idPedido`,`idProducto`),
  ADD KEY `idProducto` (`idProducto`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`idPedido`),
  ADD KEY `idCliente` (`idCliente`),
  ADD KEY `idRepartidor` (`idRepartidor`),
  ADD KEY `idx_fecha_vencimiento` (`fechaVencimiento`);

--
-- Indices de la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD PRIMARY KEY (`idProfile`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`idProducto`),
  ADD KEY `fk_productos_categorias` (`idCategoria`),
  ADD KEY `fk_subcategoria_producto` (`idSubcategoria`);

--
-- Indices de la tabla `repartidores`
--
ALTER TABLE `repartidores`
  ADD PRIMARY KEY (`idRepartidor`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `subcategorias`
--
ALTER TABLE `subcategorias`
  ADD PRIMARY KEY (`idSubcategoria`),
  ADD KEY `idCategoria` (`idCategoria`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `id_rol` (`id_rol`),
  ADD KEY `idCliente` (`idCliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `idCategoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `core_notificacion`
--
ALTER TABLE `core_notificacion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `core_profile`
--
ALTER TABLE `core_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `detallepedido`
--
ALTER TABLE `detallepedido`
  MODIFY `idDetalle` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=120;

--
-- AUTO_INCREMENT de la tabla `distribuidores`
--
ALTER TABLE `distribuidores`
  MODIFY `idDistribuidor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `facturas`
--
ALTER TABLE `facturas`
  MODIFY `idFactura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `mensajecontacto`
--
ALTER TABLE `mensajecontacto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  MODIFY `idMensaje` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `metodospago`
--
ALTER TABLE `metodospago`
  MODIFY `idMetodoPago` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `movimientos_producto`
--
ALTER TABLE `movimientos_producto`
  MODIFY `idMovimiento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=141;

--
-- AUTO_INCREMENT de la tabla `notificaciones_problema`
--
ALTER TABLE `notificaciones_problema`
  MODIFY `idNotificacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `idPedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT de la tabla `perfil`
--
ALTER TABLE `perfil`
  MODIFY `idProfile` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `idProducto` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7709876543220;

--
-- AUTO_INCREMENT de la tabla `repartidores`
--
ALTER TABLE `repartidores`
  MODIFY `idRepartidor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `subcategorias`
--
ALTER TABLE `subcategorias`
  MODIFY `idSubcategoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `core_notificacion`
--
ALTER TABLE `core_notificacion`
  ADD CONSTRAINT `core_notificacion_usuario_id_f14c4107_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `detallepedido`
--
ALTER TABLE `detallepedido`
  ADD CONSTRAINT `detallepedido_ibfk_1` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `detallepedido_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `productos` (`idProducto`);

--
-- Filtros para la tabla `distribuidorproducto`
--
ALTER TABLE `distribuidorproducto`
  ADD CONSTRAINT `distribuidorproducto_ibfk_1` FOREIGN KEY (`idDistribuidor`) REFERENCES `distribuidores` (`idDistribuidor`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`),
  ADD CONSTRAINT `facturas_ibfk_2` FOREIGN KEY (`idMetodoPago`) REFERENCES `metodospago` (`idMetodoPago`);

--
-- Filtros para la tabla `movimientos_producto`
--
ALTER TABLE `movimientos_producto`
  ADD CONSTRAINT `movimientos_producto_idPedido_f819b66b_fk_pedidos_idPedido` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`),
  ADD CONSTRAINT `movimientos_producto_producto_id_a133645f_fk_productos` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`idProducto`);

--
-- Filtros para la tabla `notificaciones_problema`
--
ALTER TABLE `notificaciones_problema`
  ADD CONSTRAINT `notificaciones_problema_idPedido_2316d01a_fk_pedidos_idPedido` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`);

--
-- Filtros para la tabla `pedidoproducto`
--
ALTER TABLE `pedidoproducto`
  ADD CONSTRAINT `pedidoproducto_ibfk_1` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`),
  ADD CONSTRAINT `pedidoproducto_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `productos` (`idProducto`);

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`idRepartidor`) REFERENCES `repartidores` (`idRepartidor`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk_categoria_producto` FOREIGN KEY (`idCategoria`) REFERENCES `categorias` (`idCategoria`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_productos_categorias` FOREIGN KEY (`idCategoria`) REFERENCES `categorias` (`idCategoria`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_subcategoria_producto` FOREIGN KEY (`idSubcategoria`) REFERENCES `subcategorias` (`idSubcategoria`);

--
-- Filtros para la tabla `subcategorias`
--
ALTER TABLE `subcategorias`
  ADD CONSTRAINT `subcategorias_ibfk_1` FOREIGN KEY (`idCategoria`) REFERENCES `categorias` (`idCategoria`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`),
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
