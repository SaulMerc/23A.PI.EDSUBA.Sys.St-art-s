

--
-- Servidor: localhost:3306
-- Tiempo de generación: 14-05-2023 a las 19:02:57
-- Versión del servidor: 5.7.24
-- Versión de PHP: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";




--
-- Base de datos: `db_starts`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aviso`
--

CREATE TABLE `aviso` (
  `id` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `aviso` text NOT NULL,
  `fecha` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `id` int(11) NOT NULL,
  `vendido` enum('si','no') NOT NULL DEFAULT 'no',
  `fecha_vendido` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `categoria` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comentarios`
--

CREATE TABLE `comentarios` (
  `id` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `comentario` text NOT NULL,
  `fecha` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contrasenas`
--

CREATE TABLE `contrasenas` (
  `id_usuario` int(11) NOT NULL,
  `contrasena` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direccion`
--

CREATE TABLE `direccion` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `colonia` text NOT NULL,
  `cod_postal` int(11) NOT NULL,
  `municipio` text NOT NULL,
  `calle` text NOT NULL,
  `num_ext` int(11) NOT NULL,
  `num_int` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fotos_perfil`
--

CREATE TABLE `fotos_perfil` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `imagen` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imagenes`
--

CREATE TABLE `imagenes` (
  `id` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  `imagen` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `met_pago`
--

CREATE TABLE `met_pago` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `num_tarjeta` text NOT NULL,
  `nombre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipios_jalisco`
--

CREATE TABLE `municipios_jalisco` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `municipios_jalisco`
--

INSERT INTO `municipios_jalisco` (`id`, `nombre`) VALUES
(1, 'Acatic'),
(2, 'Acatlán de Juárez'),
(3, 'Ahualulco de Mercado'),
(4, 'Amacueca'),
(5, 'Amatitán'),
(6, 'Ameca'),
(7, 'Arandas'),
(8, 'Atemajac de Brizuela'),
(9, 'Atengo'),
(10, 'Atenguillo'),
(11, 'Atotonilco el Alto'),
(12, 'Atoyac'),
(13, 'Autlán de Navarro'),
(14, 'Ayotlán'),
(15, 'Ayutla'),
(16, 'Bolaños'),
(17, 'Cabo Corrientes'),
(18, 'Cañadas de Obregón'),
(19, 'Casimiro Castillo'),
(20, 'Chapala'),
(21, 'Chimaltitán'),
(22, 'Chiquilistlán'),
(23, 'Cihuatlán'),
(24, 'Cocula'),
(25, 'Colotlán'),
(26, 'Concepción de Buenos Aires'),
(27, 'Cuautitlán de García Barragán'),
(28, 'Cuautla'),
(29, 'Cuquío'),
(30, 'Degollado'),
(31, 'Ejutla'),
(32, 'El Arenal'),
(33, 'El Grullo'),
(34, 'El Limón'),
(35, 'El Salto'),
(36, 'Encarnación de Díaz'),
(37, 'Etzatlán'),
(38, 'Gómez Farías'),
(39, 'Guachinango'),
(40, 'Guadalajara'),
(41, 'Hostotipaquillo'),
(42, 'Huejúcar'),
(43, 'Huejuquilla el Alto'),
(44, 'Ixtlahuacán de los Membrillos'),
(45, 'Ixtlahuacán del Río'),
(46, 'Jalostotitlán'),
(47, 'Jamay'),
(48, 'Jesús María'),
(49, 'Jilotlán de los Dolores'),
(50, 'Jocotepec'),
(51, 'Juanacatlán'),
(52, 'Juchitlán'),
(53, 'La Barca'),
(54, 'La Huerta'),
(55, 'La Manzanilla de la Paz'),
(56, 'Lagos de Moreno'),
(57, 'Magdalena'),
(58, 'Mascota'),
(59, 'Mazamitla'),
(60, 'Mexticacán'),
(61, 'Mezquitic'),
(62, 'Mixtlán'),
(63, 'Ocotlán'),
(64, 'Ojuelos de Jalisco'),
(65, 'Pihuamo'),
(66, 'Poncitlán'),
(67, 'Puerto Vallarta'),
(68, 'Quitupan'),
(69, 'San Cristóbal de la Barranca'),
(70, 'San Diego de Alejandría'),
(71, 'San Gabriel'),
(72, 'San Ignacio Cerro Gordo'),
(73, 'San Juan de los Lagos'),
(74, 'San Juanito de Escobedo'),
(75, 'San Julián'),
(76, 'San Marcos'),
(77, 'San Martín de Bolaños'),
(78, 'San Martín Hidalgo'),
(79, 'San Miguel el Alto'),
(80, 'San Sebastián del Oeste'),
(81, 'Santa María de los Ángeles'),
(82, 'Santa María del Oro'),
(83, 'Sayula'),
(84, 'Tala'),
(85, 'Talpa de Allende'),
(86, 'Tamazula de Gordiano'),
(87, 'Tapalpa'),
(88, 'Tecalitlán'),
(89, 'Techaluta de Montenegro'),
(90, 'Tecolotlán'),
(91, 'Tenamaxtlán'),
(92, 'Teocaltiche'),
(93, 'Teocuitatlán de Corona'),
(94, 'Tepatitlán de Morelos'),
(95, 'Tequila'),
(96, 'Teuchitlán'),
(97, 'Tizapán el Alto'),
(98, 'Tlajomulco de Zúñiga'),
(99, 'Tlaquepaque'),
(100, 'Tolimán'),
(101, 'Tomatlán'),
(102, 'Tonala'),
(103, 'Tonaya'),
(104, 'Totatiche'),
(105, 'Tototlán'),
(106, 'Tuxcacuesco'),
(107, 'Tuxcueca'),
(108, 'Tuxpan'),
(109, 'Unión de San Antonio'),
(110, 'Unión de Tula'),
(111, 'Valle de Guadalupe'),
(112, 'Valle de Juárez'),
(113, 'Villa Corona'),
(114, 'Villa Guerrero'),
(115, 'Villa Hidalgo'),
(116, 'Villa Purificación'),
(117, 'Yahualica de González Gallo'),
(118, 'Zacoalco de Torres'),
(119, 'Zapopan'),
(120, 'Zapotiltic'),
(121, 'Zapotitlán de Vadillo'),
(122, 'Zapotlán del Rey'),
(123, 'Zapotlán el Grande'),
(124, 'Zapotlanejo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id` int(11) NOT NULL COMMENT 'Identificador de los permisos',
  `permiso` varchar(25) NOT NULL COMMENT 'Permiso que se le asignará a un rol',
  `descripcion` tinytext NOT NULL COMMENT 'Descripción del permiso'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `titulo` text NOT NULL,
  `descripcion` text NOT NULL,
  `existencia` int(11) NOT NULL,
  `estado` enum('activo','inactivo') NOT NULL DEFAULT 'activo',
  `precio` int(11) NOT NULL,
  `categoria` tinytext NOT NULL,
  `fecha` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de publicación del producto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rel_car_prod`
--

CREATE TABLE `rel_car_prod` (
  `id_prod` int(11) NOT NULL,
  `id_car` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rel_rol_permiso`
--

CREATE TABLE `rel_rol_permiso` (
  `id_permiso` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rel_user_car`
--

CREATE TABLE `rel_user_car` (
  `id_user` int(11) NOT NULL,
  `id_car` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL COMMENT 'Identificador de la tabla roles',
  `rol` varchar(25) NOT NULL COMMENT 'Rol que se le asignará a un usuario',
  `descripcion` tinytext NOT NULL COMMENT 'Descripción del rol'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` text NOT NULL,
  `correo` text NOT NULL,
  `nombre_usuario` text NOT NULL,
  `f_nacimiento` date NOT NULL,
  `numero_tel` text NOT NULL,
  `acerca_mi` text,
  `activo_desde` datetime DEFAULT CURRENT_TIMESTAMP,
  `id_rol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `aviso`
--
ALTER TABLE `aviso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_avi_us` (`id_user`),
  ADD KEY `fk_avi_pro` (`id_prod`);

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_com_us` (`id_user`),
  ADD KEY `fk_com_pro` (`id_prod`);

--
-- Indices de la tabla `contrasenas`
--
ALTER TABLE `contrasenas`
  ADD UNIQUE KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `direccion`
--
ALTER TABLE `direccion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_dic_us` (`id_user`);

--
-- Indices de la tabla `fotos_perfil`
--
ALTER TABLE `fotos_perfil`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `fk_fp_us` (`id_user`) USING BTREE;

--
-- Indices de la tabla `imagenes`
--
ALTER TABLE `imagenes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_img_pro` (`id_prod`);

--
-- Indices de la tabla `met_pago`
--
ALTER TABLE `met_pago`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_met_us` (`id_user`);

--
-- Indices de la tabla `municipios_jalisco`
--
ALTER TABLE `municipios_jalisco`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pro_us` (`id_user`);

--
-- Indices de la tabla `rel_car_prod`
--
ALTER TABLE `rel_car_prod`
  ADD KEY `fk_rel_car` (`id_car`),
  ADD KEY `fk_rel_pro` (`id_prod`);

--
-- Indices de la tabla `rel_rol_permiso`
--
ALTER TABLE `rel_rol_permiso`
  ADD KEY `fk_permiso` (`id_permiso`),
  ADD KEY `fk_rol` (`id_rol`);

--
-- Indices de la tabla `rel_user_car`
--
ALTER TABLE `rel_user_car`
  ADD KEY `fk_car_us` (`id_car`),
  ADD KEY `fk_us_car` (`id_user`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_us_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `aviso`
--
ALTER TABLE `aviso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `direccion`
--
ALTER TABLE `direccion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fotos_perfil`
--
ALTER TABLE `fotos_perfil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `imagenes`
--
ALTER TABLE `imagenes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `met_pago`
--
ALTER TABLE `met_pago`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `municipios_jalisco`
--
ALTER TABLE `municipios_jalisco`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=125;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Identificador de los permisos';

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Identificador de la tabla roles';

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `aviso`
--
ALTER TABLE `aviso`
  ADD CONSTRAINT `fk_avi_pro` FOREIGN KEY (`id_prod`) REFERENCES `productos` (`id`),
  ADD CONSTRAINT `fk_avi_us` FOREIGN KEY (`id_user`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD CONSTRAINT `fk_com_pro` FOREIGN KEY (`id_prod`) REFERENCES `productos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_com_us` FOREIGN KEY (`id_user`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `contrasenas`
--
ALTER TABLE `contrasenas`
  ADD CONSTRAINT `fk_cont_usu` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `direccion`
--
ALTER TABLE `direccion`
  ADD CONSTRAINT `fk_dic_us` FOREIGN KEY (`id_user`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `fotos_perfil`
--
ALTER TABLE `fotos_perfil`
  ADD CONSTRAINT `fk_fp_us` FOREIGN KEY (`id_user`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `imagenes`
--
ALTER TABLE `imagenes`
  ADD CONSTRAINT `fk_img_pro` FOREIGN KEY (`id_prod`) REFERENCES `productos` (`id`);

--
-- Filtros para la tabla `met_pago`
--
ALTER TABLE `met_pago`
  ADD CONSTRAINT `fk_met_us` FOREIGN KEY (`id_user`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk_pro_us` FOREIGN KEY (`id_user`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `rel_car_prod`
--
ALTER TABLE `rel_car_prod`
  ADD CONSTRAINT `fk_rel_car` FOREIGN KEY (`id_car`) REFERENCES `carrito` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_rel_pro` FOREIGN KEY (`id_prod`) REFERENCES `productos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `rel_rol_permiso`
--
ALTER TABLE `rel_rol_permiso`
  ADD CONSTRAINT `fk_permiso` FOREIGN KEY (`id_permiso`) REFERENCES `permisos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_rol` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `rel_user_car`
--
ALTER TABLE `rel_user_car`
  ADD CONSTRAINT `fk_car_us` FOREIGN KEY (`id_car`) REFERENCES `carrito` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_us_car` FOREIGN KEY (`id_user`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_us_rol` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

