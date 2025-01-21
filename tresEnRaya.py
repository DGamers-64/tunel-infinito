import Consola as consola
import random
consola = consola.Consola()

class Tablero:
    tablero: list

    def __init__(self):
        self.tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        
    def vaciarTablero(self):
        self.tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

    def comprobarTablero(self):
        for i in range(0,2):
            if self.tablero[i][0] == "X" and self.tablero[i][1] == "X" and self.tablero[i][2] == "X":
                return 0
            if self.tablero[0][i] == "X" and self.tablero[1][i] == "X" and self.tablero[2][i] == "X":
                return 0
            if self.tablero[0][0] == "X" and self.tablero[1][1] == "X" and self.tablero[2][2] == "X":
                return 0
            if self.tablero[0][2] == "X" and self.tablero[1][1] == "X" and self.tablero[2][0] == "X":
                return 0
        for i in range(0,2):
            if self.tablero[i][0] == "O" and self.tablero[i][1] == "O" and self.tablero[i][2] == "O":
                return 2
            if self.tablero[0][i] == "O" and self.tablero[1][i] == "O" and self.tablero[2][i] == "O":
                return 2
            if self.tablero[0][0] == "O" and self.tablero[1][1] == "O" and self.tablero[2][2] == "O":
                return 2
            if self.tablero[0][2] == "O" and self.tablero[1][1] == "O" and self.tablero[2][0] == "O":
                return 2
        empate = True
        for i in range(0,2):
            if " " in self.tablero[i]:
                empate = False
        if empate:
            return 1
        else:
            return 3
        
    def dibujarTablero(self, jugadorTunel):
        consola.limpiar()
        consola.cabecera(jugadorTunel)
        print(" \\ | 1 | 2 | 3")
        print(f" 1 | {self.tablero[0][0]} | {self.tablero[0][1]} | {self.tablero[0][2]}")
        print(f" 2 | {self.tablero[1][0]} | {self.tablero[1][1]} | {self.tablero[1][2]}")
        print(f" 3 | {self.tablero[2][0]} | {self.tablero[2][1]} | {self.tablero[2][2]}")
        consola.linea()

class Jugador:
    def preguntarCoord(self, tablero):
        print(" Fila > ", end="")
        fila = int(input())-1
        print(" Columna > ", end="")
        columna = int(input())-1
        if tablero.tablero[fila][columna] == " ":
            tablero.tablero[fila][columna] = "X"
        else:
            raise IndexError()

    def generarCoord(self, tablero):
        correcto = False
        while correcto == False:
            fila = random.randint(0,2)
            columna = random.randint(0,2)
            if tablero.tablero[fila][columna] == " ":
                tablero.tablero[fila][columna] = "O"
                correcto = True
                break

class TresEnRaya:
    def juego(self, jugadorTunel):
        ganador = 3
        tablero = Tablero()
        jugador = Jugador()
        bot = Jugador()
        while ganador == 3:
            coordCorrecta = False
            while coordCorrecta == False:
                tablero.dibujarTablero(jugadorTunel)
                try:
                    jugador.preguntarCoord(tablero)
                    coordCorrecta = True
                except ValueError:
                    consola.error("tresEnRayaFaltaCoord")
                except IndexError:            
                    consola.error("tresEnRayaCoordIncorrecta")
            ganador = tablero.comprobarTablero()
            if ganador != 3:
                break
            bot.generarCoord(tablero)
            ganador = tablero.comprobarTablero()
        tablero.dibujarTablero(jugadorTunel)
        match ganador:
            case 0:
                print(" ¡Oh, me has ganado!")
            case 1:
                print(" Empatamos jaja")
            case 2:
                print(" ¡Te he ganado! ¡Yupii!")
        return ganador