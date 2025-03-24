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

      
    def save_to_json(self):
        number_list = []
        for value in self.contacts.values():
            number_list.append(value["number"])
        print(number_list, self.number)
        if not self.number  in number_list:
             self.contacts[self.name] = {"number": self.number, "email":self.email, "address":self.address}

             with open(self.jsonfile, "w") as file:
                json.dump(self.contacts, file, indent=3)
           
        else:
            print("Number already exists! ")


    def delete_from_json(self,name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_to_json()

    def search_contact(self, name):
        is_avail  = True 
        for key, values in self.contacts.items():
            if name != key :
                 
                 continue 
            else : 
                 print(key,values)
                 is_avail = False
                 
        if  is_avail:
            print("No mathches found!")
                 
         