from product_unit import ProductUnit
from money.money import Money
from money.currency import Currency

def groceries(products):
    
    units = 0
    pldge = 0
    
    total = Money('0.0', Currency.EUR)
    pfand = ProductUnit('Pfand', '0.25')

    print('[Groceries]:')

    for product in products:
        print(product.unit_description())
        total += product.price
        units += 1

        if (product.pledge):
            print('     {}'.format(pfand.unit_description()))
            total += pfand.price
            pldge += 1

    pfand_total = pfand.price * pldge
    total_pless = total - pfand_total        

    # calculates avg including pledges
    #print('{} items bought, averaging in price at {}'.format(units, (total / units).format('de_DE')))
    # calculates avg excluding pledges
    print('{} items bought, averaging in price at {}'.format(units, (total_pless / units).format('de_DE')))
    
    print('[Total : {}]'.format(total.format('de_DE')))   

unit_1 = ProductUnit('CoCa-Cola', '0.75')
unit_2 = ProductUnit('Beer', '1.75')
unit_3 = ProductUnit('Salmon', '4.23')
unit_4 = ProductUnit('Grapes', '0.99')

unit_1.apply_pledge()
unit_2.apply_pledge()

grocery_list  = [ unit_1, unit_2, unit_3, unit_4 ]
grocery_tuple = ( unit_1, unit_2, unit_3, unit_4 )
grocery_set   = { unit_1, unit_2, unit_3, unit_4 }

groceries(grocery_list)

# funily doesnt work , it cycles out
#popped = grocery_list.pop()
#print(popped)
# print(pop.unit_description()