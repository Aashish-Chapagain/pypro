#importing class
from new_bank import Contacts 

_contacts = Contacts() #instance of the class for every object like a variable to store the copy of class for every object 


def command(): 
   return("""Enter (save) to save new contact
Enter (exit) to exit program
Enter (search) to search in contacts 
Enter (delete) to delect the contacts """)

#function to create new contact 
def save_new_contact():
    while True :
         try :
  
          name = input("First and Last name : ")
          number = int(input("Enter the phone number: "))       
          address = input("Enter address: ")
          email  = input("Enter email: ")
          
         except ValueError: 
            print("Something didnot worked! Try again")
            continue 
         
         _contacts.save_contact(name,number,email,address)
         _contacts.save_to_json()


#function to delete a contact 
def delete_a_contact(): 
    
      name  = input("Enter the contact name you want to delete: ")
      _contacts.delete_from_json(name)


list_of_commands = ["save", "exit", "search", "delete"]


print(command())
while True : 
   
    user = input("Enter the command: ").strip().lower()
    if user not in list_of_commands:
       print(f"command not found! Try again with \n{command()}")
    
    elif user == "save" : 
         save_new_contact()
       

         choice = input("Do you want to create new contact ? y/n: ").strip().lower()
         if choice != "y": 
            break 

    elif user == 'exit': 
       print("exiting program")
       break
    

    elif user == "delete" : 
       delete_a_contact()


