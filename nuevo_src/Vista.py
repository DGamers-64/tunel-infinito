import time, os

class Vista:
    def input_max_numero(max_opciones, texto=" > "):
        correcto = False
        while not correcto:
            try:
                Vista.print_linea()
                time.sleep(0.05)
                respuesta = int(input(texto))
                time.sleep(0.05)
                if respuesta < 1 or respuesta > max_opciones:
                    Vista.print_linea()
                    time.sleep(0.05)
                    print(" Opción inválida")
                    time.sleep(0.05)
                    continue
                correcto = True
            except ValueError:
                Vista.print_linea()
                time.sleep(0.05)
                print(" Valor incorrecto")
        return respuesta

    def input_nombre():
        correcto = False
        while not correcto:
            Vista.print_linea()
            time.sleep(0.05)
            nombre = input(" Escribe tu nombre > ")
            time.sleep(0.05)
            if len(nombre) > 20:
                Vista.print_linea()
                time.sleep(0.05)
                print(" Nombre demasiado largo")
                time.sleep(0.05)
                continue
            correcto = True
        return nombre

    def limpiar_consola():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
    
    def print_linea():
        print("-----------------------------------------")

    def print_menu_bienvenida():
        Vista.limpiar_consola()
        Vista.print_linea()
        time.sleep(0.05)
        print(" TUNEL INFINITO... ¿Saldrás algún día?")
        time.sleep(0.05)
        Vista.print_linea()
        time.sleep(0.05)
        print(" 1. Jugar")
        time.sleep(0.05)
        print(" 2. Ranking")
        time.sleep(0.05)
        respuesta = Vista.input_max_numero(2)
        return respuesta

    def print_ranking(usuarios):
        Vista.print_cabecera("xxxxx", 0, 0)
        time.sleep(0.05)
        if len(usuarios) > 10:
            longitud = 10
        else:
            longitud = len(usuarios)   
        for i in range(longitud):
            print(f" {i+1}. {usuarios[i]["nombre"]}: {usuarios[i]["puntuacion"]}")
            time.sleep(0.05)
        input()

    def print_cabecera(nombre, puntuacion, mejor_puntuacion):
        Vista.limpiar_consola()
        Vista.print_linea()
        time.sleep(0.05)
        print(f" {puntuacion}m | Record: {mejor_puntuacion}m | {nombre}")
        time.sleep(0.05)
        Vista.print_linea()
        time.sleep(0.05)

    def print_animacion():
        pass

    def print_evento(evento: dict) -> None:
        print(f" {evento["nombre"]}")
        time.sleep(0.05)
        print(f"  {evento["pregunta"]}")
        time.sleep(0.05)
        Vista.print_linea()
        time.sleep(0.05)
        for i in range(len(evento["opciones"])):
            print(f" {i+1}. {evento["opciones"][i]["respuesta"]}")
            time.sleep(0.05)
        respuesta = Vista.input_max_numero(len(evento["opciones"]))
        time.sleep(0.05)
        return respuesta
    
    def print_dialogo(dialogo):
        Vista.print_linea()
        time.sleep(0.05)
        print(f" {dialogo[0]}")
        time.sleep(0.05)
        if len(dialogo) > 1:
            print(f" {dialogo[1]}")
            time.sleep(0.05)
        if len(dialogo) > 2:
            print(f" {dialogo[2]}")
            time.sleep(0.05)
        Vista.print_linea()

    def print_texto(texto):
        print(f" {texto}")
        time.sleep(0.05)
        Vista.print_linea()

    def print_efecto():
        pass

    def print_pantalla_fin():
        pass
