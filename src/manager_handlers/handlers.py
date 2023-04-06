from aiogram.types import Message, CallbackQuery
from keyboard.for_questions import get_keyboard
from manager_handlers.reply_dict import reply_dict


async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}\!\n\nЯ – интеллектуальный чат\-бот, готовый ответить на ваши вопросы " \
                         "о Точке кипения ОмГТУ\. Давайте начнём\!\n\nЗарегистрированы ли Вы на Leader\-ID\?", reply_markup=get_keyboard(['yes', 'no'], "Да", "Нет"))



async def callback_handlers(callback: CallbackQuery):
    for ans in reply_dict[callback.data]:
        if len(ans) == 2:
            if ans[1] != None:
                await callback.message.answer(ans[0], reply_markup=get_keyboard(*ans[1]))
            else:
                await callback.message.answer(ans[0])
        else:
            if reply_dict[ans[0]][0][1] != None:
                await callback.message.answer(reply_dict[ans[0]][0][0], reply_markup=get_keyboard(*reply_dict[ans[0]][0][1]))
            else:
                await callback.message.answer(reply_dict[ans[0]][0][0])
