
quotes = {
    'Moe': 'A wise guy, huh?',
    'Curly': 'Nyuk nyuk!',
    'Larry': 'Ow!'
}

for stooge in quotes:
    print(stooge)

from collections import OrderedDict

# Ordered Dict respects the order in which you insert the elements
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Curly', 'Nyuk nyuk!'),
    ('Larry', 'Ow!')
])
for stooge in quotes:
    print(quotes)