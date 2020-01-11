# model buying list item
import datetime
my_date = datetime.date(2016, 7, 11)
#blablabla
class GroceryItem:

    pledge_cost = 25
    
    def __init__(self, name, price):
        self.name  = name
        #price as money value
        self.price = price

    def itemDescription(self):
        return '{} : {}'.format(self.name, self.price) #(self.price / 100)) does not work bc of from_string, maybe harcast price into int?

    def apply_pledge(self):
        self.price +=  self.pledge_cost

    @classmethod
    def from_string(cls, item_str):
        name, price = item_str.split('-')
        return cls(name, price)

    @classmethod
    def set_pledge_cost(cls, amount)
        cls.set_pledge_cost = amount

    @staticmethod
    def foo_bar(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True      

# item init
item_1 = GroceryItem('noodles' , 79)
item_2 = GroceryItem('coke', 75)
item_3 = GroceryItem.from_string('Cherrystrauchtomaten-249')
item_4 = GroceryItem.from_string('towels-299')

# collection
items = [item_1, item_2, item_3, item_4]

#testing
item_2.apply_pledge()

#print(GroceryItem.__dict__)

i = 0

#iteration
for item in items:
    print(item.itemDescription())
    #i += item.price [line 15]

#print(price) [line 15]
print(GroceryItem.foo_bar(my_date))