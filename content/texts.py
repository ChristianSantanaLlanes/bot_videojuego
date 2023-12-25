start_text = '''
¡Hola {}! Bienvenido  al bot de videojuegos. Aquí podrás encontrar información sobre tus juegos favoritos, como la foto, el nombre, la descripción y mucho más.

Para empezar, usa la opción "Buscar Videojuego" y envíame el nombre del juego que quieres buscar. Por ejemplo, si quieres buscar información sobre "Elden Ring", envíame "Elden Ring".

También puedes utilizar los siguientes comandos:

/help: Para obtener ayuda sobre el bot.
/info: Para obtener tu informacion
'''

info_text = '''
Nombre: {first_name} {last_name}
Username: {username}
Id: {id}

Version del Bot: 0.1.0 beta
'''

error_text_game_not_found = '''
❌ El bot ha rechazado su solicitud:

▫ Asegúrese de cumplir los siguientes requisitos:

1. El nombre del videojuego está escrito correctamente.
2. ⁠El juego existe actualmente.
'''

error_text_no_comand = '''
❌ El bot ha rechazado su solicitud:

▫ Asegúrese de cumplir los siguientes requisitos:

1. Estas buscando en el boton {}
2. Estas usando algun comando existente
'''

game_text = '''
**Nombre**:👉👉 {name}
**Descripcion**:👉 {description}
    '''