from aiogram.types import Message, CallbackQuery
from keyboard.for_questions import get_keyboard


async def cmd_start(message: Message):
    await message.answer(f"Привет\!, {message.from_user.first_name}", reply_markup=get_keyboard(['yes', 'no'], "Да", "Нет"))

async def cmd_user(message: Message):
    await message.answer(f"ТЕКСТ", reply_markup=get_keyboard(['organizer', 'user', 'participant'], "Организатор", "Просто интересуюсь", "Участник"))

async def cmd_remind(message: Message):
    await message.answer(f"ТЕКСТ", reply_markup=get_keyboard(['dont_book', 'book', 'reg'], 
                                                             "Я не бронировал(а) и не регистрировал(а) мероприятие и не знаю как это сделать", 
                                                             "Я бронировал(а) мероприятие, но не регистрировал(а) на Leader-ID", 
                                                             "Я регистрировал(а) мероприятие"))
    

async def callback_handlers(callback: CallbackQuery):
    if callback.data == 'yes':
        await callback.message.answer('Вы ответили да')
    elif callback.data == 'no':
        await callback.message.answer("Вы ответили нет")
    elif callback.data == 'organizer':
        await callback.message.answer('Организатор')
    elif callback.data == 'user':
        await callback.message.answer("Просто интересуюсь")
    elif callback.data == 'participant':
        await callback.message.answer("Участник")
    elif callback.data == 'dont_book':
        await callback.message.answer("предложение о брони")
    elif callback.data == 'book':
        await callback.message.answer("инструкция1")
    elif callback.data == 'reg':
        await callback.message.answer("инструкция2")

async def cmd_help(message: Message):
    await message.answer(f"Помощь")




