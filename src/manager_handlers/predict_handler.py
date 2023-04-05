import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery

from utils.config_reader import config

def predict(message: types.Message):
    url = config.server_url
    payload = {"bot_guid": config.bot_guid, "message": str(message)}
    r = requests.post(url, data=payload)
    answer = r.json()['answer']
    return answer