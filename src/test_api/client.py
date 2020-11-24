import requests

url = r"http://127.0.0.1:5000/check_statement"

data = {"sentence": "ana are mere"}
r = requests.post(url, json=data, headers={'AuthorizationToken': 'xy124zjw3'})

print(r.text)