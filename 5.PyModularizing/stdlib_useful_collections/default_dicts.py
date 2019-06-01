periodic_table = {'Hidrogen': 1, 'Helium': 2}
print(periodic_table)
carbon = periodic_table.setdefault('Carbon', 12)
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']
print(periodic_table)
print(periodic_table['Hydrogen'])
print(periodic_table['Lead'])

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

print(bestiary['A'])
print(bestiary['B'])
print(bestiary['WTF'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam', '', '', '']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)