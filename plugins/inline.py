from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from helpers.recortar_texto import recortar_texto

from helpers.service import get_game_by_name
from models.Game import Game, game_from_dict

def get_results(name):
    games, meta = get_game_by_name(name)
    resultados = []
    if games:
        for game in games:
            obj_game = game_from_dict(game)
            name = obj_game.attributes.name
            id = obj_game.id
            foto = obj_game.attributes.cover.data.attributes.url
            description = recortar_texto(obj_game.attributes.description, 120)
            obj = InlineQueryResultArticle(
                name,
                InputTextMessageContent(f'game~{id}~{name}'),
                thumb_url=foto,
                description=description
            )
            resultados.append(obj)
    return resultados, meta

@Client.on_inline_query()
async def inline(client, inline_query):
    query = inline_query.query
    results, meta = get_results(query)
    page = meta.pagination.page
    count_page = meta.pagination.page_count
    offset = 1
    if page < count_page:
        offset = page + 1
    await inline_query.answer(results,is_gallery=False)