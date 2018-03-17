import requests
import json
from freshlogin import domain, api_key, password

# Update a Company
# curl -vu api_key:x -H "Content-Type: application/json" -X PUT -d '{ "name" : "Super Nova", "description" : "Space Shuttle Manufacturing" }' 'https://domain.freshdesk.com/api/v2/companies/36000214007'

company_id = '36000214007'

company_info = { "name" : "Super Nova", "description" : "Space Shuttle Manufacturing" }
headers = { "Content-Type" : "application/json" }

r = requests.put("https://{0}.freshdesk.com/api/v2/companies/{1}".format(domain, company_id), auth = (api_key, password), data = json.dumps(company_info), headers = headers)

if r.status_code == 200:
  print ("Company updated successfully, the response is given below")
else:
  print ("Failed to update company, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
