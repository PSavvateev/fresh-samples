import requests
import json
from freshlogin import domain, api_key, password

# Return the tickets that are new or opend & assigned to you
# If you want to fetch all tickets remove the filter query param
r = requests.get("https://{0}.freshdesk.com/api/v2/tickets?filter=new_and_my_open".format(domain), auth = (api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below")
else:
  print ("Failed to read ticket, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
