from pyrogram import Client

api_id = 25566003
api_hash = "f36cd30cf88e8a3030cc9b714e75c932"
bot_token = "6973403026:AAFCcqRrZCnCmDs997kQwzzzAKZQPTpdsK0"
plugins = dict(root="plugins")

app = Client("my_account", plugins=plugins, api_id=api_id, api_hash=api_hash, bot_token=bot_token)

app.run()