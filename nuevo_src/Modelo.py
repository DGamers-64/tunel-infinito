import mysql.connector

class Modelo:
    def abrir_conexion():
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
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
        pass

    # Obtener diccionario con TODA la información de un evento aleatorio.
    def get_random_evento(metros: int) -> dict:
        cursor, conexion = Modelo.abrir_conexion()
        cursor.execute("SELECT * FROM evento")

        resultados = cursor.fetchall()

        for fila in resultados:
            print(fila)

        Modelo.cerrar_conexion(cursor, conexion)
