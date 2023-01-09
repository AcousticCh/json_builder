import requests
import json

endpoint_root = "http://127.0.0.1:8000/"
endpoint_add_json = "http://127.0.0.1:8000/add_json"
body = { "accounts": {"6": {
    "index": 0,
    "website": "blubber",
    "email": "hassenr@fil.com",
    "username": "acousticCh",
    "password": "peantac", 
    }}}

response = requests.post(endpoint_add_json, json=body)
# response = requests.get(endpoint_root)

print(response.json())

# with open("db.json", "r") as file:
#     data = json.load(file)
#     data.update(dict(response.json()))

# with open("accounts_db.json", "w") as file:
#     json.dump(data, file)