from Modelo import Modelo
from Vista import Vista
from Tunel import Tunel
from Efecto import Efecto

respuesta = 0
while respuesta != 1:
    respuesta = Vista.print_menu_bienvenida()
    if respuesta == 2:
        usuarios = Modelo.get_all_usuarios()
        Vista.print_ranking(usuarios)

nombre = Vista.input_nombre()
usuario = Modelo.get_usuario(nombre)
if usuario is None:
    Modelo.set_usuario_nuevo(nombre)
    usuario = Modelo.get_usuario(nombre)

tunel = Tunel()
efecto = Efecto()

while tunel.salida():
    evento = Modelo.get_random_evento(tunel.metros)
    Vista.print_cabecera(usuario["nombre"], tunel.metros, usuario["puntuacion"])
    opcion_escogida = Vista.print_evento(evento)
    for i in evento["opciones"][opcion_escogida-1]["efectos"]:
        getattr(efecto, i["efecto"])(tunel, i["param1"], i["param2"], i["param3"])
    input()