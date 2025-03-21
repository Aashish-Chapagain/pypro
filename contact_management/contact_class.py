import json 
import os 


class Contacts: 
    def __init__(self):
        self.contacts = {}
        self.jsonfile = "contacts.json"
        

        if os.path.exists(self.jsonfile): 
           with open(self.jsonfile, "r") as file :
              try : 
                 self.contacts = json.load(file)
              except json.JSONDecodeError:
                 self.contacts = {}
                 
    

    def save_contact(self, name , number , email, address):
        self.name = name
        self.number = number 
        self.email = email 
        self.address  = address 
        
       
        self.contacts[name] = {"number":number , "email": email, "address": address }

    
    def save_to_json(self): 
         with open(self.jsonfile, "w" ) as file : 
            json.dump(self.contacts, file, indent = 3 )
    
    def delete_from_json(self,name):
        if name in self.contacts: 
            del self.contacts[name]
            self.save_to_json()
           
            
