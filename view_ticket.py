import requests
import json
from freshlogin import domain, api_key, password

# You can use a ticket 2
ticket_id = input('Enter ticket ID for viewing: ')

r = requests.get("https://{0}.freshdesk.com/api/v2/tickets/{1}".format(domain, ticket_id), auth = (api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below")
else:
  print ("Failed to read ticket, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

# t = r.json()
print(r.json())