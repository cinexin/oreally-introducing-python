def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))
    
unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')
unicode_test('\u00e9')
import unicodedata
unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')
place = 'caf\u00e9'
print(place)
u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)
drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my drink',drink,'in a',place)

# The string len function counts Unicode characters, not bytes...
len('$')
len('\U0001f47b')