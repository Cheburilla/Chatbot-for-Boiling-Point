import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from config_reader import config
import requests


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="MarkdownV2")
# Диспетчер
dp = Dispatcher()

url = config.server_url

@dp.message(Command("predict"))
async def predict(message: types.Message):
    r = requests.post(url, data={"bot_guid": config.bot_guid, "message": str(message)})
    answer = r.json()['answer']
    await message.answer(answer)

