# FUNCTIONS ASSIGNMENTS
# 4.1
guess_me = 9
if guess_me > 7:
    print('too high')
elif guess_me < 7:
    print('too low')
else:
    print('just right')
    
# 4.2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low!')
    else:
        if start == guess_me:
            print('found it!')
            break
        elif start > guess_me:
            print('Ooooooops')
            break
    start += 1
    
# 4.3
for value in [3,2,1,0]:
    print(value)
    
# 4.4
first_even_numbers = [number for number in range(10) if number % 2 == 0]

# 4.5
first_squares = {i: i*i for i in range(10)}

# 4.6
first_odd_numbers = {i for i in range(10) if i % 2 == 1}

# 4.7
got_generator = ('Got '+ str(i) for i in range(10))
for got in got_generator:
    print(got)
    
# 4.8
def good():
    return ['Harry', 'Ron', 'Hermione']    

# 4.9
def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i

for i in get_odds():
    print(i)
    
# 4.10
def test(func):
    def inner_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print(result)
        print('end')
        return result
    return inner_func
@test
def add_ints(a,b):
    return a + b

# 4.11
class OopsException(Exception):
    pass
try:
    raise OopsException
except OopsException:
    print("Caught an oops")

# 4.12
movies = zip(['Creature of Habit', 'Crewel Fate'], ['A nun turns into a monster', 'A haunted yarn shop'])
for movie in movies:
    print ("Movie:", movie)