import aiohttp

from src.services.weather.models.get_weather_response import GetWeatherResponse
from src.utils.secrets import read_secrets

secrets = read_secrets()
URL = secrets["WEATHER_API_URL"]


async def get_weather() -> GetWeatherResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            return GetWeatherResponse(await resp.json())
