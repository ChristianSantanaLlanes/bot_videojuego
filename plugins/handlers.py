from pyrogram import Client, filters
from content.texts import TEXTS
from models.User import User

from helpers.service import get_new_user_telegram_or_create

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    user_data = message.from_user
    user = get_new_user_telegram_or_create(user_data)
    nombre = user.first_name
    await message.reply(TEXTS['start_text'].format(nombre))

@Client.on_message(filters.command('data'))
async def data(client, message):
    user_id = message.from_user
    print(str(user_id))

@Client.on_message(filters.command('help'))
async def help(client, message):
    await message.reply('Esta es la ayuda')

@Client.on_message(filters.command('info'))
async def info(client, message):
    user = User(message.from_user)
    username = user.username if user.username != '' else 'No Username'
    text = TEXTS['info_text'].format(
        first_name=user.first_name, 
        last_name=user.last_name,
        username=username,
        id=user.id 
    )
    await message.reply(text)
