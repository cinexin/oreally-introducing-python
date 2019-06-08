import itertools

'''Itertools contain special-purpose iterator functions
Each returns one item at a time when called within a for loop, and remembers its state between calls'''

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
    
for item in itertools.cycle([1,2]):
    print(item)
    
import itertools
for item in itertools.accumulate([1,2,3,4]):
    print(item)
    
import itertools
def multiply(a,b):
    return a*b

for item in itertools.accumulate([1,2,3,4], multiply):
    print(item)