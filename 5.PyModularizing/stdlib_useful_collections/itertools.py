import itertools

'''Itertools contain special-purpose iterator functions
Each returns one item at a time when called within a for loop, and remembers its state between calls'''

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)