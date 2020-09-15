'''R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.'''

class Flower:
    
    def __init__(self, name, petal, priceper, numof):
        self.name = name
        self.petal = petal
        self.priceper = priceper

    # def sellingCost(self):
    #     return ('{}' '{}'.format((self.priceper) * (self.numof)))

flw_1 = Flower('Rose', 5, 5.50)
flw_2 = Flower('Tulip', 3, 2.50)

# print(flw_1)
# print(flw_2)

# print(flw_1.sellingCost())