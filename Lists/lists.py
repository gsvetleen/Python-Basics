# Sequence types - Lists, tuple, range

# lib method .count()
ipAddress = input("Please input IP Address: ")
print(ipAddress.count("."))  # returns number of . in String

parrot_lists = ["non_pinin", "no more", "a stiff", "berefit of life"]

# Adding to the String
parrot_lists.append("A Norwegian Blue")
for state in parrot_lists:
    print("The parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd

# two ways to sort numbers
numbers_in_order = sorted(numbers)
if numbers == numbers_in_order:
    print("The Lists are equal")
else:
    print("The numbers are not sorted!")

numbers.sort()

if numbers == numbers_in_order:
    print("The Lists are equal")
else:
    print("The numbers are not sorted!")
