marxes = ['Groucho','Chico','Harpo','Zeppo']
marxes.index('Chico')
words = ['a','deer','a','female','deer']
friends = ['Harry', 'Hermione', 'Ron']
numbers = [2,1,4.0,3]
marx_tuple = 'Groucho', 'Chico', 'Harpo'
bierce_dictionary = {
    "day": "A period of 24h, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind fo fortune that never misses"
}
lol = [['a','b'],['c','d'], ['e','f']]
pythons = {
    "Chapman": "Graham",
    "Cleese": "John",
    "Idle": "Eric",
    "Jones": "Terry",
    "Palin": "Michael"
}
signals = {'green': 'go', 'yellow': 'be careful', 'red': 'stop'}

even_numbers_set = {0,2,4,6,8}
odd_numbers_set = {1,3,5,7,9}

drinks = {
    'martini': {'vodka','vermouth'},
    'black russian': {'vodka','kahlua'},
    'white russian': {'cream','kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if ('vodka' in contents and not('vermouth' in contents or 'cream' in contents)):
        print(name)

for name, contents in drinks.items():
    if (contents & {'vermouth', 'orange juice'}):
        print(name)

for name, contents in drinks.items():
    if (contents & {'vodka'}):
        if (not(contents & {'vermouth', 'cream'})):
            print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

years_list = [1981,1982,1983,1984,1985,1986]

#f2e = {}
#for english, french in e2f.items():
#    f2e[french] = english

# life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],'octopi':{},'emus': {}},'plants': {},'other' {}}