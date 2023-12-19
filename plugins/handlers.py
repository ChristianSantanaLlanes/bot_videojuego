from pyrogram import Client, filters

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    nombre = message.from_user.first_name
    await message.reply(f"Hola {nombre}")