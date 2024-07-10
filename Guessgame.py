import random
import math
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
x = random.randint(lower, upper)
chances = round(math.log(upper-lower + 1, 2))
print("\n\t Total chances you get is ", chances )
count = 0
while count < chances:
    count += 1 
    a = int(input(" \n Enter your guess: "))
    if a == x:
        print("correct ")
     
    elif a<x:
        print("not correct too low ")
    else:
        print("not correct too high")
if count <= chances and x != a  :
    print(f"\n \t The random number is {x}")
    print("\n \t Oh no! You could not guess it ")
     

