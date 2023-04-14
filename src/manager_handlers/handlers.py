from aiogram.types import Message, CallbackQuery
from keyboard.for_questions import get_keyboard
from manager_handlers.reply_dict import reply_dict


async def cmd_start(message: Message):
    await message.answer_photo('https://sun9-52.userapi.com/impg/RiX6_0PL_ni4KGaTPfNCi-MFWT18jfT7L62Ytg/EoFk_1CY7ss.jpg?size=1080x1080&quality=95&sign=f2768ff45453aecfad743d2730ba6afe&type=album')
    await message.answer(f"Привет, {message.from_user.first_name}\!\n\nЕсли Вы не уверены\, что Вы хотите спросить\, " \
                         "отвечайте на мои вопросы, и я вам помогу\!😉\n\nЗарегистрированы ли Вы на Leader\-ID\?", reply_markup=get_keyboard(['yes', 'no'], "Да", "Нет"))



async def callback_handlers(callback: CallbackQuery):
    async def repl(call_data):
        for ans in reply_dict[call_data]:
            if len(ans) != 1:
                if ans[1] != None:
                    await callback.message.answer(ans[0], reply_markup=get_keyboard(*ans[1]))
                else:
                    await callback.message.answer(ans[0])
                if ans[2] != None:
                    await callback.message.answer_photo(ans[2])
            else:
                await repl(ans[0])
    await repl(callback.data)
