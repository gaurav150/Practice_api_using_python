import requests
from marshmallow import Schema, fields, ValidationError, EXCLUDE
from common_utils.common_methods import https_catch_errors, request_exception_error

# ✅ Define schema with class Meta
class PostResponseSchema(Schema):
    title = fields.String(required=True)
    body = fields.String(required=True)
    userId = fields.Integer(required=True)
    id = fields.Integer(required=True)

    class Meta:
        unknown = EXCLUDE  # Ignore any unexpected fields in response

url = "https://jsonplaceholder.typicode.com/posts"
data_sending = {
    "title": "First_Try",
    "body": "This is My first Try",
    "userId": 1
}

response_post = requests.post(url=url, json=data_sending)

try:
    print(response_post.content)

    if response_post.status_code == 201:
        print("Success")
        response_data = response_post.json()
        print(response_data)

        # ✅ Validate response using schema with class Meta
        schema = PostResponseSchema()
        validated_data = schema.load(response_data)
        print("Schema validation passed ✅")
        print(validated_data)

    else:
        print("Request failed ❌")

except ValidationError as val_err:
    print("Schema validation failed ❌")
    print(val_err.messages)

except requests.exceptions.HTTPError as http_err:
    https_catch_errors(response_post, http_err)

except requests.exceptions.RequestException as err:
    request_exception_error(err)
