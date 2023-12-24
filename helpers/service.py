import json
from models.User import User
import requests
token = 'd0434777c591f1cb7894a3202ca3dd01ada108c543e18b991809fb324553e5b2d072d1bd4bcd3558b88e7da4cb188643eb41a2d3c344e70f0c32ed2c44e7ceb32ba8b25ffb88abfe6c3af6e1fe53f258ec8b8e5c76d3da8dc53d7c96188a22d3bee28f30dcc4e9a6b9d61c0521db72308d7d613abf298f6941dc348e4c250975'
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
    print(resp.content)

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