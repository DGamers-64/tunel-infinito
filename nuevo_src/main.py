from Modelo import Modelo
from Vista import Vista

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
evento = Modelo.get_random_evento(1500)
print(evento)