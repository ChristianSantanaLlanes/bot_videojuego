from helpers.service import get_game_by_name
from state.state import get_state, set_state
from models.Game import Game
from models.User import User
from plugins.buttons import get_game_buttons, get_list_game_buttons
from content.texts import (game_text, 
                           error_text_game_not_found, 
                           game_list_text,
                           text_with_cancel,
                           search_text)
from pyrocon import patch
from pyrogram import filters


async def get_game_and_respond(client, user:User, game:Game):
        name = game.attributes.name
        description = game.attributes.description
        photo = game.attributes.cover.data.attributes.url 
        trailer_url = game.attributes.trailer_url
        text_cap = game_text.format(
            name=name,
            description=description,
        )
        set_state(user.id, 
                  game.attributes.req_min, 
                  game.attributes.rec_rec, 
                  text_cap, 
                  trailer_url,
                  False)
        await client.send_photo(user.id, photo, caption=text_cap, reply_markup=get_game_buttons(trailer_url))

async def get_games_list_and_respond(client, answer):
    user = User(answer.from_user)
    resp, meta = get_game_by_name(answer.text)
    if resp:
        text = game_list_text.format(total=meta.pagination.total,
                                     page=meta.pagination.page,
                                     page_count=meta.pagination.page_count)
        set_state(user.id, buscando=False)
        await answer.reply(text, reply_markup=get_list_game_buttons(resp, meta))
    else: 
        await answer.reply(error_text_game_not_found)
        quiz = patch(client)
        answer = await quiz.ask(answer,search_text,filter=filters.text)
        if answer.text:
            await get_games_list_and_respond(client, answer)
        if answer.cancel:
            set_state(user.id, buscando=False)
            await client.send_message(user.id, text_with_cancel)

async def create_first_state(id):
    state = get_state(id)
    if state:
          return state
    else:
        set_state(id)
        return get_state(id)