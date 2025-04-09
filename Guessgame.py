import random
import math
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
x = random.randint(lower, upper)
chances = round(math.log(upper - lower + 1, 2))
print(f"\n\tYou have {chances} chances to guess the number!\n")
count = 0
while count < chances:
    count += 1
    guess = int(input(f"Guess {count}: Enter your number: "))
    if guess == x:
        print("\n🎉 Correct! You guessed the number!")
        break
    elif guess < x:
        print("Too low!")
    else:
        print("Too high!")
if guess != x:
    print(f"\n😢 Oops! You couldn't guess the number.")
    print(f"The correct number was: {x}")
