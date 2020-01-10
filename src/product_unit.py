from money.money import Money
from money.currency import Currency


class ProductUnit:
    pass


m = Money('9.95', Currency.EUR).format('de_DE')
print(m)
test = "test" 
#fooBar