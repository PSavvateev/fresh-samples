import requests
import json
from freshlogin import domain, api_key, password

# Create a Company
# curl -vu api_key:x -H "Content-Type: application/json" -X POST -d '{ "name":"SuperNova", "description":"Spaceship Manufacturing Company", "note" : "Regular customer" }' 'https://domain.freshdesk.com/api/v2/companies'

company_info = { "name" : "SuperNova", "description" : "Spaceship Manufacturing Company", "note" : "Regular customer" }
headers = { "Content-Type" : "application/json" }

r = requests.post("https://{0}.freshdesk.com/api/v2/companies".format(domain), auth = (api_key, password), data = json.dumps(company_info), headers = headers)

if r.status_code == 201:
  print ("Companies created successfully, the response is given below")
else:
  print ("Failed to create companies, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())