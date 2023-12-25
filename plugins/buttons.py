from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard_buttons_text = {
    'sarch_game': '🔎 Buscar Videojuego',
    'help': '🆘 Ayuda'
}

def get_game_buttons(trailer_url):
    game_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Requisitos minimos', callback_data='rec_min')
            ],
            [
                InlineKeyboardButton('Requisitos Recomendados', callback_data='rec_rec')
            ],
            [
                InlineKeyboardButton('Ver Trailer', url=trailer_url)
            ]
        ]
    )
    return game_buttons

def get_back_button():
    back_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('🔙', callback_data='back')]
        ]
    )
    return back_button

def get_start_button():
    start_button = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(keyboard_buttons_text['sarch_game'])
            ],
            [
                KeyboardButton(keyboard_buttons_text['help'])
            ]
        ],
        resize_keyboard=True,
        is_persistent=True
    )
    return start_button