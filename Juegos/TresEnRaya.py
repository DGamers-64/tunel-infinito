from Vista import Vista
import random, time

class Tablero:
    tablero: list

    def __init__(self):
        self.tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        
    def vaciar_tablero(self):
        self.tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

    def comprobar_tablero(self):
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
        
    def dibujar_tablero(self, tunel, jugador_tunel):
        Vista.limpiar_consola()
        Vista.print_cabecera(jugador_tunel["nombre"], tunel.metros, jugador_tunel["puntuacion"])
        time.sleep(0.05)
        print(" \\ | 1 | 2 | 3")
        time.sleep(0.05)
        print(f" 1 | {self.tablero[0][0]} | {self.tablero[0][1]} | {self.tablero[0][2]}")
        time.sleep(0.05)
        print(f" 2 | {self.tablero[1][0]} | {self.tablero[1][1]} | {self.tablero[1][2]}")
        time.sleep(0.05)
        print(f" 3 | {self.tablero[2][0]} | {self.tablero[2][1]} | {self.tablero[2][2]}")
        time.sleep(0.05)
        Vista.print_linea()

class Jugador:
    def preguntar_coord(self, tablero):
        print(" Fila > ", end="")
        fila = int(input())-1
        print(" Columna > ", end="")
        columna = int(input())-1
        if tablero.tablero[fila][columna] == " ":
            tablero.tablero[fila][columna] = "X"
        else:
            raise IndexError()

    def generar_coord(self, tablero):
        correcto = False
        while correcto == False:
            fila = random.randint(0,2)
            columna = random.randint(0,2)
            if tablero.tablero[fila][columna] == " ":
                tablero.tablero[fila][columna] = "O"
                correcto = True
                break

class TresEnRaya:
    def juego(self, tunel, jugadorTunel):
        ganador = 3
        tablero = Tablero()
        jugador = Jugador()
        bot = Jugador()
        while ganador == 3:
            coordCorrecta = False
            while coordCorrecta == False:
                tablero.dibujar_tablero(tunel, jugadorTunel)
                try:
                    jugador.preguntar_coord(tablero)
                    coordCorrecta = True
                except ValueError:
                    Vista.print_linea()
                    Vista.print_texto(" Valor incorrecto")
                    Vista.print_linea()
                    input()
                    time.sleep(0.05)
                except IndexError: 
                    Vista.print_linea()           
                    Vista.print_texto(" Coordenada ocupada")
                    Vista.print_linea()
                    input()
                    time.sleep(0.05)
            ganador = tablero.comprobar_tablero()
            if ganador != 3:
                break
            bot.generar_coord(tablero)
            ganador = tablero.comprobar_tablero()
        tablero.dibujar_tablero(tunel, jugadorTunel)
        return ganador