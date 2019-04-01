age = int(input("How old are you?: "))

# age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# Note: In python true and false evaluates to 0 and 1. All non zero and
# non empty values will evaluate to false

# FALSE VALUES
print("""False: {}
None: {}
0: {}
0.0: {}
empty list []: {}
empty tuple (): {}
empty String'': {}
empty String"": {}
empty mapping {{}}: {}
""".format(False, bool(None), bool(0), bool(0.0),
           bool([]), bool(()), bool(''), bool(""), bool({})))

# Example of empty input
x = input("Please enter some text ")
if x:
    print("You entered {}".format(x))
else:
    print("You didn't enter anything")


# Using not

age = int(input("How old are you?"))
if not(age < 18):
    print("Please vote.")
else:
    print("Please come back in {0} years".format(18 - age))


# Check character in string

parrot = "Norweigian Blue"
letter = input("Enter a character: ")
if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Bob".format(letter))