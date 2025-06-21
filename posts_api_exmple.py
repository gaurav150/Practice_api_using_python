import requests

from common_utils.common_methods import https_catch_errors, request_exception_error

url =  "https://jsonplaceholder.typicode.com/posts"
data_sending = {
    "title":"First_Try",
    "body":"This is My first Try",
    "userId":1
}
response_post= requests.post(url=url,json=data_sending)
try:
    print(response_post.content)
    if response_post.status_code == 201:
        print("Success")
        print(response_post.json())
    else:
        print("failed")

except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response_post,http_err)

except requests.exceptions.RequestException as err:
    request_exception_error(err)

