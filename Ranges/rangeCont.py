# returns true, same sequence
print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = range(0, 100)
print(r)

for i in r[::-2]:  # prints backwards 99-0
    print(i, end=" ")

# same as above

for i in range(99,0,-2):
    print(i, end=" ")


# reverse a string
backstring = "eguagnal lufrewop yrev a si nohtyP"
print(backstring[::-1])

