# Iterators are objects that represent a stream of data.

string = "123456789"

# what happens here is that an iterator is created to iterate through the string
# when there are no more items the iterator returns an error and the for loop terminates
for char in string:
    print(char, end=" ")


my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# same thing as above
for char in iter(string):
    print(char,end=" ")

