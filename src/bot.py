import asyncio
import logging

import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message

from keyboard.for_questions import get_keyboard
from manager_handlers import handlers, predict_handler
from manager_handlers.handlers import Form
from utils.config_reader import config
from utils.phone_check import is_phone_number

storage = MemoryStorage()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="markdown")
# Диспетчер
dp = Dispatcher(bot=bot, storage=storage)
# Регистрация хэндлеров
# регистрация команды /start
dp.register_message_handler(callback=handlers.cmd_book, commands=["book"])
dp.register_message_handler(callback=handlers.cmd_start, commands=['start'])
dp.register_message_handler(callback=handlers.process_name, state=Form.name)
dp.register_message_handler(handlers.process_hall_invalid, lambda message: message.text not in [
                            "Малый зал", "Большой зал"], state=Form.hall)
dp.register_message_handler(callback=handlers.process_hall, state=Form.hall)
dp.register_message_handler(handlers.process_date_invalid, lambda message: not handlers.is_date(
    message.text) or not handlers.is_date_now(message.text), state=Form.date)
dp.register_message_handler(callback=handlers.process_date, state=Form.date)
dp.register_message_handler(handlers.process_beg_t_invalid, lambda message: not handlers.is_time(
    message.text), state=Form.begin_time)
dp.register_message_handler(
    callback=handlers.process_beg_t, state=Form.begin_time)
dp.register_message_handler(handlers.process_end_t_invalid,
                            lambda message: not handlers.is_time(message.text), state=Form.end_time)
dp.register_message_handler(
    callback=handlers.process_end_t, state=Form.end_time)
dp.register_message_handler(handlers.process_phone_invalid,
                            lambda message: not is_phone_number(message.text), state=Form.phone)
dp.register_message_handler(callback=handlers.process_phone, state=Form.phone)
dp.register_message_handler(
    callback=handlers.process_comments, state=Form.comments)
dp.register_message_handler(
    callback=handlers.process_event_name, state=Form.event_name)
dp.register_message_handler(callback=predict_handler.predict)
dp.register_callback_query_handler(callback=handlers.callback_handlers)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
