import requests


def account_post() ->None:

    url = "https://demoqa.com/swagger/#/Account/AccountV1AuthorizedPost"
    parameter = {
      "userName": "rahul",
      "password": "shetty"
    }

    response = requests.get(url=url,params=parameter)
    try:
        response.raise_for_status()
        print("response code for the url is ",response.status_code)
    except Exception as e:
        print(f"Error occurred {e}.")
    finally:
        print("response code for the url is ", response.status_code)
def account_authorization_post()->None:
    url = "https://demoqa.com/Account/v1/GenerateToken"
    parameter = {
      "userName": "rahul",
      "password": "shetty"
    }
    response = requests.get(url=url,params=parameter)
    print("response code for the url is",response.status_code)

def account_user()->None:
    url = "https://demoqa.com/Account/v1/User"
    parameter = {
        "userName": "rahul",
        "password": "sinha"
    }
    response = requests.get(url=url,params=parameter)
    response.raise_for_status()
    print("status code for the add user is ",response.status_code)


account_post()
account_authorization_post()
account_user()