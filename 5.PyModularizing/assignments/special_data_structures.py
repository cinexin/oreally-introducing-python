plain = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(plain)

from collections import OrderedDict
fancy = OrderedDict(plain)
print(fancy)

from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a'].append('something harder for a')
dict_of_lists['a'].append('something even harder for a')
dict_of_lists['a'].append('the hardest for a')
print(dict_of_lists)