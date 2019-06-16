class Bill():
    def __init__(self,description):
        self.description = description

class Tail():
    def __init__(self,length):
        self.length = length
        
class Duck():
    def __init__(self,bill,tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print("This Duck has a",self.bill.description,"bill and a",self.tail.length,"tail")
        
a_tail = Tail('long')
a_bill = Bill('Wide Orange')
duck = Duck(a_bill,a_tail)
duck.about()