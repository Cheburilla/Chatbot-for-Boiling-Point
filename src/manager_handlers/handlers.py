from datetime import datetime

import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (CallbackQuery, Message,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove)

from keyboard.for_questions import get_keyboard
from manager_handlers.reply_dict import reply_dict


class Form(StatesGroup):
    name = State()
    hall = State()
    date = State()
    begin_time = State()
    end_time = State()
    phone = State()
    comments = State()
    event_name = State()


async def cmd_book(message: Message):
    await Form.name.set()
    await message.answer('На какое имя будет бронь\?')

# async def process_name(message: Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text

#     await Form.next()


async def process_name(message: Message, state: FSMContext):
    # Update state and data
    await Form.next()
    async with state.proxy() as data:
        data['name'] = message.text

    # Configure ReplyKeyboardMarkup
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Большой зал", "Малый зал")

    await message.answer("В каком зале будет проводиться мероприятие\?", reply_markup=markup)


async def process_hall(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['hall'] = message.text

        # Remove keyboard
        markup = ReplyKeyboardRemove()

        await Form.next()
        await message.answer("Введите дату мероприятия в формате ДД\.ММ\.ГГГГ", reply_markup=markup)


async def process_date(message: Message, state: FSMContext):

    # try:
    #     date = datetime.strptime(message.text, '%d.%m.%Y')
    # except:
    #     return await message.answer("Пожалуйста, введите действительную дату в формате ДД.ММ.ГГГГ.")

    await Form.next()
    await state.update_data(date=datetime.strptime(message.text, '%d.%m.%Y'))

    await message.answer("Введите время начала мероприятия в формате ЧЧ\:ММ")


async def process_beg_t(message: Message, state: FSMContext):

    # try:
    #     b_t = datetime.strptime(message.text, '%H:%M.')
    # except:
    #     return await message.answer("Пожалуйста, введите действительное время в формате ДД.ММ.ГГГГ.")

    await Form.next()
    await state.update_data(begin_time=datetime.strptime(message.text, '%H:%M'))

    await message.answer("Введите время конца мероприятия в формате ЧЧ\:ММ")


async def process_end_t(message: Message, state: FSMContext):

    # try:
    #     e_t = datetime.strptime(message.text, '%H:%M.')
    # except:
    #     return await message.answer("Пожалуйста, введите действительное время в формате ДД.ММ.ГГГГ.")

    await Form.next()
    await state.update_data(end_time=datetime.strptime(message.text, '%H:%M'))

    await message.answer("Оставьте номер телефона\, с вами может связаться администратор📞")


async def process_phone(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

        await Form.next()
        await message.answer("Введите уточнения по оборудованию и оформлению зала\, например \"организовать деление зала стеллажами\"")


async def process_comments(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['comments'] = message.text

        await Form.next()
        await message.answer("Введите *исчерпывающее* и *информативное* название Вашего мероприятия")


async def process_event_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['event_name'] = message.text

        await message.answer(f"Проверьте Ваши данные:\n\nВы забронировали мерпориятие на имя <b>{data['name']}</b>\nМесто проведения Вашего мероприятия - <b>{data['hall']}</b>\nВаше меропритятие будет проводиться <b>{data['date'].strftime('%d.%m.%Y')}</b> с <b>{data['begin_time'].strftime('%H:%M')}</b> до <b>{data['end_time'].strftime('%H:%M')}</b>\nВаш номер телефона - <b>{data['phone']}</b>\nВаши требования по оборудованию и оформлению зала: <b>{data['comments']}</b>\nНазвание Вашего мероприятия - <b>{data['event_name']}</b>",
                             parse_mode='HTML')

    # Finish conversation
    await state.finish()


async def cmd_start(message: Message):
    await message.answer_photo('https://sun9-52.userapi.com/impg/RiX6_0PL_ni4KGaTPfNCi-MFWT18jfT7L62Ytg/EoFk_1CY7ss.jpg?size=1080x1080&quality=95&sign=f2768ff45453aecfad743d2730ba6afe&type=album')
    await message.answer(f"Привет, {message.from_user.first_name}\!\n\nЕсли Вы не уверены\, что Вы хотите спросить\, "
                         "отвечайте на мои вопросы, и я вам помогу\!😉\n\nЗарегистрированы ли Вы на Leader\-ID\?", reply_markup=get_keyboard(['yes', 'no'], "Да", "Нет"))


async def cmd_reg(message: Message):
    for ans in reply_dict['reg_yes']:
        if len(ans) != 1:
            if ans[0] != None:
                await message.answer(ans[0])

            if ans[1] != None:
                await message.answer(ans[0], reply_markup=get_keyboard(*ans[1]))

            if ans[2] != None:
                await message.answer_photo(ans[2])


async def callback_handlers(callback: CallbackQuery):
    async def repl(call_data):
        for ans in reply_dict[call_data]:
            if len(ans) != 1:
                if ans[0] != None:
                    await callback.message.answer(ans[0])

                if ans[1] != None:
                    await callback.message.answer(ans[0], reply_markup=get_keyboard(*ans[1]))

                if ans[2] != None:
                    await callback.message.answer_photo(ans[2])

            else:
                await repl(ans[0])
    await repl(callback.data)
