import requests
import json
from freshlogin import domain, api_key, password

# Id of the ticket to be updated
ticket_id = '2'

headers = { 'Content-Type' : 'application/json' }

ticket = {
  'subject' : 'Updated Title',
  'description' : 'Updated description Python 3.5.2',
  'priority' : 3,
}

r = requests.put("https://{0}.freshdesk.com/api/v2/tickets/{1}".format(domain, ticket_id), auth = (api_key, password), headers = headers, data = json.dumps(ticket))

if r.status_code == 200:
  print ("Ticket updated successfully, the response is given below")
else:
  print ("Failed to update ticket, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
