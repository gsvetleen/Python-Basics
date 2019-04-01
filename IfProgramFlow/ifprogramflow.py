# name = input("Please enter your name: ")
# # type casting input return value;
# age = (int)input("How old are you, {0}? ".format(name))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0} years".format(18 -age))


print("Please guess a number between one and 10: ")
guess = int(input())
if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it right the first time")