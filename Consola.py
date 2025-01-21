import os, time

class Consola:
    def limpiar(self):
        os.system("cls")

    def linea(self):
        print("-----------------------------------------")

    def inicio(self, jugador):
        self.linea()
        time.sleep(0.05)
        print(f" TÚNEL INFINITO: Record: {jugador.mejorPuntuacion}")
        time.sleep(0.05)
        self.linea()
        time.sleep(0.05)
        print(f" Elige un nombre: ", end="")
        nombre = input()
        jugador.setNombre(nombre)

    def cabecera(self, jugador):
        self.linea()
        time.sleep(0.05)
        print(f" {jugador.metros}m	| Record: {jugador.mejorPuntuacion}m | {jugador.nombre}")
        time.sleep(0.05)
        self.linea()

    def evento(self, tunel):
        time.sleep(0.05)
        print(f" {tunel.eventoActual["nombre"]}")
        time.sleep(0.05)
        print(f" {tunel.eventoActual["pregunta"]}")
        time.sleep(0.05)
        self.linea()
        time.sleep(0.05)
        for i in range(tunel.getLenOpciones()):
            print(f" {i+1}. {tunel.eventoActual["opciones"][i]["respuesta"]}")
            time.sleep(0.05)
        self.linea()
        time.sleep(0.05)
        print(" > ", end="")
        respuesta = int(input())
        self.linea()
        time.sleep(0.05)
        print(f" {tunel.eventoActual["opciones"][respuesta-1]["dialogoFinal"]}")
        time.sleep(0.05)
        self.linea()
        input()
        return respuesta
    
    def hasMuerto(self, jugador):
        self.linea()
        print(f" {jugador.nombre} HAS MUERTO")
        self.linea()
        input()

    def enhorabuena(self, jugador):
        self.linea()
        print(f" HAS SALIDO DEL TÚNEL")
        print(f" {jugador.nombre} has conseguido {jugador.metros}m")
        print(f" Tu récord actual es de {jugador.mejorPuntuacion}m")
        self.linea()
        print(" ¿Quieres volver a jugar? (s/n)")
        self.linea()
        print(" > ", end="")
        respuesta = input()
        if respuesta == "s":
            return True
        return False