import asyncio
import logging

import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, CallbackQuery

from utils.config_reader import config
from keyboard.for_questions import get_keyboard
from manager_handlers import handlers

    
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="MarkdownV2")
# Диспетчер
dp = Dispatcher(bot=bot)
# Регистрация хэндлеров
# регистрация команды /start
dp.register_message_handler(callback=handlers.cmd_start, commands=['start'])
dp.register_callback_query_handler(callback=handlers.callback_handlers)
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
