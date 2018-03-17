import requests
import json
from freshlogin import domain, api_key, password

contact_info = { "name" : "Example User", "email" : "api_v2_user_03@example.com" }
headers = { "Content-Type" : "application/json" }

r = requests.post("https://{0}.freshdesk.com/api/v2/contacts".format(domain), auth = (api_key, password), data = json.dumps(contact_info), headers = headers)

if r.status_code == 201:
  print ("Contact created successfully, the response is given below")
else:
  print ("Failed to create contact, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
