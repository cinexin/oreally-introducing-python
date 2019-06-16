from collections import namedtuple

# A namedtuple is a lightweight alternative to classes
Duck = namedtuple('Duck','bill, tail')
duck = Duck('wide orange','long')
duck
parts = {'bill':'wide orange','tail':'long'}
duck2 = Duck(**parts)
duck

# namedtuples are immutable, but there's a workaround
duck3 = duck2._replace(tail = 'magnificent', bill = 'crushing')
duck3

'''Namedtuples:
- Looks and act as immutable objects
- More space and time efficient
- You can access attributes by using dot notation instead of dictionary-style square brackets
- You can use it as a dictionary key
'''