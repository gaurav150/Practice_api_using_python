import requests

from common_utils.common_methods import https_catch_errors, request_exception_error

# get method in api
url_joke = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url=url_joke)
try:
    response.raise_for_status()
    print(f"response code is {response.status_code}")
    data = response.json()
    print(response.json())
    print(data['setup'])
    print(data['punchline'])
except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response,http_err)

except requests.exceptions.RequestException as err:
    request_exception_error(err)

# sunrise and set time using get methods with passing some parameters
parameters = {
    "lat":12.971599,
    "lng":77.594566,
    # "formatted":0 here formatted 0 means timing will be in 24 hours format
}
url_sunset_sunrise = "https://api.sunrise-sunset.org/json"
response_sun_movement_timing =  requests.get(url=url_sunset_sunrise,params=parameters)
try:
    response_sun_movement_timing.raise_for_status()
    print(f"response code of sun rise and sunset is {response_sun_movement_timing.status_code}")
    time_data = response_sun_movement_timing.json()
    print(time_data)
    print(f"Sunrise Time is {time_data['results']['sunrise']} in UTC")
    print(f"Sunset Time is {time_data['results']['sunset']} in UTC")

except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response,http_err)

except requests.exceptions.RequestException as err:
    request_exception_error(err)




