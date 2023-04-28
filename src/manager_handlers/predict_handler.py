import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery, Message

from utils.config_reader import config


def predict(message: types.Message):
    url = config.server_url.get_secret_value()
    payload = dict(bot_guid=config.bot_guid.get_secret_value(),
                   message=str(message.text), client_id=message.from_user.id)
    r = requests.post(url, json=payload)
    if r.status_code != 200:
        if r.status_code == 404:
            print(str(message.text))
            return message.answer(
                "Команда не найдена, пожалуйста, проверьте ее правильность или спросите другой вопрос")
        if r.status_code == 273:
            return message.answer(
                "Спасибо за вашу помощь, мы учтем это при следующем обучении бота")
    answer = r.json()['answer']
    return message.answer(answer)
