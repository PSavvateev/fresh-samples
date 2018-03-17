import requests
import json
from freshlogin import domain, api_key, password

headers = { 'Content-Type' : 'application/json' }

ticket = {
    'subject' : 'Ticket title',
    'description' : 'Ticket detail',
    'email' : 'example@example.com',
    'priority' : 1,
    'status' : 2,
    'cc_emails' : ['sample_email@domain.com', 'user_email@domain.com']
}

r = requests.post("https://{0}.freshdesk.com/api/v2/tickets".format(domain), auth = (api_key, password), headers = headers, data = json.dumps(ticket))

if r.status_code == 201:
  print ("Ticket created successfully, the response is given below")
else:
  print ("Failed to create ticket, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
