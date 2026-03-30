import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" # http://localhost:8000/api/

get_response = requests.get(endpoint, json={"product_id": 123}) # HTTP request
# print(get_response.headers) # print the response headers
# print(get_response.text) # print the raw response text
# print(get_response.status_code)


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation (JSON) -> Python Dictionary
print(get_response.json()) # print the response as a Python dictionary
# print(get_response.status_code) # print the HTTP status code of the response