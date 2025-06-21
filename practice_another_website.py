import requests


def get_data_from_url() -> None:
    uel = "https://apichallenges.eviltester.com/sim/entities"
    response = requests.get(url=uel)
    try:
        response.raise_for_status()
        print("response code of the url is",response.status_code)
        data = response.json()
        whole_data = data["entities"]
        for ele in whole_data:
            print(ele["name"])
    except Exception as e:
        print(f"Error Occurred {e}")
    finally:
        print(f"response status code is :{response.status_code}")

get_data_from_url()