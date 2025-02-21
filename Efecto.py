import random
import Juegos.TresEnRaya
from Vista import Vista
import Juegos

class Efecto:
    def alejar(self, tunel, usuario, params):
        tunel.add_eventos_restantes(int(params[0]["parametro"]))
        Vista.print_texto(" > Sientes que te has \n alejado un poco")
    
    def acercar(self, tunel, usuario, params):
        tunel.sub_eventos_restantes(int(params[0]["parametro"]))
        Vista.print_texto(" > Sientes que te has \n acercado un poco")

    def dialogo(self, tunel, usuario, params):
        for i in params:
            Vista.print_texto(i["parametro"])

    def terminar(self, tunel, usuario, params):
        tunel.eventos_restantes = 0
        Vista.print_texto(" > Sientes que todo ha\n terminado")

    def tren(self, tunel, usuario, params):
        rangos_metros = [[400, 600], [400, 600], [400, 600], [900, 1100], [900, 1100], [1900, 2100]]
        direccion = random.randint(0,1)
        magnitud = random.randint(0,len(rangos_metros)-1)
        if direccion == 0:
            tunel.sub_metros(random.randint(rangos_metros[magnitud][0], rangos_metros[magnitud][1]))
        else:
            tunel.add_metros(random.randint(rangos_metros[magnitud][0], rangos_metros[magnitud][1]))
        Vista.print_texto(" > Has sido llevado en el tren")
    
    # Tres en raya, necesita rehacerse entero todo
    def tres_en_raya(self, tunel, usuario, params):
        juego = Juegos.TresEnRaya.TresEnRaya()
        resultado = juego.juego(tunel, usuario)
        match resultado:
            case 0:
                Vista.print_texto(f" {params[0]["parametro"]}")
            case 1:
                Vista.print_texto(f" {params[1]["parametro"]}")
            case 2:
                Vista.print_texto(f" {params[2]["parametro"]}")