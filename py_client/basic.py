import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint, json={"title" : "ABC 123","content": "Hello World", "price" : "abc123"})  # HTTP Request
# print(get_response.text)
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dictionary

print(get_response.json())
# print(get_response.status_code)
