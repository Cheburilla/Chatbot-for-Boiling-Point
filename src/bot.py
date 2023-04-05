import asyncio
import logging

import requests
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command, Text

from utils.config_reader import config


async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    # Объект бота
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="MarkdownV2")
    # Диспетчер
    dp = Dispatcher()

    url = config.server_url


    @dp.message(Text())
    async def predict(message: types.Message):
        payload = {"bot_guid": config.bot_guid, "message": str(message)}
        r = requests.post(url, data=payload)
        answer = r.json()['answer']
        await message.answer(answer)

if __name__ == "__main__":
    asyncio.run(main())
