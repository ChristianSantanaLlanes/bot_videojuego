from pyrogram import Client
# import uvloop
plugins = dict(root="plugins")
# uvloop.install()
app = Client("my_account", plugins=plugins)

app.run()