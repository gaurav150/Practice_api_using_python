import requests
import json
# import os

from weather_validation import WeatherSchema
from marshmallow import ValidationError
from common_utils.common_methods import https_catch_errors, request_exception_error

# You can swap to os.getenv later for security
API_KEY = "2ca78f5fdf7b04d1536d8701c17e27f2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather_data(city):
    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=parameters)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        https_catch_errors(response, http_err)
    except requests.exceptions.RequestException as err:
        request_exception_error(err)
    return None


def validate_weather_data(data):
    try:
        schema = WeatherSchema()
        return schema.load(data)
    except ValidationError as val_err:
        print("❌ Validation Error:", val_err.messages)
        return None


def display_weather_info(validated_data, city):
    weather = validated_data["weather"][0]["description"]
    temperature = validated_data["main"]["temp"]
    humidity = validated_data["main"]["humidity"]
    wind_speed = validated_data["wind"]["speed"]

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


def write_to_file(data, filename="weather_test.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Data written to {filename} successfully")


def main():
    city = "Bangalore"
    response = fetch_weather_data(city)

    if response and response.status_code == 200:
        data = response.json()
        validated_data = validate_weather_data(data)
        print(f"weather data is {data}")

        if validated_data:
            display_weather_info(validated_data, city)
            write_to_file(data)

        print("Response headers:", response.headers)
        print("Response reason:", response.reason)
        print("Time elapsed for response:", response.elapsed)



if __name__ == "__main__":
    main()
    print("response data in console")
