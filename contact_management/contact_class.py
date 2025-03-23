import json
import os


class Contacts:
    def __init__(self):
        self.contacts = {}
        self.jsonfile = "contacts.json"

        if os.path.exists(self.jsonfile):
            with open(self.jsonfile, "r") as file:
                try:
                    self.contacts = json.load(file)
                except json.JSONDecodeError:
                    self.contacts = {}

    def save_contact(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address

        self.contacts[name] = {"number": number, "email": email, "address": address}

    def save_to_json(self):
        number_list = []
        for value in self.contacts.values():
            number_list.append(value["number"])
        if not self.number in number_list:
            with open(self.jsonfile, "w") as file:
                json.dump(self.contacts, file, indent=3)

        else:
            print("Number already exists! ")

    def delete_from_json(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_to_json()

    def search_contact(self, name):
        list_of_name = []
        for key, values in self.contacts.items():
            list_of_name.append(key)
            if name != key :
                 continue 
            else : 
                 print(key,values)
        if name not in list_of_name: 
            print("No mathches found!")
                 
            

            
            