class Contact():

    contact_value_dict = {}
    
    def __init__(self,name,number):
        self.name = name 
        self.number = number 

    @classmethod

    def save(cls):
        name = input("enter full name:  ")
        number = int(input("Enter the number: ")) 
        return cls(name,number)
    


contact = Contact.save()

print(contact.name, contact.number)


        