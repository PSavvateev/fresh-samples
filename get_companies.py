import requests
import json
from freshlogin import domain, api_key, password

# List All Companies
# curl -vu api_key:x -X GET 'https://domain.freshdesk.com/api/v2/companies'

r = requests.get("https://{0}.freshdesk.com/api/v2/companies".format(domain), auth = (api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below")
else:
  print ("Failed to read ticket, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

companies = r.json()

for item in companies:
  print(item['id'], item['name'], item['description'], item['note'])