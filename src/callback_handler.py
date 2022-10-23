from aiogram import types

from src.menu_keyboard import get_menu_keyboard
from src.services.weather.weather_service import get_weather_service_response

CALLBACKS = {
    "weather": get_weather_service_response
}


async def process_callback(callback_query: types.CallbackQuery):

    route = callback_query.data
    callback = CALLBACKS[route]
    response = await callback()

    await callback_query.message.answer(
        response,
        parse_mode=types.ParseMode.HTML,
        reply_markup=get_menu_keyboard()
    )
