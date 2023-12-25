from pyrogram import Client, filters
from pyrocon import patch
from models.User import User
from plugins.buttons import keyboard_buttons_text
from plugins.buttons import keyboard_buttons_text
from extra_functionality.extra_funcionality import get_game_and_respond
from content.texts import error_text_no_comand
from state.state import get_state, set_state
@Client.on_message(filters.text & filters.private)
async def get_text(client, message):
    user = User(message.from_user)
    text = message.text
    state = get_state(user.id)
    if text == keyboard_buttons_text['sarch_game']:
        set_state(user.id, buscando=True)
        quiz = patch(client)
        answer = await quiz.ask(message,'Escriba el nombre del juego a buscar',filter=filters.text)
        if answer.text:
            await get_game_and_respond(answer)
            

    elif text == keyboard_buttons_text['help']:
        await message.reply('Este es el mensaje de ayuda')
    elif state['buscando'] == False:
        await message.reply(error_text_no_comand.format(keyboard_buttons_text['sarch_game']))