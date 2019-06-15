class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I am a A!")
    @classmethod
    def kids(cls):
        print("A has",cls.count,"little objects.")
        
easy_a = A()
breezy_a = A()
wheezy_A = A()
A.kids()