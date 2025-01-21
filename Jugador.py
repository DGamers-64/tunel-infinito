import random

class Jugador:
    nombre: str
    metros: int
    vida: int
    fuerza: int
    defensa: int
    mejorPuntuacion: int
    eventosToGo: int

    def __init__(self, mejorPuntuacion=10000):
        recordFile = open("record.txt", "r")
        self.nombre = "Nombre"
        self.mejorPuntuacion = int(recordFile.read())
        self.metros = 0
        self.eventosToGo = random.randint(5,20)
        recordFile.close()
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def subEventosToGo(self,num=1):
        self.eventosToGo -= num

    def calcularMetros(self):
        self.metros += random.randint(15,70)

    # RECOMPENSAS
    # alejarPequeño: Aleja 3 eventos el final
    # acercarPequeño: Acerca 3 eventos el final
    # alejarGrande: Aleja 6 eventos el final
    # acercarGrande: Acerca 6 eventos el final
    # terminar: Termina la run
    # nada: No ocurre nada

    def recompensas(self, tunel, consola, respuesta):
        for i in tunel.eventoActual["opciones"][respuesta-1]["efecto"]:
            match i:
                case "alejarPequeño":
                    self.eventosToGo += 3
                case "acercarPequeño":
                    self.eventosToGo -= 3
                case "alejarGrande":
                    self.eventosToGo += 6
                case "acercarGrande":
                    self.eventosToGo -= 6
                case "terminar":
                    self.eventosToGo = 0
                case "nada":
                    pass
            consola.recompensa(i)
        
    def actualizarRecord(self):
        if self.metros > self.mejorPuntuacion:
            recordFile = open("record.txt", "w")
            recordFile.write(str(self.metros))
            recordFile.close()
            self.mejorPuntuacion = self.metros