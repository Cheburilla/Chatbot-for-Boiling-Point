import asyncio
import logging

import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.config_reader import config
from keyboard.for_questions import get_keyboard
from manager_handlers import handlers, predict_handler
from manager_handlers.handlers import Form


storage = MemoryStorage()
    
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="MarkdownV2")
# Диспетчер
dp = Dispatcher(bot=bot, storage=storage)
# Регистрация хэндлеров
# регистрация команды /start
dp.register_message_handler(callback=handlers.cmd_book, commands = ["book"])
dp.register_message_handler(callback=handlers.cmd_start, commands=['start'])
dp.register_message_handler(callback=handlers.process_name, state=Form.name)
dp.register_message_handler(callback=handlers.process_hall, state=Form.hall)
dp.register_message_handler(callback=handlers.process_date, state=Form.date)
dp.register_message_handler(callback=handlers.process_beg_t, state=Form.begin_time)
dp.register_message_handler(callback=handlers.process_end_t, state=Form.end_time)
dp.register_message_handler(callback=handlers.process_phone, state=Form.phone)
dp.register_message_handler(callback=handlers.process_comments, state=Form.comments)
dp.register_message_handler(callback=handlers.process_event_name, state=Form.event_name)
dp.register_message_handler(callback=predict_handler.predict)
dp.register_callback_query_handler(callback=handlers.callback_handlers)
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
