import requests

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        	"latitude": 10.823,
            "longitude": 106.6296,
            "hourly": ["temperature_2m", "weather_code", "rain"],
            "timezone": "GMT+7",
    }
    response = requests.get(url, params=params)
    return response.json()