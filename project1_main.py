import secrets
import string 


def registration():
    while True : 
        phone_number = input("Phone number: ")
        try: 
            
            if not phone_number.isdigit():
                raise ValueError("incorrect input format!")

            if  len(str(phone_number)) != 10 : 
             raise ValueError("Enter Valid phone number")
 
            print("Your phone number is: ",phone_number) 
            break 
    
        except ValueError as e : 
          print(f"Error : {e}, please try again!")


def password_generator():
   
   random_words = string.ascii_letters + string.digits + string.punctuation


   password_length = 16 


   password = "".join(secrets.choice(random_words) for _ in range (password_length)) 

   print(password,"is your generated password.")




def manual_password():
   
   upper_letters = string.ascii_uppercase
   symbols = string.punctuation
   numbers = string.digits 

 
   
   while True : 
    input_password = input("Enter your password: ").strip()
    contains_upper_letters = any(char in upper_letters for char in input_password)
    contains_symbols = any(char in symbols for char in input_password)
    contains_numbers = any(char in numbers for char in input_password)

    if (contains_numbers and contains_symbols and contains_upper_letters) :
        print(input_password,"is the password you created") 
        break 

    else : 
      print("Try different combination!")
        


def main():
  
   registration()

   
   user_input = input('press y to generate password and n to enter password manually y/n : ').strip().lower()


   if user_input not in ['y','n']: 
    print(f"{user_input} command not found!")
    
   elif user_input == 'y':
    password_generator()
       
     
   elif user_input == 'n':
    manual_password()
    
   else : 
    pass 



main()
    

    
    
    
    
    
     
 


    
   
          
    
       
       
     
    
   

  

            
            


   
   
      
      

   