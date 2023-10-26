from pprint import pprint

import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url=url)

result = response.json()
pprint(result)
astros = result['people']

for person in astros:
    pprint(person['name'])
