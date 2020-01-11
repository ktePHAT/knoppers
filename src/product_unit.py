from money.money import Money
from money.currency import Currency


class ProductUnit:
    
    def __init__(self, name, price):
        self.name  = name
        self.price = Money(price, Currency.EUR)
    
    
    def apply_pledge(self):
        """Pfand"""
        pledge = Money('0.25', Currency.EUR)
        self.price += pledge

    def unit_description(self):
        return '{} : {}'.format(self.name, self.price.format('de_DE'))

#coke = ProductUnit('CoCa-Cola', '0.75')
#print(coke.name)
#print(coke.price)
#print(coke.unit_description())