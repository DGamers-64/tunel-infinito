import json, random

class Tunel:

    eventoActual: dict

    def generarEvento(self):
        eventosFile = open('./eventos.json', 'r', encoding='utf-8')
        eventos = json.loads(eventosFile.read())
        eventoId = random.randint(0,len(eventos)-1)
        self.eventoActual = eventos[eventoId]
    
    def getLenOpciones(self):
        return len(self.eventoActual["opciones"])