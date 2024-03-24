from typedproperty import typedproperty

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'
    
    @property
    def cost(self):
        return self.shares * self.price
        
    def sell(self, num_shares):
        self.shares -= num_shares
        
        
class MyStock(Stock):
    def cost(self):
        actual_cost = super().cost()
        return 1.25 * actual_cost
        
    def panic(self):
        self.sell(self.shares)
