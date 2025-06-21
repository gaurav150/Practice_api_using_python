
def https_catch_errors(response,http_err) ->None:
    if 400 <= response.status_code < 500:
        print(f"⚠️ Client error (4xx): {response.status_code}")
        print("Details:", response.text)
    elif 500 <= response.status_code < 600:
        print(f"🔥 Server error (5xx): {response.status_code}")
        print("Details:", response.text)
    else:
        print(f"❌ Other HTTP error occurred: {http_err}")

def request_exception_error(err) ->None:
    print("❌ Request failed:", err)