import requests
import json

from common_utils.common_methods import https_catch_errors, request_exception_error

API_KEY = "2ca78f5fdf7b04d1536d8701c17e27f2"
# INSTEAD OF DISPLAYING HERE KEY WE CAN USE
# export owm_api_key=2ca78f5fdf7b04d1536d8701c17e27f2 to set this as environment variable
city = "Bangalore"
url = "http://api.openweathermap.org/data/2.5/weather"
parameter = {
        "q":city,
        "appid":API_KEY,
        "units":"metric"
}
response = requests.get(url=url,params=parameter)
try:
    response.raise_for_status()
    if response.status_code == 200:
        data = response.json()
        print(data)
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        with open("weather_test.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)
            print("Data Written to api_test.json file ,successfully")

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response,http_err)

except requests.exceptions.RequestException as err:
    # This catches network-related errors (e.g., DNS failure, refused connection)
    request_exception_error(err)




print("response Headers value are; ",response.headers)
print("response reason is given :",response.reason)
print("Time Elapsed to get response is",response.elapsed)