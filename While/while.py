import random

# Guessing Game

highest = 10
answer = random.randint(1,highest)
print("Please Guess a number between 1 - {} exclusive: ".format(highest))
guess = int(input())

while guess != answer:
    if guess < answer:
        print("Guess higher: ")
    else:
        print("Guess Lower: ")
    guess = int(input())

print("BITCH you Guessed it!!!!!!!....WOOAH....You is right.")

# Basic example
i = 0
while i < 10:
    print("i is now {}".format(i))
    i +=1


# More common Example
available_exits = ["east","north east","south"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game over!")
        break

print("Aren't you glad you got out of there?")



