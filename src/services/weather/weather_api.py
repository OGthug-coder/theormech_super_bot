import aiohttp

from src.services.weather.models.get_weather_response import GetWeatherResponse

SPB_LATITUDE = "59.93"
SPB_LONGITUDE = "30.30"
TIMEZONE = "Europe%2FMoscow"

URL = f"https://api.open-meteo.com/v1/forecast?" \
      f"latitude={SPB_LATITUDE}&" \
      f"longitude={SPB_LONGITUDE}&" \
      f"current_weather=true&timezone={TIMEZONE}"


async def get_weather() -> GetWeatherResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            return GetWeatherResponse(await resp.json())
