import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery

from utils.config_reader import config

def predict(message: types.Message):
    url = config.server_url.get_secret_value()
    payload = dict(bot_guid=config.bot_guid.get_secret_value(), message=str(message.text), client_id=message.from_user.id)
    print(url, payload)
    r = requests.post(url, json=payload)
    print(r.json())
    answer = r.json()['answer']
    return message.answer(answer)
