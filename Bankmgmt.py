class Bank : # defining the class Bank 

    _customer = 0 #this is class variable which can be accesed by and object or instance for this class 

    def __init__(self,name,account_number,balance):  #constructor or attributes of the calss Bank where self is the instance of every object in this class

        self.name= name 
        self.account_number = account_number
        self.balance = balance 
        Bank._customer += 1 # _costumer is increamented every time the constructor is called 
    

    def display(self):  # method to display object 
        print(f"""name: {self.name}
account number: {self.account_number}
balance: $ {self.balance} \n""")
        



user1 = Bank("sponge bob",103299233022,40000 )    # creating object 
user2 = Bank("patrick", 103872873890, 55000)  # creating object 
user3 = Bank("squidward", 103879379390, 65000)  # creating object 
user4 = Bank("mr carbs", 103873422340, 650000)  # creating object 

user1.display()   # using display method to print the object into the console 
user2.display() # using display method to print the object into the console 
user3.display() # using display method to print the object into the console 
user4.display() # using display method to print the object into the console 


print(f"The number of customers is: ", Bank._customer)  # printing the calss variable to the console 


print(user1.name)  
print(user2.name)  
print(user3.name)  
print(user4.name)  

