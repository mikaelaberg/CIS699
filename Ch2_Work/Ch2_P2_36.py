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

import random
import numpy as np

class animal():

    def __init__(self, place):
        self.place = place      #an animals place in the food chain

    def moveAnimal(self):
        return self.place

class bear(animal):

    def __placeBear__(self):
        return "Bear(self.place)"

    def movement(self):
        step = np.random.choice([-1,1])
        new_place = self.place + step
        print(self, 'moves', 'left' if step == -1 else 'right')
        return new_place

class fish(animal):

    def __placeFish__(self):
        return "Fish(self.place)"

    def movement(self):
        step = np.random.choice([-1,1])
        new_place = self.place + step
        print(self, 'moves', 'left' if step == -1 else 'right')
        return new_place

class river:

    def __init__(self, space):
        self.space = space
        self.ecosys = None

    def initalize(self):
        self.ecosys = []
        animal = np.random.choice ([bear, fish, None], size=self.space)
        for place, animal in enumerate(animal):
            self.ecosys.append(animal(place) if animal is not None else None)

    def timeStep(self, t=1, text=True):
        for i in range(t):
            move_place = np.random.choice(list(range(self.space)))
            if self.ecosys[move_place] is None:
                print ('No movement')
                pass
            else:
                new_space = self.ecosys[move_place].moveAnimal()
                if new_space < 0 or new_space > len(self.ecosys) -1:
                    pass
                elif isinstance(self.ecosys[move_place], bear):
                    if isinstance(self.ecosys[new_space], bear):
                        pass
                    elif isinstance(self.ecosys[new_space], fish):
                        self.ecosys[new_space] = bear(new_space)
                        self.ecosys[move_place] = None
                    else:
                        self.ecosys[new_space] = bear(new_space)
                elif isinstance(self.ecosys[move_place], fish):
                    if isinstance(self.ecosys[new_space], fish):
                        pass
                    elif isinstance(self.ecosys[new_space], bear):
                        self.ecosys[move_place] = None
                    else:
                        self.ecosys[new_space] = fish(new_space)
                else:
                    raise ValueError("Undefined Creature")
            if text:
                self.display()

    def display(self):
        print('===================')
        print('Ecosystem status: \n')
        print(self.ecosys, '\n')
        print('===================')

River = river(5)
River.initalize()
River.display

River.timeStep(10)
