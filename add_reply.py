import requests
import json
from freshlogin import domain, api_key, password

# id of the ticket to add a note
ticket_id = '2'

headers = { 'Content-Type' : 'application/json' }

note = {
  'body' : 'Sample reply'
}

r = requests.post("https://{0}.freshdesk.com/api/v2/tickets/{1}/reply".format(domain, ticket_id), auth = (api_key, password), headers = headers, data = json.dumps(note))

if r.status_code == 201:
  print ("Reply added successfully, the response is given below")
else:
  print ("Failed to add reply, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
