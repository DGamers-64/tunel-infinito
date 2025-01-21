import os, time

class Consola:
    def limpiar(self):
        os.system("cls")

    def linea(self):
        print("-----------------------------------------")

    def inicio(self, jugador):
        self.linea()
        time.sleep(0.05)
        print(f" TÚNEL INFINITO > Record: {jugador.mejorPuntuacion}")
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
        if respuesta <= 0 or respuesta > len(tunel.eventoActual["opciones"]):
            raise IndexError("La respuesta debe de estar listada")
        self.linea()
        time.sleep(0.05)
        print(f" {tunel.eventoActual["opciones"][respuesta-1]["dialogoFinal"]}\n")
        time.sleep(0.05)
        return respuesta
    
    # FUNCION SIN USAR

    def hasMuerto(self, jugador):
        self.linea()
        print(f" {jugador.nombre} HAS MUERTO")
        self.linea()
        input()

    ##################

    def enhorabuena(self, jugador):
        self.linea()
        time.sleep(0.05)
        print(f" HAS SALIDO DEL TÚNEL")
        time.sleep(0.05)
        print(f" {jugador.nombre} has conseguido {jugador.metros}m")
        time.sleep(0.05)
        print(f" Tu récord actual es de {jugador.mejorPuntuacion}m")
        time.sleep(0.05)
        self.linea()
        time.sleep(0.05)
        print(" ¿Quieres volver a jugar? (s/n)")
        time.sleep(0.05)
        self.linea()
        time.sleep(0.05)
        print(" > ", end="")
        respuesta = input()
        if respuesta == "s":
            return True
        return False
    
    def recompensa(self, recompensa):
        match recompensa:
            case "alejarPequeño":
                print(" > Tienes la sensación de haberte\n alejado del final <")
            case "acercarPequeño":
                print(" > Tienes la sensación de haberte\n acercado al final <")
            case "alejarGrande":
                print(" > Tienes la sensación de haberte\n alejado mucho del final <")
            case "acercarGrande":
                print(" > Tienes la sensación de haberte\n acercado mucho al final <")
            case "terminar":
                print(" > Crees que se ha terminado todo <")
            case "nada":
                print(" > No ocurre nada <")
        time.sleep(0.05)
        self.linea()
        input()

    def error(self, error):
        self.linea()
        time.sleep(0.05)
        match error:
            case "default":
                print(" Err: Error por defecto")
            case "valorIncorrecto":
                print(" Err: Valor incorrecto")
            case "indexError":
                print(" Err: La respuesta debe de estar listada")
        time.sleep(0.05)
        self.linea()
        input()
        self.limpiar()