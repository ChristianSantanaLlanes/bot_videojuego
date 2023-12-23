from pyrogram import Client, filters
from content.texts import TEXTS

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