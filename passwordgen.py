import secrets    
import string 

def generate_password(password_length  = 16 ): 
   


    password = string.ascii_letters + string.digits + string.punctuation
    
    

   
    password_ = ''.join(secrets.choice(password)  for _ in range(password_length))

    print(password_) 




while True :
 user_input = input('press y to generate password and n to exit y/n : ').strip().lower()


 if user_input not in ['y','n']: 
    print(f"{user_input} command not found!")
 elif user_input == 'y':
   generate_password()
 else : 
    print("Exiting program")
    break 
 
    



    
