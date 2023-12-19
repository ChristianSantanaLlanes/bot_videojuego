from pyrogram import Client
plugins = dict(root="plugins")

app = Client("my_account", plugins=plugins)

app.run()