# example of range 0 -100
print(range(100))  # prints range (0,100)

# prints each number in range
my_list = list(range(10))
print(range)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))
print(even)  # [0,2,4,6,8]
print(odd)  # [1,3,5,7,9]

# .index() and indexing a string
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

# indexing from ranges ex1
small_decimals = range(0, 10)
print(small_decimals)  # prints range(0,10)
print(small_decimals.index(3))

# indexing from ranges ex2
odder = range(1, 10000, 2)
print(odder)  # prints range(0,10000,2)
print(odder[985])  # prints the 985th odd number 1971

# example with conditionals
seven = range(7, 1000000, 7)
x = int(input("Please enter a number divisable by seven: "))
if x in seven:
    print("{} is divisable by seven".format(x))
else:
    print("{} is not diviable by seven".format(x))

# copying ranges
my_range_copy = small_decimals[::2]
print(my_range_copy)  # prints range(0,10,2)
print(my_range_copy.index(4))  # prints 2 (Have no idea why :( )

# copy ranges example 2

decimals = range(0, 100)
print(decimals)

my_range_decimals = decimals[3:40:3]
print(my_range_decimals)

for i in my_range_decimals:
    print(i, end=" ")

print("*" * 40)

print(my_range_decimals == range(3, 40, 3)) # returns true
