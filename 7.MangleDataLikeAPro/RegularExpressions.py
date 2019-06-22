import re
result = re.match('You','Young Frankenstein')
print(result)
my_pattern = re.compile('You')
result = my_pattern.match('Young Frankenstein')
'''
search() returns the first match
findall() returns a list of all non-overlapping matches, if any
split() splits source at matches with pattern and returns a list of the string pieces
sub() takes another replacement argument, and changes all parts of source that are matched by pattern to replacement
'''
# Exact match with match()
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())

# start anchor does the same
m = re.match('^You', source)
if m:
    print(m.group())
# What happens if the match isn't at the beginning of the source...?
m = re.match('Frank', source)
if m:
    print(m.group())
# it prints nothing!! :o

# search() works if the pattern is anywhere
m = re.search('Frank', source)
if m:
    print(m.group())
    
# Let's work with a bit more complex patterns
m = re.match('.*Frank', source)    
if m:
    print(m.group())
    
# First match with search()
m = re.search('Frank', source)
if m:
    print(m.group())

# All matches with findAll()
m = re.findall('n', source)
print(m)
print('Found',len(m),'matches')

# Search 'n' followed by any character
m = re.findall('n.',source)
print(m)

# What about any character (including no following character)
m = re.findall('n.?', source)
print(m)

# Split at matches
m = re.split('n', source)
print(m)

# Replace matches...
m = re.sub('n','?', source)
print(m)

# Pattern matching
import string
printable = string.printable
len(printable)
printable[0:50]
printable[50:]
# Which characters in printable are digits...?
re.findall('\d', printable)
# Which characters are alphanumeric?
re.findall('\w', printable)
# Which characters are spaces?
re.findall('\s', printable)

# Patterns: Using specifiers
source = "I wish I may, I wish I might...Have a dish of fish tonight"
re.findall('wish', source)
re.findall('wish | dish', source)
re.findall('^wish', source)
re.findall('^I wish', source)
re.findall('fish$', source)
re.findall('fish tonight$', source)
re.findall('[wf]ish', source)
re.findall('[wsh]', source)
re.findall('[wsh]+', source)
re.findall('ght\W', source)
# I followed by wish:
re.findall('I (?=wish)', source)
# I preceded by wish:
re.findall('(?<=I) wish', source)
# Specifying explicitely we're putting regular expressions to avoid clashing with Python escape characters
re.findall(r'\bfish', source)


# Patterns: specifying match output
m = re.search(r'(. dish\b).*(\bfish)', source)
m.group()
m.groups()

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
m.group()
m.groups()
m.group('DISH')
m.group('FISH')