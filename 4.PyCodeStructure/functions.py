def do_nothing():
    pass

def make_a_sound():
    print("quack")

def agree():
    return True

def echo(anything):
    return anything +' '+ anything

def reverse_echo(anything):
    return anything +' '+ anything[::-1]

def comment_a_color(color):
    if color == 'red':
        return "It's a tomatoe"
    elif color == 'green':
        return "It's a green pepper"
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it"
    else:
        return "I've never head of " + color

def menu(wine, entree, dessert = 'cola-cao'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

def print_args(*args):
    print("Positional argument tuple:", args)

# THIS IS EXTREMELY TRICKY TO ME
def buggy(arg, result=[]):
    result.append(arg)    
    print(result)

def non_buggy(arg, result = None):
    if result == None:
        result = []
    result.append(arg)
    print(result)

# KEYWORD ARGUMENTS
def print_kwargs(**kwargs):
    print("Keyword arguments:",kwargs)
print_kwargs(wine='Merlot',entree='Mutton',dessert='Macaroon')

# DOCUMENTATION COUNTS
def print_if_true(thing,check):
    '''
    Prints the first argument if the second argument is true
    The operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

# FUNCTIONS AS OBJECTS / PARAMS        
def answer():
    print(42)
    
def run_something(func):
    func()

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
    
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

# INNER FUNCTIONS
def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)

# CLOSURES
def knights(saying):
    def inner():
        return "We are the knights who say: %s" % saying
    return inner
duckKnights = knights('Duck')
germanKnights = knights('Hasenpfeffer')
type(duckKnights)
type(germanKnights)
duckKnights()
germanKnights()

# LAMBDAS
def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
     #give that prose more punch!
     return word.capitalize() + "!"

# envliven is so short we could replace with a lambda 
edit_story(stairs, lambda word: word.capitalize() + '!')

# GENERATORS
def my_custom_range(first = 0, last = 10, step = 1):
    number = first
    while number < last:
        yield number
        number += step
        
for n in my_custom_range(1,5):
    print(n)
    
    
# DECORATORS
def document_it(func):
    def new_function(*args, **kwargs):
        print ('Running function: '+ func.__name__)
        print ('Positional arguments',args)
        print ('Keyword arguments',kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
def add_ints(a,b):
    return a + b
cooler_add_ints = document_it(add_ints)
@document_it
def add_ints(a,b):
    return a + b

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a,b):
    return a + b

@square_it
@document_it
def add_ints(a,b):
    return a + b

# GLOBALS AND LOCALS
animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())
    
# RESERVED NAMES / KEYWORDS
def amazing_spiderman():
    '''This is Amazing Spiderman function.
    Want to see it again??'''
    print('This function is named:', amazing_spiderman.__name__)
    print('And its docstring is:', amazing_spiderman.__doc__)
    
