from pyrogram import Client, filters
from content.texts import (
    error_text_game_not_found, 
    start_text,
    info_text,
    game_text
)
from models.Game import game_from_dict
from models.User import User

from helpers.service import get_game_by_name, get_new_user_telegram_or_create

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
    text = message.text
    resp = get_game_by_name(text)
    if resp:
        data = resp[0]
        result = game_from_dict(data)
        name = result.attributes.name
        description = result.attributes.description
        photo = result.attributes.cover.data.attributes.url 
        text = game_text.format(
            name=name,
            description=description,
)
        await message.reply_photo(photo, caption=text)
    else:
        await message.reply(error_text_game_not_found)