from src.services.weather.models.current_weather import CurrentWeather


class GetWeatherResponse:

    def __init__(self, json):

        self.latitude: float = json["latitude"]
        self.longitude: float = json["longitude"]
        self.generationtime_ms: float = json["generationtime_ms"]
        self.utc_offset_seconds: int = json["utc_offset_seconds"]
        self.timezone: str = json["timezone"]
        self.timezone_abbreviation: str = json["timezone_abbreviation"]
        self.elevation: int = json["elevation"]
        self.current_weather: CurrentWeather = CurrentWeather(json["current_weather"])
