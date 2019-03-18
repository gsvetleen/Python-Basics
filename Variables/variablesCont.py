parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
# starts at 0 minus number of steps from last character
print(parrot[-1])
# print characters in a range
print(parrot[0:6])
# Same as previous
print(parrot[:6])
# starting point all the way to the end of String
print(parrot[6:])
# You get the idea
print(parrot[-4:-2])
# 0 - 6 index in increments of 2
print(parrot[0:6:2])
# 0 -6 index in increments of 3
print(parrot[0:6:3])

# concatenate Strings
string1 = "he's "
string2 = "probably "
print(string1 + string2)

# print string number of times
print("Hello " * 5)

# check if substring is in string

today = "friday"
print("day" in today) #true
print("fri" in today) #true
print("thurs" in today) #false
print("parrot" in "faulkner") #false\

#Note: Numbers cannot be concatenated with strings in python.     