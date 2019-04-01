# Two ways of creating lists

list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")

# reformats String into a char list
print(list("The lists are equal"))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
another_even = even

# difference between == and is
print(another_even is even)  # false
print(another_even == even)  # true

# sorts and reverses order of even (2 ways)
# another_even.sort(reverse=True)
another_even.sort(reverse=True)

print(even)

# Lists of Lists
numbers = [even, odd]
print(numbers)

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value, end=" ")
