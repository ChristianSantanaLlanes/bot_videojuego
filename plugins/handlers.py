from pyrogram import Client, filters
from content.texts import (
    error_text_game_not_found, 
    start_text,
    info_text,
    game_text
)
from helpers.state import get_state, set_state
from models.Game import game_from_dict
from models.User import User

from helpers.service import get_game_by_name, get_new_user_telegram_or_create
from plugins.buttons import get_back_button, get_game_buttons

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    user_data = message.from_user
    user = get_new_user_telegram_or_create(user_data)
    nombre = user.first_name
    await message.reply(start_text.format(nombre))

@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply('Esta es la ayuda')

@Client.on_message(filters.command('info') & filters.private)
async def info(client, message):
    user = User(message.from_user)
    username = user.username if user.username != '' else 'No Username'
    text = info_text.format(
        first_name=user.first_name, 
        last_name=user.last_name,
        username=username,
        id=user.id 
    )
    await message.reply(text)

@Client.on_message(filters.text & filters.private)
async def get_text(client, message):
    user = User(message.from_user)
    text = message.text
    resp = get_game_by_name(text)
    if resp:
        data = resp[0]
        result = game_from_dict(data)
        name = result.attributes.name
        description = result.attributes.description
        photo = result.attributes.cover.data.attributes.url 
        trailer_url = result.attributes.trailer_url
        text_cap = game_text.format(
            name=name,
            description=description,
        )
        set_state(user.id, result.attributes.req_min, result.attributes.rec_rec, text_cap, trailer_url)
        await message.reply_photo(photo, caption=text_cap, reply_markup=get_game_buttons(trailer_url))
    else:
        await message.reply(error_text_game_not_found)

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
            await callback_query.edit_message_caption(state.get('result'),reply_markup=get_game_buttons(state.get('trailer_url')))
    else:
        await callback_query.edit_message_caption('El tiempo de espera termino por favor reinicie el bot con el comando /start')