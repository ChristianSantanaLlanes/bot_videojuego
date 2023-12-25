from pyrogram import Client
from extra_functionality.extra_funcionality import get_game_and_respond
from helpers.service import get_game_by_id
from state.state import get_state

from models.User import User
from plugins.buttons import get_back_button, get_game_buttons

@Client.on_callback_query()
async def next_back_page(client, callback_query):
    user = User(callback_query.from_user)
    query = callback_query.data
    state = get_state(user.id)
    if query == 'next_page':
        print('Next Page')
    elif query == 'back_page':
        print('Back Page')
    elif query == 'rec_min':
        await callback_query.edit_message_caption(state.get('rec_min'),reply_markup=get_back_button())
    elif query == 'rec_rec':
        await callback_query.edit_message_caption(state.get('rec_rec'),reply_markup=get_back_button())
    elif query == 'back':
        await callback_query.edit_message_caption(state.get('result'),reply_markup=get_game_buttons(state['trailer_url']))
    elif query.startswith('game'):
        id = query.split('-')[1]
        game = get_game_by_id(id)
        if game:
            await get_game_and_respond(client, user, game)
        else:
            callback_query.reply('Algo fallo')