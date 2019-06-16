'''
Make a class called Thing with no contents and print it
Then, create an object called example from this class and also print it.
Are the printed values the same or different?
'''
class Thing():
    def __init__(self):
        pass
example = Thing()

print(Thing)
print(example)

'''
Make a class called Thing2 and assign the value 'abc' to a class attribute called letters
Print letters
'''
class Thing2():
    letters = 'abc'
print(Thing2.letters)

'''
Make another class Thing3. This time, assign the value 'xyz'
to an instance called letters. Print letters
Do you need an object? (Of course, yes)
'''
class Thing3():
    def __init__(self,letters):
        self.letters = letters
letters = Thing3('xyz')
print(letters.letters)

'''
Make a class called Element with instance attributes:
- name 
- symbol
- number
Create an object: 'Hydrogen','H',1

Define a method dump() that prints the object's attributes
Make dump() method to be the one that it's called when you print the object

Make attributes private and define getters and setters for them
'''
class Element():
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, element_name):
        self.__name = element_name
        
    @property
    def symbol(self):
        return self.__symbol
    @symbol.setter
    def symbol(self, element_symbol):
        self.__symbol = element_symbol
        
    @property
    def number(self):
        return self.__number
    @symbol.setter
    def number(self, element_number):
        self.__number = element_number
        
    def dump(self):
        dump_content = "Name:" + self.name + "- Symbol:" + self.symbol + "- Number:" + str(self.number)
        return dump_content
    def __str__(self):
        return self.dump()
    
hydrogen = Element('Hydrogen','H',1)

'''
Make a dictionary with these keys and values:
'name': 'Hydrogen'
'symbol': 'H'
'number': 1
Then, create hydrogen object using this dictionary
'''
hydrogen_dict = dict({'name':'Hydrogen','symbol':'H', 'number':1})
hydrogen = Element(**hydrogen_dict)
hydrogen.dump()
print(hydrogen)

'''
Define 3 classes: Bear, Rabbit and Octothorpe
For each, define one method: eats()
This should return 'berries'(Bear), 'clover' (Rabbit), 'campers' (Octothorpe)
Create one instance from each and print what it eats
'''
class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'
class Octothorpe:
    def eats(self):
        return 'campers'
a_bear = Bear()
a_rabbit = Rabbit()
a_octothorpe = Octothorpe()
print(a_bear.eats())
print(a_rabbit.eats())
print(a_octothorpe.eats())

'''
Define these classes: Laser, Claw, and SmartPhone
Each has only one method: does()
This return:
 'disintegrate' (Laser)
 'crush' (Claw)
 'ring' (Smartphone)
Then, define the class Robot that has one instance (object) of each of these
Define a does method for Robot that prints waht its component objects do
'''
class Laser():
    def does(self):
        return 'disintegrate'
class Claw():
    def does(self):
        return 'crush'
class SmartPhone():
    def does(self):
        return 'ring'
class Robot():
    def __init__(self,laser,claw,smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone
    def does(self):
        return self.laser.does() + "," + self.claw.does() + "," + self.smartphone.does()

a_laser = Laser()
a_claw = Claw()
a_smartphone = SmartPhone()
a_robot = Robot(a_laser,a_claw,a_smartphone)
print(a_robot.does())