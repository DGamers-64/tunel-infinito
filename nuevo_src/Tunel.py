class Tunel:
    __metros: int
    eventos_restantes: int

    def __init__(self):
        self.__metros = 0
        self.eventos_restantes = 6

    @property
    def metros(self):
        return self.__metros
    
    def salida(self):
        if self.eventos_restantes == 0:
            return False
        return True
    