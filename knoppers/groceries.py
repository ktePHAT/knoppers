from product import ProductUnit
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

        if product.pledge:
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