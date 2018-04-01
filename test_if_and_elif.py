import requests
import json
from freshlogin import domain, api_key, password

a = int(input('''1: View Ticket\n
2: View Company\n
Enter: '''))

if a == 1:
   ticket = int(input('Enter Ticket: '))
   r = requests.get("https://{0}.freshdesk.com/api/v2/tickets/{1}".format(domain, ticket), auth = (api_key, password))
   print(r.json())
elif a == 2:
    company = int(input('Enter Company: ')) 
    r = requests.get("https://{0}.freshdesk.com/api/v2/companies/{1}".format(domain, company), auth = (api_key, password))
    print(r.json())