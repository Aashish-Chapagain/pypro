import random 
import string 
print("\n \tWelcome to snake water gun game")
print("""\n How would You like to play
      a) computer vs Player(chances are random)
      b) player vs player(chances are not random)""")

# taking input from the user

selection = input("press \"a\" for option a or press \'b\' for option b  ")
selection.lower()

#checking where user want to play vs computer or vs player

if selection == "a":
    player1 = str(input("Enter the name of the player: "))
    chances_random = random.randint(3,10)
    print("Total chances you get is: ", chances_random)
    li_elements= ['s','g','w']
    user_pts = 0
    computer_pts = 0
    while chances_random > 0:
      user_choice = str(input("Enter your choice \"s for snake\" \"w for water\" \"g for gun\" : "))
      user_choice.lower()
      random_choice = random.choice(li_elements)
      print("Computer: ",random_choice)
      if  (random_choice == "s" and user_choice == "w") or (random_choice == "w" and user_choice=="g" ) or (random_choice == "g" and user_choice == "s"):
         computer_pts += 1 
         print("point ", computer_pts)
         print("The winner of the round is Computer")
      elif random_choice==user_choice :
         print("This round is draw ")
      else :
         print("The winner of this round is: ",player1 )
         user_pts += 1 
         print("point ", user_pts)
      chances_random -= 1 
      print("Remaining chances: ", chances_random)
if user_pts > computer_pts : 
      print(f"The winner is {player1} with {user_pts} points")
elif user_pts == computer_pts : 
      print(f"The game is draw computer points is {computer_pts} and {player1} is {user_pts}")
else: 
      print(f"The winner is computer with {computer_pts} points")
   