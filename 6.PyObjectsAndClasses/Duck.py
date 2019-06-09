class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
fowl.name
fowl.name = 'Daffy'

# Use of decorators to define properties...
class BetterDuck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
donald = BetterDuck('Howard')
donald.name
donald.name = 'Donald'

# Private fields using Python standar way (the "__")
class Duck():
    
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name
fowl = Duck('Howard')
fowl.name
fowl.name = 'Donald'
fowl.name
# You'll never be able to access fowl.__name
# but there's a trick...
print(fowl._Duck__name)