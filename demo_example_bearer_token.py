import requests

# Step 1: Login endpoint
login_url = "https://reqres.in/api/login"
login_payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

# Include your API key in the headers
api_key = "reqres-free-v1"
headers_with_key = {
    "x-api-key": api_key
}

# Send login POST request
login_response = requests.post(login_url, json=login_payload, headers=headers_with_key)

print("Login Response Status Code:", login_response.status_code)
print("Login Response Body:", login_response.text)

# Step 2: Check if login is successful and extract token
if login_response.status_code == 200:
    token = login_response.json().get("token")
    print(f"\n✅ Logged in successfully! Token: {token}")

    # Step 3: Simulate protected API call using Bearer Token
    protected_url = "https://reqres.in/api/users/2"
    headers_with_token = {
        "Authorization": f"Bearer {token}",
        "x-api-key": api_key  # still include the API key
    }

    print(" Sending token in headers...")
    print("Sent Headers:", headers_with_token)

    # Send GET request with Authorization + API key
    protected_response = requests.get(protected_url, headers=headers_with_token)

    # Output response
    print("\nProtected Endpoint Status Code:", protected_response.status_code)
    print("Protected Endpoint Response JSON:")
    print(protected_response.json())

else:
    print("\n❌ Login failed. Please check email/password or API key.")
