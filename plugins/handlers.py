from pyrogram import Client, filters
from content.texts import (
    start_text,
    info_text,
    help_text,
    search_text,
    text_with_cancel
)
from pyrocon import patch
from extra_functionality.extra_funcionality import create_first_state, get_games_list_and_respond
from models.User import User
from helpers.service import get_new_user_telegram_or_create
from plugins.buttons import get_start_button
from state.state import set_state


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

@Client.on_message(filters.command('search') & filters.private)
async def search(client, message):
    user = User(message.from_user)
    set_state(user.id, buscando=True)
    quiz = patch(client)
    answer = await quiz.ask(message,search_text,filter=filters.text)
    if answer.text:
        await get_games_list_and_respond(client, answer)
    if answer.cancel:
        set_state(user.id, buscando=False)
        await client.send_message(user.id, text_with_cancel)