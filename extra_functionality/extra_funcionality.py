from helpers.service import get_game_by_name
from state.state import set_state
from models.Game import game_from_dict
from models.User import User
from plugins.buttons import get_game_buttons
from content.texts import game_text, error_text_game_not_found


async def get_game_and_respond(answer):
    user = User(answer.from_user)
    resp = get_game_by_name(answer.text)
    if resp:
        data = resp[0]
        result = game_from_dict(data)
        name = result.attributes.name
        description = result.attributes.description
        photo = result.attributes.cover.data.attributes.url 
        trailer_url = result.attributes.trailer_url
        text_cap = game_text.format(
            name=name,
            description=description,
        )
        set_state(user.id, 
                  result.attributes.req_min, 
                  result.attributes.rec_rec, 
                  text_cap, 
                  trailer_url,
                  False)
        await answer.reply_photo(photo, caption=text_cap, reply_markup=get_game_buttons(trailer_url))
    else:
        set_state(user.id,buscando=False)
        await answer.reply(error_text_game_not_found)