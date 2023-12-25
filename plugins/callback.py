from pyrogram import Client
from state.state import get_state

from models.User import User
from plugins.buttons import get_back_button, get_game_buttons

@Client.on_callback_query()
async def query(client, callback_query):
    user = User(callback_query.from_user)
    state = get_state(user.id)
    query = callback_query.data
    if state:
        if query == 'rec_min':
            await callback_query.edit_message_caption(state.get('rec_min'),reply_markup=get_back_button())
        elif query == 'rec_rec':
            await callback_query.edit_message_caption(state.get('rec_rec'),reply_markup=get_back_button())
        elif query == 'back':
            await callback_query.edit_message_caption(state.get('result'),reply_markup=get_game_buttons(state['trailer_url']))
    else:
        await callback_query.edit_message_caption('El tiempo de espera termino por favor reinicie el bot con el comando /start')