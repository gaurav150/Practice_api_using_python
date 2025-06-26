import requests
from marshmallow import ValidationError
from common_utils.common_methods import https_catch_errors, request_exception_error
from joke_schema_validation import JokeSchema
# get method in api
url_joke = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url=url_joke)
try:

    response.raise_for_status()
    print(f"✅ Response code is {response.status_code}")

    data = response.json()
    print("🌐 Raw JSON Response:", data)

    # ✅ Validate JSON response using Marshmallow schema
    schema = JokeSchema()
    validated_data = schema.load(data)
    print("✅ Schema validated successfully!")
    print("Setup:", validated_data['setup'])
    print("Punchline:", validated_data['punchline'])

except ValidationError as val_err:
    print("❌ Schema validation failed!")
    print(val_err.messages)

except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response, http_err)

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




