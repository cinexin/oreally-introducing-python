class Person():
    def __init__(self, name):
        self.name = name   
class MDPerson(Person):
    def __init__(self, name):
        self.name = "Dr " + name
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)