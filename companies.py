import requests
import json
from freshlogin import domain, api_key, password

class Companies:
    id = input('ID компании: ')
    name = input('Имя огранизации: ')
    description = input('Описание организации: ')
    note = input('Заметка: ')
    info = { "name" : name, "description" : description, "note" : note }
    headers = { "Content-Type" : "application/json" }

    def get():
        r = requests.get("{0}companies".format(domain), auth = (api_key, password))

        companies = r.json()

        for item in companies:
            print(item['id'], item['name'], item['description'], item['note'])

    def create():
        r = requests.post("{0}companies".format(domain), auth = (api_key, password), data = json.dumps(Companies.info), headers = Companies.headers)

    def updated():
        r = requests.put("{0}companies/{1}".format(domain, Companies.id), auth = (api_key, password), data = json.dumps(Companies.info), headers = Companies.headers)