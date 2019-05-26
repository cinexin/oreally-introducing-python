count = 1
while (count <=10):
    print(count)
    count+=1

while True:
    stuff = input("String to capitalize [type 'q' to quit]: ")    
    if (stuff == 'q'):
        break
    else:
        print(stuff.capitalize())

while True:
    value = input("Integer, please ['q' to quit]: ")
    if (value == 'q'):
        break
    else:
        number = int(value)
        if (number % 2 == 0):
            continue
        else:
            print(number, "squared is:", number**2)

numbers = [1,3,5]
position = 0
while (position < len(numbers)):
    number = numbers[position]
    if (number % 2 == 0):
        print('Found an even number:',number)
        break
    position +=1
else: #break NOT CALLED
    print("No even number found")

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}    
for card, clue in accusation.items():
    print(card,":",clue)

cheeses = []
for cheese in cheeses:
    print("This shop has some lovely",cheese)
    break
else:
    print("Shitty no-cheese shop!")

# THE "ZIP"
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day,": drink", drink, "-eat", fruit, "-enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
list(zip(english, french))
dict(zip(english, french))

# RANGE
for x in range(0,3):
    print(x)

for x in range(2,-1,-1):
    print(x)

# LIST COMPREHENSIONS
number_list = list(range(1,6))
number_list = [number for number in range(1,6)]
odd_number_list = [number for number in range(1,6) if number % 2 == 1]

# NESTED LOOPS
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

cells = [(row, col) for row in rows for col in cols]
for cell in cells: 
    print(cell)

# DICTIONARY COMPREHENSIONS
word='letters'
letter_counts = {letter: word.count(letter) for letter in word}

# SET COMPREHENSIONS
a_set = {number for number in range(1,6) if number %3 == 1}
