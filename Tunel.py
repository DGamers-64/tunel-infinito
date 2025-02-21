import random

class Tunel:
    metros: int
    eventos_restantes: int

    def __init__(self):
        self.metros = 0
        self.eventos_restantes = 6

    def salida(self) -> bool:
        if self.eventos_restantes <= 0:
            return False
        return True
    
    def avanzar_tunel(self) -> None:
        self.metros += random.randint(15,30)
        self.eventos_restantes -= 1

    def add_eventos_restantes(self, num: int) -> None:
        self.eventos_restantes += num

    def sub_eventos_restantes(self, num: int) -> None:
        self.eventos_restantes -= num
    
    def add_metros(self, num: int) -> None:
        self.metros += num

    def sub_metros(self, num: int) -> None:
        self.metros -= num
        if self.metros < 0:
            self.metros = 0