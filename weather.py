import datetime as dt
import requests

# OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "YOUR_API_KEY"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * 9 / 5 + 32
    return celsius, fahrenheit

def get_weather(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()
    current_time = dt.datetime.now() + dt.timedelta(seconds=response['timezone'])
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'], dt.timezone.utc)
    sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'], dt.timezone.utc)
    formatted_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    formatted_sunrise_time = sunrise_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    formatted_sunset_time = sunset_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    return (f"🕒 Current time in {city}: {formatted_current_time}\n"
            f"🌡️ Temperature: {temp_celsius:.2f}°C ({temp_fahrenheit:.2f}°F)\n"
            f"👍 Feels like: {feels_like_celsius:.2f}°C ({feels_like_fahrenheit:.2f}°F)\n"
            f"🌬️ Wind speed: {wind_speed} m/s\n"
            f"💧 Humidity: {humidity}%\n"
            f"☁️ Description: {description}\n"
            f"🌅 Sunrise: {formatted_sunrise_time}\n"
            f"🌇 Sunset: {formatted_sunset_time}")
