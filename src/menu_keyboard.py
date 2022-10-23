from aiogram import types


def get_menu_keyboard():

    weather_button = types.InlineKeyboardButton("Погода в СПБ", callback_data="weather")

    first_row = [weather_button]

    rmk = types.InlineKeyboardMarkup(inline_keyboard=[first_row])

    return rmk
