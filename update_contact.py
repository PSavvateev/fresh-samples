import requests
import json
from freshlogin import domain, api_key, password

# Id of the contact to be updated
contact_id = '36005577380'

contact_info = { "priority" : "Super Hero" }
headers = { "Content-Type" : "application/json" }

r = requests.put("https://{0}.freshdesk.com/api/v2/contacts/{1}".format(domain, contact_id), auth = (api_key, password), data = json.dumps(contact_info), headers = headers)

if r.status_code == 200:
  print ("Contact updated successfully, the response is given below")
else:
  print ("Failed to update contact, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
