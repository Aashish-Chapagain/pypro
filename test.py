import secrets
import string
import json
import os 

ACCOUNTNUMBERLENGTH = 13


numbers = string.digits 



class Bank_management(): 

    customer_number = 0 
    customer_dict = {}
    

    def __init__(self, name, account_number, balance):

        self.name = name 
        self.account_number = account_number 
        self.balance = balance 
    
    @classmethod
    def create_new_account(cls):
        while True : 
         try : 
          name = (input("Enter Your full name: ")).capitalize().strip()
          new_name = name.replace(" ","")
          deposit_amount = float(input("Enter the first deposit amount: "))
          account_number = "".join(secrets.choice(numbers) for _ in range(ACCOUNTNUMBERLENGTH))
          if deposit_amount < 1 : 
             raise ValueError("Deposit amount cannot be less than 1$")
          
          if not new_name.isalpha():
             raise ValueError("Invalid input! try again") 
          

         
          break 
       

         except ValueError as e : 
            print(e)
         
         return cls(name,new_name,account_number)
        

        
         
     
    def display(self): 
       print(self.name, self.account_number, self.balance, end = '\n')





        
person1 = Bank_management.create_new_account()
person1.display()
    



    


