import random
import Juegos.TresEnRaya
from Vista import Vista
import Juegos

class Efecto:
    def alejar(self, tunel, usuario, param1, param2, param3):
        tunel.add_eventos_restantes(int(param1))
        Vista.print_texto(" > Sientes que te has \n alejado un poco")
    
    def acercar(self, tunel, usuario, param1, param2, param3):
        tunel.sub_eventos_restantes(int(param1))
        Vista.print_texto(" > Sientes que te has \n acercado un poco")

    def dialogo(self, tunel, usuario, param1, param2, param3):
        if param2 is not None and param3 is not None:
            Vista.print_dialogo([param1, param2, param3])
        elif param2 is not None and param3 is None:
            Vista.print_dialogo([param1, param2])
        elif param2 is None:
            Vista.print_dialogo([param1])

    def terminar(self, tunel, usuario, param1, param2, param3):
        tunel.eventos_restantes = 0
        Vista.print_texto(" > Sientes que todo ha\n terminado")

    def tren(self, tunel, usuario, param1, param2, param3):
        rangos_metros = [[400, 600], [400, 600], [400, 600], [900, 1100], [900, 1100], [1900, 2100]]
        direccion = random.randint(0,1)
        magnitud = random.randint(0,len(rangos_metros)-1)
        if direccion == 0:
            tunel.sub_metros(random.randint(rangos_metros[magnitud][0], rangos_metros[magnitud][1]))
        else:
            tunel.add_metros(random.randint(rangos_metros[magnitud][0], rangos_metros[magnitud][1]))
        Vista.print_texto(" > Has sido llevado en el tren")
    
    def tres_en_raya(self, tunel, usuario, param1, param2, param3):
        juego = Juegos.TresEnRaya.TresEnRaya()
        resultado = juego.juego(tunel, usuario)
        match resultado:
            case 0:
                Vista.print_texto(f" {param1}")
            case 1:
                Vista.print_texto(f" {param2}")
            case 2:
                Vista.print_texto(f" {param3}")