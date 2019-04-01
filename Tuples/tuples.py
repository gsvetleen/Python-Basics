# tuples are an ordered set of data
# Similar to lists except that they're immutable
# example 1
t = "a", "b", "c"
print("a", "b", "c")
print(("a", "b", "c"))
# example 2
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# cannot do this -> metallica[0] = "Something here", tuples are immmutable
# However, can change the variable object inside the tuple
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

# NOTE -> Seperate form tuples
a = b = c = d = 12
print(c)
a, b = 12, 13
print(a, b)
a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))


# Unpacking the tuple example
title, artist, year = imelda
print(title)
print(artist)
print(year)

