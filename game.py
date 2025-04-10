import random

print("\n\tWelcome to Snake-Water-Gun Game!")
print("""
How would you like to play?
a) Computer vs Player (chances are random)
b) Player vs Player (chances are not random)
""")

# Taking input from the user
selection = input('Press "a" for option a or press "b" for option b: ')
selection = selection.lower()

# Option a: Player vs Computer
if selection == "a":
    player1 = input("Enter the name of the player: ")
    chances_random = random.randint(3, 10)
    print("Total chances you get:", chances_random)

    choices = ['s', 'w', 'g']
    user_pts = 0
    computer_pts = 0

    while chances_random > 0:
        user_choice = input('Enter your choice ("s" for Snake, "w" for Water, "g" for Gun): ').lower()
        if user_choice not in choices:
            print("Invalid choice! Please enter s, w, or g.")
            continue

        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")

        if (comp_choice == "s" and user_choice == "w") or \
           (comp_choice == "w" and user_choice == "g") or \
           (comp_choice == "g" and user_choice == "s"):
            computer_pts += 1
            print("Computer wins this round.")
        elif comp_choice == user_choice:
            print("This round is a draw.")
        else:
            user_pts += 1
            print(f"{player1} wins this round.")

        print(f"Score => {player1}: {user_pts}, Computer: {computer_pts}")
        chances_random -= 1
        print(f"Remaining chances: {chances_random}\n")

    print("\n🎉 Final Result 🎉")
    if user_pts > computer_pts:
        print(f"The winner is {player1} with {user_pts} points!")
    elif user_pts == computer_pts:
        print(f"The game is a draw! Both scored {user_pts} points.")
    else:
        print(f"The winner is Computer with {computer_pts} points!")

elif selection == "b":
    print("Player vs Player mode is under development. Stay tuned!")

else:
    print("Invalid option selected.")
