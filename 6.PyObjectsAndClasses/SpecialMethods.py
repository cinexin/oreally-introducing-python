class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
    # Using special method...
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    
first = Word('ha')
second = Word('HA')
third = Word('eh')

first.equals(second)
second.equals(third)

first == second
second == third
'''Table of Magic Methods:
__eq__(self, other) => self == other
__ne__(self, other) => self != other
__lt__(self, other) => self < other
__gt__(self, other) => self > other
__le__(self, other) => self <= other
__ge__(self, other) => self >= other

__add__(self, other) => self + other
__sub__(self, other) => self - other
__mul__(self, other) => self * other
__floordiv__(self, other) => self // other
__truediv__(self, other) => self / other
__mod__(self, other) => self % other
__pow__(self, other) => self ** other

__str__(self) => str(self)
__repr__(self) => repr(self)
__len__(self) => len(self)
'''
class Word():
    def __init__(self,text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return "Word(" + self.text + ")"

first = Word('ha')
first
print(first)
