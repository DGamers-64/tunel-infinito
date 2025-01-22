import Jugador as Jugador
import Tunel as Tunel
import Consola

def main():
    repetir = True
    while repetir == True:
        jugador = Jugador.Jugador()
        tunel = Tunel.Tunel()
        consola = Consola.Consola()

        consola.limpiar()
        consola.inicio(jugador)
        consola.limpiar()
        
        salidaEmergencia = False
        while jugador.eventosToGo > 0:
            consola.transicion(jugador)
            jugador.calcularMetros()
            jugador.subEventosToGo()
            tunel.generarEvento()
            respuestaValida = False
            while respuestaValida == False:
                try:
                    consola.cabecera(jugador)
                    respuesta = consola.evento(tunel)
                    respuestaValida = True
                    if respuesta == 0:
                        salidaEmergencia = True
                        break
                except ValueError:
                    consola.error("valorIncorrecto")
                except IndexError:
                    consola.error("indexError")
                except:
                    consola.error("default")
            if salidaEmergencia:
                consola.limpiar()
                break
            jugador.recompensas(tunel, respuesta)
            consola.limpiar()

        jugador.actualizarRecord()
        repetir = consola.enhorabuena(jugador)

if __name__ == "__main__":
    main()