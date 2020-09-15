'''R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.'''

class Flower:
    
    def __init__(self, name, petal, pricePer):
        self.name = name
        self.petal = petal
        self.pricePer = pricePer

    def __getName__(self):
        return self.name

    def __setName__(self, name):
        self.name = name

    def __getPetal__(self):
        return self.petal

    def __setPetal__(self, petal):
        self.petal = petal
    
    def __getPricePer__(self):
        return self.pricePer

    def __setPricePer__(self, name):
        self.pricePer = pricePer

flw_1 = Flower('Rose', 5, 5.50)
flw_2 = Flower('Tulip', 3, 2.50)

print(flw_1.__getPetal__())
print(flw_2.__getPetal__())