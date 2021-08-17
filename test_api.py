import requests
import json
response_API = requests.get('http://127.0.0.1:8000')
data = response_API.text
parse_json = json.loads(data)
print(parse_json)