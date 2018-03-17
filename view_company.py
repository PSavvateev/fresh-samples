import requests
import json
from freshlogin import domain, api_key, password

# View a Company
# curl -vu api_key:x -X GET 'https://domain.freshdesk.com/api/v2/companies/36000214007'

company_id = '36000214007'

r = requests.get("https://{0}.freshdesk.com/api/v2/companies/{1}".format(domain, company_id), auth = (api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below")
else:
  print ("Failed to read companies, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
