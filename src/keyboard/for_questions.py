from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard(callback_name : list[str], *args) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i, name_button in enumerate(args):
        keyboard.add(InlineKeyboardButton(text=name_button, callback_data=callback_name[i]))
    return keyboard
