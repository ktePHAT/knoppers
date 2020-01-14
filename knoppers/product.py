from money.money import Money
from money.currency import Currency

class ProductUnit:
    
    def __init__(self, name, price):
        self.name   = name
        self.price  = Money(price, Currency.EUR)
        self.pledge = False
    
    
    def apply_pledge(self):
        """Pfand"""
        self.pledge = True

    def unit_description(self):
        return '{} : {}'.format(self.name, self.price.format('de_DE'))

#coke = ProductUnit('CoCa-Cola', '0.75')
#print(coke.name)
#print(coke.price)
#print(coke.unit_description())