from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from models.Game import game_from_dict
from models.Meta import Meta

keyboard_buttons_text = {
    'sarch_game': '🔎 Buscar Videojuego',
    'help': '🆘 Ayuda',
    'info': 'Info',
    'siguiente': '⏩',
    'anterior': '⏪'
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
                KeyboardButton(keyboard_buttons_text['help']),
                KeyboardButton(keyboard_buttons_text['info'])
            ]
        ],
        resize_keyboard=True,
        is_persistent=True
    )
    return start_button

def get_list_game_buttons(resp, meta:Meta):
    list_games = []
    markup = InlineKeyboardMarkup(list_games)
    list = []
    page_count = meta.pagination.page_count
    page = meta.pagination.page
    for respuest in resp:
        game = game_from_dict(respuest)
        button = InlineKeyboardButton(game.attributes.name, callback_data=f'game-{game.id}')
        list.append(button)
    list_games.append(list)
    menu_buttons = []
    if page < page_count:
        next_button = [
            InlineKeyboardButton(keyboard_buttons_text['siguiente'], callback_data='next_page')
        ]
        menu_buttons.append(next_button)
    if page > 1:
        back_button = [
            InlineKeyboardButton(keyboard_buttons_text['anterior'], callback_data='back_page')
        ]
        menu_buttons.append(back_button)
    list_games.append(menu_buttons)
    return markup