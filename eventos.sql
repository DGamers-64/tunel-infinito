DROP DATABASE IF EXISTS tunel_infinito;
CREATE DATABASE tunel_infinito;
USE tunel_infinito;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(10),
    puntuacion INT
);

CREATE TABLE evento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20),
    pregunta VARCHAR(40),
    rango_min INT,
    rango_max INT
);

CREATE TABLE opcion_evento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT,
    respuesta VARCHAR(40),
    FOREIGN KEY (id_evento) REFERENCES evento(id)
);

CREATE TABLE efecto_opcion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_opcion INT,
    orden INT,
    efecto VARCHAR(40),
    FOREIGN KEY (id_opcion) REFERENCES opcion_evento(id)
);

CREATE TABLE params_efecto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_efecto INT,
    orden INT,
    parametro VARCHAR(40),
    FOREIGN KEY (id_efecto) REFERENCES efecto_opcion(id)
)

INSERT INTO evento (nombre, pregunta, rango_min, rango_max) VALUES
    ("Niño", "¿Te has perdido? ¡Yo también!", 0, 99999),
    ("Abuela", "¿Cuánto es 2x4?", 1000, 99999);

INSERT INTO opcion_evento (id_evento, respuesta) VALUES
    (1, "Ehm si..."),
    (1, "¡Que va!"),
    (2, "¡8!"),
    (2, "¡5!");

INSERT INTO efecto_opcion (id_opcion, orden, efecto, param1, param2, param3) VALUES
    (1, 1, "alejar", "3", NULL, NULL),
    (2, 1, "acercar", "3", NULL, NULL),
    (2, 2, "dialogo", "¡ADIOS JIJIJIJA!", NULL, NULL),
    (3, 1, "alejar", "6", NULL, NULL),
    (4, 1, "acercar", "6", NULL, NULL);