from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

API_KEY = "ce5d60cd6fe82eb2e97f74c8a764342f"

continent_cities = {
    "asia": "Tokyo",
    "europe": "London",
    "north america": "New York",
    "south america": "São Paulo",
    "africa": "Cairo",
    "australia": "Sydney",
    "antarctica": "McMurdo Station"
}


def get_weather(city):
    """Fetch weather details from OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 401:
            return "Invalid API Key. Check OpenWeatherMap API key."
        elif response.status_code != 200:
            return f"Error fetching weather: {data.get('message', 'Unknown error')}"

        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Current weather in {city}: {weather_desc}, {temp}°C."

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    for continent, city in continent_cities.items():
        if continent in user_input:
            weather = get_weather(city)
            return jsonify({"reply": weather})

    return jsonify({
        "reply": "Please specify a continent (Asia, Europe, North America, South America, Africa, Australia, or Antarctica)."
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)