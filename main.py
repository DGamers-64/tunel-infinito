import Jugador, Tunel, Consola

def main():
    repetir = True
    while repetir == True:
        jugador = Jugador.Jugador()
        consola = Consola.Consola()
        tunel = Tunel.Tunel()

        consola.limpiar()
        consola.inicio(jugador)
        consola.limpiar()
        
        while jugador.eventosToGo > 0:
            jugador.calcularMetros()
            jugador.subEventosToGo()
            tunel.generarEvento()
            consola.cabecera(jugador)
            respuesta = consola.evento(tunel)
            consola.limpiar()
            jugador.recompensas(tunel, respuesta)

        jugador.actualizarRecord()

        repetir = consola.enhorabuena(jugador)

if __name__ == "__main__":
    main()