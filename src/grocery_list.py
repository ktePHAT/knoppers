from product_unit import ProductUnit

unit_1 = ProductUnit('CoCa-Cola', '0.75')
unit_2 = ProductUnit('Beer', '1.75')
unit_3 = ProductUnit('Salmon', '4.23')
unit_4 = ProductUnit('Grapes', '0.99')

#print(unit_1.unit_description())
#print(unit_2.unit_description())
#print(unit_3.unit_description())
#print(unit_4.unit_description())

unit_1.apply_pledge()
#print(unit_1.unit_description())

grocery_list  = [ unit_1, unit_2, unit_3, unit_4 ]
grocery_tuple = ( unit_1, unit_2, unit_3, unit_4 )
grocery_set   = { unit_1, unit_2, unit_3, unit_4 }

print(grocery_list)

for unit in grocery_list:
    print(unit.unit_description())

    # funily doesnt work , it cycles out
    #popped = grocery_list.pop()
    #print(popped)
    # print(pop.unit_description())

