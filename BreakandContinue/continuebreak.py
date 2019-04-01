shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# Example continue
for item in shopping_list:
    if item == 'spam':
        continue
    print("Buy " + item)

# Example break
for item in shopping_list:
    if item == 'spam':
        break
    print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
    else:
        print("I'll have some please")

if nasty_food_item:
    print("Can't I have anything without spam in it?")

# Augmented Assignment less work, more efficient

number = "567,887,646,467"
cleanedNumner =''

for i in range (0,len(number)):
    if number[i] in '0123456789':
        cleanedNumner += number[i]

newNumber = int(cleanedNumner)
print("The number is {}".format(newNumber))