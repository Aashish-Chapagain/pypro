import string 
import getpass 
def player_vs_player():
 print("Snake-Water-Gun the game ")
 print("""Description:
 s for snake, w for water and g for gun! """)
# asking the user, for how many rounds they want to play 
 rounds = int(input("How many rounds you want to play: "))
 if rounds > 15 or rounds < 1:
   print(" Please enter the value between 0 and 16 ")
 else :
    # list of elements 
  li_of_elements = ["s","w","g"]
#counting points and rounds 
  print("Total chance:",rounds)
# taking name of the user and starting to count the rounds points 
  user1_name = str(input("Enter name of the first player: "))
  user2_name = str(input("Enter the name of second player: "))
  user1_points = 0
  user2_points = 0
# taking inputs from the users and varifying the input
#for user1
  while rounds != 0 : 
    print("snake,water,gun:")
    print(f"choose from snake , water and gun \'Remeber s for snake, w for water and g for gun\' {user1_name}: ", end='')
    gamer1 = str(input())
    if gamer1 in li_of_elements:
       gamer1.lower()
    else: 
       print("please enter the value \"s or w or g\" : " )
       gamer1 = str(input())
    #for user2
    print(f"choose from snake , water and gun \'Remeber s for snake, w for water and g for gun\' {user2_name}: ", end='')
    gamer2 = str(input())
    if gamer1 in li_of_elements:
     gamer1.lower()
    else: 
        print("please the the value \"s or w or g\" :")
        gamer2 = str(input())
#checking the condition to determine the winner and the loser 
    print(f"The chosen word by {user1_name} is : ",str(gamer1))
    print(f"The chosen word by {user2_name} is : ",str(gamer2))
    if (gamer1 == "s" and gamer2 == "w") or (gamer1 == "w" and gamer2=="g" ) or (gamer1 == "g" and gamer2 == "s"):
        user1_points += 1 
        print("\n \tThe winner for this round is: ",user1_name)
    elif (gamer1 == gamer2):
        print("\n \tThe round is draw")
    else : 
        print("\n \tThe winner for this round is: ",user2_name)
        user2_points += 1 
    rounds -= 1 
    print ("\n Rounds remaining ", rounds)
    print(f" \n current point of {user1_name} is:", user1_points)
    print(f"\n current point of {user2_name} is:", user2_points)

 if user1_points > user2_points :
    print(f"The winner is {user1_name} with {user1_points} points")
 elif user1_points == user2_points: 
  print("The match is darw")
 else:
    print(f"The winner is {user2_name} with {user2_points} points")
player_vs_player()  
                           

    


    

    

    

 