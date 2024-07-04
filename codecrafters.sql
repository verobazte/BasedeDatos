-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-07-2024 a las 22:42:51
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `codecrafters`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `codigo` int(11) NOT NULL,
  `apeynom` varchar(255) NOT NULL,
  `domcalle` varchar(130) DEFAULT NULL,
  `domnro` int(10) NOT NULL,
  `domciudad` varchar(50) NOT NULL,
  `dompcia` varchar(50) NOT NULL,
  `email` varchar(40) NOT NULL,
  `tel` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`codigo`, `apeynom`, `domcalle`, `domnro`, `domciudad`, `dompcia`, `email`, `tel`) VALUES
(1, 'Ruiz Juan', 'Dorrego', 2434, 'Bahia Blanca', 'Buenos Aires', 'juanr@gmail.com', 22547779),
(2, 'Sica, Ana', 'Vieytes', 1234, 'Oran', 'Salta', 'anasica@gmail.com', 3333355),
(4, 'Lunati Julio', 'San Martín', 6656, 'Tandil', 'Buenos Aires', 'jl@gmail.com', 7777665),
(5, 'Lima Rocio', 'Libertad', 1343, 'La Falda', 'Cordoba', 'rolima@gmail.com', 7779978),
(6, 'Benitez Juan', 'Balcace', 1122, 'Viedma', 'Rio Negro', 'jbenitez@gmail.com', 88764099);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `codigo` int(11) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `imagen_url` varchar(255) DEFAULT NULL,
  `proveedor` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`codigo`, `descripcion`, `cantidad`, `precio`, `imagen_url`, `proveedor`) VALUES
(1, 'Parlante Portatil Go', 10, 24700.00, 'parlante.jpg', 101),
(2, 'Parlante Portatil Inhalambrico Go', 15, 25300.00, 'parlante.jpg', 110),
(3, 'Auricular Inhalambrico M10 Pro Superior', 8, 94500.00, 'auricular_in.jpg', 102),
(4, 'Auricular Bluetooth de diadema M8', 15, 44700.00, 'auricular_blu.jpg', 103),
(5, 'Teclado Gamer con retroiluminacion Led A24', 10, 67800.00, 'teclado.jpg', 104),
(6, 'Monitor Led 21,5 pulgadas marca H', 6, 97500.00, 'minitor.jpg', 105);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `codigo` int(11) NOT NULL,
  `cod_producto` int(20) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `razon_social` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`codigo`, `cod_producto`, `descripcion`, `razon_social`) VALUES
(1, 22, 'Auricular inhalambrico', 'TecnoS.A.'),
(2, 22, 'Parlante Portatil Inhalambrico Go', 'Atlia S.A'),
(3, 3, 'Parlante Portatil Go', 'Atlia S.A'),
(4, 2, 'Teclado Gamer con retroiluminacion Led A24', 'MtaR S.A.'),
(5, 1, 'Notebook A 16p Pro 8g ram', 'IDEAS S.A');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`codigo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
