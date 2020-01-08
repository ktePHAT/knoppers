# modell buying list item

class GroceryItem:
    
    pledge_cost = 25

    def __init__(self, name, price):
        self.name  = name
        self.price = price
        #pfand as switch field?

    def itemDescription(self):
        return '{} : {}'.format(self.name, (self.price / 100))
        #return self.name

    def apply_pledge(self):
        self.price +=  self.pledge_cost

# item init
item_1 = GroceryItem('noodles' , 79)
item_2 = GroceryItem('coke', 75)
item_3 = GroceryItem('Cherrystrauchtomaten', 249)
item_4 = GroceryItem('towels', 299)

# collection
items = [item_1, item_2, item_3, item_4]

#testing
item_2.apply_pledge()
print(GroceryItem.__dict__)

#iteration
for item in items:
    print(item.itemDescription())