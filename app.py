import requests
from click.types import convert_type

API_KEY = "dc417f2f9a3c398912efd50e1c480f81"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params ={
        "q":city,
        "appid":API_KEY,
        "units":"metric"
    }
    response = requests.get(BASE_URL, params=params)
    print(f"la url es {response.url}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_weather(data):
    city = data["name"]
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    return {
        "city":city,
        "temperature":temperature,
        "description":description,
        "humidity":humidity,
        "wind_speed":wind_speed
    }

city="Londres"
data = fetch_weather(city)
if data:
   parsed_data = parse_weather(data)
   print(parsed_data)