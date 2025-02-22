import mysql.connector, random, os
from dotenv import load_dotenv

load_dotenv()

class Modelo:
    def abrir_conexion():
        conexion = mysql.connector.connect(
            host=os.getenv("mysql-host"),
            user=os.getenv("mysql-user"),
            password=os.getenv("mysql-password"),
            database="tunel_infinito"
        )

        return conexion.cursor(dictionary=True), conexion
    
    def cerrar_conexion(cursor, conexion) -> None:
        cursor.close()
        conexion.close()

    # Métodos usuarios
    def get_usuario(nombre: str) -> dict:
        cursor, conexion = Modelo.abrir_conexion()
        cursor.execute("SELECT nombre, puntuacion FROM usuario WHERE nombre LIKE %s", (nombre,))
        usuario = cursor.fetchone()
        Modelo.cerrar_conexion(cursor, conexion)
        return usuario
    
    def get_all_usuarios() -> list[dict]:
        cursor, conexion = Modelo.abrir_conexion()
        cursor.execute("SELECT nombre, puntuacion FROM usuario")
        usuarios = cursor.fetchall()
        Modelo.cerrar_conexion(cursor, conexion)
        return usuarios

    def set_usuario_nuevo(nombre: str) -> None:
        cursor, conexion = Modelo.abrir_conexion()
        cursor.execute("INSERT INTO usuario (nombre, puntuacion) VALUES (%s, 0)", (nombre, ))
        conexion.commit()
        Modelo.cerrar_conexion(cursor, conexion)

    def update_usuario(nombre: str, puntuacion: int) -> None:
        cursor, conexion = Modelo.abrir_conexion()
        cursor.execute("UPDATE usuario SET puntuacion = %s WHERE nombre = %s", (puntuacion, nombre, ))
        conexion.commit()
        Modelo.cerrar_conexion(cursor, conexion)

    # Obtener diccionario con TODA la información de un evento aleatorio.
    def get_random_evento(metros: int) -> dict:
        cursor, conexion = Modelo.abrir_conexion()
        cursor.execute("SELECT id, nombre, pregunta, rango_min, rango_max FROM evento WHERE %s BETWEEN rango_min AND rango_max", (metros, ))

        eventos = cursor.fetchall()
        evento = eventos[random.randint(0,len(eventos)-1)]

        cursor.execute("SELECT id, respuesta FROM opcion_evento WHERE id_evento = %s", (evento["id"], ))
        opciones = cursor.fetchall()

        for i in opciones:
            cursor.execute("SELECT id, efecto FROM efecto_opcion WHERE id_opcion = %s ORDER BY orden ASC", (i["id"], ))
            efectos = cursor.fetchall()
            i["efectos"] = efectos
            for j in efectos:
                cursor.execute("SELECT parametro FROM params_efecto WHERE id_efecto = %s", (j["id"], ))
                params = cursor.fetchall()
                j["params"] = params

        evento["opciones"] = opciones

        Modelo.cerrar_conexion(cursor, conexion)
        return evento
