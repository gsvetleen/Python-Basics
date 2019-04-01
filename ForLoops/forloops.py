for i in range(1, 20):
    print("i is now {}".format(i))

# prints numbers and commas
number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    print(number[i])

# prints only numbers
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')

# concatenating numbers
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))
