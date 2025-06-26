import requests

from common_utils.common_methods import https_catch_errors, request_exception_error

url = "https://jsonplaceholder.typicode.com/posts/1"
data_updating = {
    "id":1,
    "title":"First_Try",
    "body":"This is My first Try in put",
    "userId":1
}
# here in this method we are sending whole data instead of particular data which changed

# response_put =  requests.get(url)
global response_put
try:
    response_put = requests.put(url, data_updating)
    response_put.raise_for_status()
    print(response_put.json())
except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response_put,http_err)

except requests.exceptions.RequestException as err:
    request_exception_error(err)

# ========================Patch Method ======================

data_patching =  {
    "id":1,
    "title":"First Try in Patch"
}
# patching is done only when only some data of particular id changed
# in this method rest of the unchanged data will remain same
global response_patch
try:
    response_patch = requests.patch(url, data_patching)
    print(f"response patching done {response_patch.json()}")
except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response_patch,http_err)

except requests.exceptions.RequestException as err:
    request_exception_error(err)

# ===============Delete Method ===================
global response_delete
try:
    response_delete = requests.delete(url)
    print(f"response code of the method is {response_delete.status_code}")
    print(response_delete.json())
except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response_delete,http_err)

except requests.exceptions.RequestException as err:
    request_exception_error(err)
