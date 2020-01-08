# model buying list item

class GroceryItem:
    
    pledge_cost = 25

    def __init__(self, name, price):
        self.name  = name
        self.price = price
        #pfand as switch field?

    def itemDescription(self):
        return '{} : {}'.format(self.name, self.price) #(self.price / 100)) does not work bc of from_string, maybe harcast price into int?

    def apply_pledge(self):
        self.price +=  self.pledge_cost

    @classmethod
    def from_string(cls, item_str):
        name, price = item_str.split('-')
        return cls(name, price)


    @classmethod
    def set_pledge_cost(cls, amount):
        cls.set_pledge_cost = amount

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

#iteration
for item in items:
    print(item.itemDescription())