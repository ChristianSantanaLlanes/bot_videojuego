from pyrogram import Client, filters


@Client.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)


@Client.on_message(filters.text & filters.private, group=1)
async def echo_reversed(client, message):
    await message.reply(message.text[::-1])