'''R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.'''

class Flower:
    
    def __init__(name, petal, price):
        self.name = name
        self.petal = petal
        self.price = price

    