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

        number_list = []
        for value in self.contacts.values():
            number_list.append(value["number"])
        if not self.number  in number_list:
             self.contacts[self.name] = {"number": self.number, "email":self.email, "address":self.address}
             self.save_to_json()
        else:
            print("Number already exists! ")

    

      
    def save_to_json(self):
             with open(self.jsonfile, "w") as file:
                json.dump(self.contacts, file, indent=3)
                
        

           
       


    def delete_from_json(self,name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_to_json()
            print("contact Deleted")

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
                 

    def edit_contact(self):
        pass
         