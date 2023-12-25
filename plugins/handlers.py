from pyrogram import Client, filters
from content.texts import (
    start_text,
    info_text,
    help_text
)
from extra_functionality.extra_funcionality import create_first_state
from models.User import User
from helpers.service import get_new_user_telegram_or_create
from plugins.buttons import get_start_button


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    user_data = message.from_user
    user = get_new_user_telegram_or_create(user_data)
    nombre = user.first_name
    await message.reply(start_text.format(nombre), reply_markup=get_start_button())

@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply(help_text)

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