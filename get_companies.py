import requests
import json
from freshlogin import domain, api_key, password

# List All Companies
# curl -vu api_key:x -X GET 'https://domain.freshdesk.com/api/v2/companies'

r = requests.get("{0}companies".format(domain), auth = (api_key, password))

companies = r.json()

for item in companies:
  print(item['id'], item['name'], item['description'], item['note'])