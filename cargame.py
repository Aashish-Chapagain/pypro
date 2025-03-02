
def menu():
    return("start\ndrive\nstop\nexit")

def start():
    print("The car is started.")

def driving():
   print("The car is driving.")

def stop():
    print("The car is stopped.") 




print("help\nstart\ndrive\nstop\nexit")


menu_list = ["help","start","drive","stop","exit"]


is_started = False 


while True :
    user_input = str(input("Enter the option: ")).strip().lower()
        

    if  user_input == "help" : 
           print(menu()) 

    elif user_input=="start" : 
        if is_started :
            print("The car is already started.")
        else :
            start()
            is_started = True  

    elif user_input == "stop" :
        if is_started : 
            stop()
            is_started = False
        else :
            print("The car is already stopped.")
    
    elif user_input == "exit" :
        break 
    
    else : 
          print("Command not found!\nTry: ") 
          
          print(menu())  


        
