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

'''