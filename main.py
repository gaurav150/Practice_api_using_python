import requests
import json
api_url = "https://catfact.ninja/fact"

response = requests.get(url=api_url)
response.raise_for_status()
if response.status_code == 200:
    data = response.json()
    print(data)
    with open("api_test.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)
        print("Data Written to api_test.json file ,successfully")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")




