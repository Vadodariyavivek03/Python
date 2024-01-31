# Static variable : 

class Bakery:

    type = 'cake'                  # Class Variable

    def __init__(self,flavor,price):
        self.flavor = flavor            # Instance Variable
        self.price = price            # Instance Variable
 

a = Bakery('Butterscotch Cake', 300)
b = Bakery('Chocolate-Truffle Cake', 250)
 
print(a.type)  
print(b.type)  
print(a.flavor)  
print(b.flavor)  
print(a.price)   
print(b.price)   



