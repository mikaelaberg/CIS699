"""P-2.36 Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears)."""

#Current Issues:
#the variables are there but what is showing up 
#is their location not the actualy contents 
#maybe missing () somewhere in the long list of else statments??


# My Notes Fpr the Program:
#
# in the time step every object should move to an adjacent place in 
# in the list, longer list 
# 
# 
# crude animation; print one loop thorugh the list ; could also be a debugger
# make this 2d could make this like a game of life, where I walk though every 
# cell, or follow the animals
# 
# 
# can the animal move mulitple times or just once, its unrealistic that they can only move once
# every andimal gets a chance to move on the list. 
# 
# 
# and dont forget about the ends of the list/box 
# I can make the rules for the end of the box/beginging 
# of the box 

import random
import numpy as np
import matplotlib as plt


class animal():

    def __init__(self, place):
        self.place = place      #place animal in the food chain

    def moveAnimal(self):
        return self.place

class bear(animal):

    def __placeBear__(self):
        return "Bear(%s)" % self.place

    def movement(self):
        step = np.random.choice([-1,1])
        new_place = self.place + step
        print(self, 'moves', 'left' if step == -1 else 'right')
        return new_place

class fish(animal):

    def __placeFish__(self):
        return "Fish(%s)" % self.place

    def movement(self):
        step = np.random.choice([-1,1])
        new_place = self.place + step
        print(self, 'moves', 'left' if step == -1 else 'right')
        return new_place


class river:

    def __init__(self, spot):
        self.spot = spot
        ecosys = None

    def initalize(self):
        self.ecosys = []
        animal = np.random.choice ([bear, fish, None], size=self.spot)
        for place, animal in enumerate(animal):
            self.ecosys.append(animal(place) if animal is not None else None)

    def timeStep(self, t=1, text=True):
        for i in range(t):
            move_place = np.random.choice(list(range(self.spot)))
            if self.ecosys[move_place] is None:
                print ('No movement')
                pass
            else:
                new_spot = self.ecosys[move_place].moveAnimal()
                if new_spot < 0 or new_spot > len(self.ecosys) -1:
                    pass
                elif isinstance(self.ecosys[move_place], bear):
                    if isinstance(self.ecosys[new_spot], bear):
                        pass
                    elif isinstance(self.ecosys[new_spot], fish):
                        self.ecosys[new_space] = bear(new_spot)
                        self.ecosys[move_place] = None
                    else:
                        self.ecosys[new_space] = bear(new_spot)
                elif isinstance(self.ecosys[move_place], fish):
                    if isinstance(self.ecosys[new_spot], fish):
                        pass
                    elif isinstance(self.ecosys[new_spot], bear):
                        self.ecosys[move_place] = None
                    else:
                        self.ecosys[new_space] = fish(new_spot)
                else:
                    raise ValueError("Undefined Creature")
            if text:
                self.display()

    def display(self):
        print('===================')
        print('Ecosystem status: \n')
        print(self.ecosys, '\n')
        print('===================')


print(bear(3))
print(fish(5))
print(river(5))



# River = river(5)
# River.initalize()
# River.display

# River.timeStep(10)
