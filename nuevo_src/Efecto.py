from Vista import Vista

class Efecto:
    def alejar(self, tunel, param1, param2, param3):
        tunel.eventos_restantes += int(param1)
        Vista.print_texto("> Sientes que te has \nalejado un poco")
    
    def acercar(self, tunel, param1, param2, param3):
        tunel.eventos_restantes -= int(param1)
        Vista.print_texto("> Sientes que te has \nacercado un poco")

    def dialogo(self, tunel, param1, param2, param3):
        if param2 is not None and param3 is not None:
            Vista.print_dialogo([param1, param2, param3])
        elif param2 is not None and param3 is None:
            Vista.print_dialogo([param1, param2])
        elif param2 is None:
            Vista.print_dialogo([param1])