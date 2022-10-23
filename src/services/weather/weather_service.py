from aiogram import types

from src.services.weather.weather_api import get_weather


async def get_weather_service_response():
    data = await get_weather()
    current_temperature = int(data.current_weather.temperature)

    response = f"Погода в СПБ: <b>{current_temperature}°C</b>"
    return response


async def weather_handler(event: types.Message):
    response = await get_weather_service_response

    await event.answer(
        response,
        parse_mode=types.ParseMode.HTML
    )