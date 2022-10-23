class CurrentWeather:

    def __init__(self, json):

        self.temperature: float = json["temperature"]
        self.windspeed: float = json["windspeed"]
        self.winddirection: int = json["winddirection"]
        self.weathercode: int = json["weathercode"]
        self.time: str = json["time"]
