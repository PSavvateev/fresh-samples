import requests
import json
from freshlogin import domain, api_key, password

multipart_data = [
    ('email', ('','example@example.com')),
    ('subject', ('', 'Ticket Title')),
    ('status', ('', '2')),
    ('priority', ('', '2')),
    ('cc_emails[]', ('', 'sample_email@domain.com')),
    ('cc_emails[]', ('', 'user_email@domain.com')),
    ('attachments[]', ('logo.png', open('logo.png', 'rb'), 'image/png')),
    ('attachments[]', ('create_ticket_attachment.py', open('create_ticket_attachment.py', 'rb'), 'text/plain')),
    ('description', ('', 'Ticket description.'))
]

r = requests.post("https://{0}.freshdesk.com/api/v2/tickets".format(domain), auth = (api_key, password), files = multipart_data)

if r.status_code == 201:
  print ("Ticket created successfully, the response is given below")
else:
  print ("Failed to create ticket, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

t = r.json()
print(r.json())
