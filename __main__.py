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
            respuestaValida = False
            while respuestaValida == False:
                try:
                    consola.cabecera(jugador)
                    respuesta = consola.evento(tunel)
                    respuestaValida = True
                except ValueError:
                    consola.error("valorIncorrecto")
                except IndexError:
                    consola.error("indexError")
                except:
                    consola.error("default")
            jugador.recompensas(tunel, consola, respuesta)
            consola.limpiar()

        jugador.actualizarRecord()

        repetir = consola.enhorabuena(jugador)

if __name__ == "__main__":
    main()