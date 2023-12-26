import json
import os
from models.Game import game_from_dict
from models.Meta import meta_from_dict
from models.User import User
import requests
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN") 
URL_BACKEND = 'https://strapi-production-2d60.up.railway.app/api'
headers = {
    'Authorization': f'Bearer {token}'
}

def create_telegram_user(user):
    args = {
        'data': {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_id': user.id,
            'username': user.username
        }
    }
    url = f"{URL_BACKEND}/telegram-users"
    resp = requests.post(
        url,
        json=args,
        headers=headers
    )

def get_new_user_telegram_or_create(data):
    user = User(data)
    params = f'filters[user_id][$eq][0]={user.id}'
    url = f"{URL_BACKEND}/telegram-users?{params}"
    response = requests.get(url)
    data = response.content
    data_json = json.loads(data)
    if len(data_json['data']) == 0:
        create_telegram_user(user)
        return user
    else:
        return user
    
def get_game_by_name(name, page=1):
    params = f'sort[0]=name:asc&filters[name][$containsi]={name}&pagination[page]={page}&populate[cover]=*'
    url = f"{URL_BACKEND}/games?{params}"
    response = requests.get(url)
    data = response.content
    data_json = json.loads(data)
    if len(data_json['data']) == 0:
        games = False
        meta = False
        return games, meta
    else:
        games = data_json['data']
        meta = meta_from_dict(data_json['meta'])
        return games, meta
    
def get_game_by_id(id):
    url = f"{URL_BACKEND}/games/{id}?populate=*"
    response = requests.get(url)
    data = response.content
    data_json = json.loads(data)
    if data_json['data']:
        game = game_from_dict(data_json['data'])
        return game
    else:
        return False