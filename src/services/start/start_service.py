from aiogram import types

from src.menu_keyboard import get_menu_keyboard


async def start_handler(event: types.Message):


    await event.answer(
        f"Привет! Это ТеормехБот, как я могу тебе помочь?",
        parse_mode=types.ParseMode.HTML,
        reply_markup=get_menu_keyboard()
    )