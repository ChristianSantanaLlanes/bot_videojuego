from pyrogram import Client, filters
from pyrocon import patch
from helpers.service import get_game_by_id
from models.User import User
from plugins.buttons import keyboard_buttons_text
from extra_functionality.extra_funcionality import (
    create_first_state,
    get_game_and_respond, 
    get_games_list_and_respond)
from content.texts import (error_text_no_comand, 
                           text_with_cancel, 
                           search_text,
                           help_text,
                           info_text)
from state.state import set_state
@Client.on_message(filters.text & filters.private)
async def get_text(client, message):
    user = User(message.from_user)
    text = message.text
    state = await create_first_state(user.id)
    if text == keyboard_buttons_text['sarch_game']:
        set_state(user.id, buscando=True)
        quiz = patch(client)
        answer = await quiz.ask(message,search_text,filter=filters.text)
        if answer.text:
            await get_games_list_and_respond(client, answer)
        if answer.cancel:
            set_state(user.id, buscando=False)
            await client.send_message(user.id, text_with_cancel)
            

    elif text == keyboard_buttons_text['help']:
        await message.reply(help_text)
    elif text == keyboard_buttons_text['info']:
        await message.reply(info_text)
    elif text.startswith('game'):
        id = text.split('~')[1]
        game = get_game_by_id(id)
        if game:
            await get_game_and_respond(client, user, game)
        else:
            message.reply('Algo fallo')
    elif state:
        if state['buscando'] == False:
            await message.reply(error_text_no_comand.format(keyboard_buttons_text['sarch_game']))