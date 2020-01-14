from knoppers.product import ProductUnit
from knoppers.groceries import groceries

def run():
    unit_1 = ProductUnit('Tomatos',   '2.49')
    unit_2 = ProductUnit('Noodels',   '0.79')
    unit_3 = ProductUnit('Coca-Cola', '0.75')
    unit_4 = ProductUnit('Towels',    '2.99')

    unit_3.apply_pledge()

    grc_shp = [unit_1, unit_2, unit_3, unit_4]
    groceries(grc_shp)

if __name__ == '__main__':
    run()