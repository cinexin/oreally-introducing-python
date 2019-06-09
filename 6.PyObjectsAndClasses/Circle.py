# Here we illustrateuse of property decorator for computed fields
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2* self.radius
    
c = Circle(5)
c.radius
print(c.diameter)
c.radius = 7
print(c.diameter)