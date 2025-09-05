from calendar import error

from click.types import convert_type
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "dc417f2f9a3c398912efd50e1c480f81"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

'''
Realiza una solicitud a la API de OpenWeatherMap y devuelve los datos del clima para la ciudad dada.'''


def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    print(f"la url es {response.url}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


'''
Parsea los datos del clima y devuelve un diccionario con la información relevante.'''


def parse_weather(data):
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }


@app.route('/', methods=["GET", "POST"])
def home():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        data = fetch_weather(city)
        if data:
            weather = parse_weather(data)
        else:
            error = f"No se encontraron datos para la ciudad '{city}'."
    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

##if __name__ == "__main__":
##    app.run()
