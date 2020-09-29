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

#Current Improvemnts:
# TODO graphing; better labels/ key.
# TODO code: "we need a bigger ecosystem", what 
        # would happen when/if the ecosystem 
        # is full of bears/Fish/None
        # The above doesnt happen as long as 
        # the list/ecosystem is large 

from pylab import *
import numpy.random as random
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

class animal():

    def __init__(self, place):
        self.place = place

    def movement(self):
        step = random.choice([-1,1])
        new_place = self.place + step
        print(self, 'moves', 'left' if step == -1 else 'right')
        return new_place


class bear(animal):
    def __init__(self,place):
        super().__init__(place)
        self.color = 0.5

    def __repr__(self):
        return "Bear(%s)" % self.place


class fish(animal):
    def __init__(self, place):
        super().__init__(place)
        self.color = 0.7

    def __repr__(self):
        return "Fish(%s)" % self.place


class river:

    def __init__(self, spot):
        self.spot = spot
        ecosys = None
        self.itterationCount = 0

    def initalize(self, timestep):
        self.ecosys = []
        animal = random.choice ([bear, fish, None], size=self.spot)
        for place, animal in enumerate(animal):
            self.ecosys.append(animal(place) if animal is not None else None)

        self.gdata = []
        
        for x in range((timestep)):
            self.gdata.append([[]])
        
    def getecosys(self):
        return self.ecosys
    
    def add_random(self, animal):
        """Add animal to empty cell of river list after mating occurs"""
        if self.ecosys.count(None) > 0:
            choices = [i for i, x in enumerate(self.ecosys) if x is None]
            index = random.choice(choices)
            animal.place = index
            self.ecosys[index] = animal

    def timeStep(self, t=1, text=True):
        for i in range(t):
            move_place = random.choice(list(range(self.spot)))
            
            if self.ecosys[move_place] is None:
                print ('No movement')
                pass
            else:
                new_spot = self.ecosys[move_place].movement()
                if new_spot < 0 or new_spot > len(self.ecosys) -1:
                    self.ecosys[move_place] = None
                elif isinstance(self.ecosys[move_place], bear):
                    if isinstance(self.ecosys[new_spot], bear):
                        self.add_random(bear(0))
                    elif isinstance(self.ecosys[new_spot], fish):
                        self.ecosys[new_spot] = bear(new_spot)
                        self.ecosys[move_place] = None
                    else:
                        self.ecosys[new_spot] = bear(new_spot)
                        self.ecosys[move_place] = None

                elif isinstance(self.ecosys[move_place], fish):
                    if isinstance(self.ecosys[new_spot], fish):
                        self.add_random(fish(0))
                    elif isinstance(self.ecosys[new_spot], bear):
                        self.ecosys[move_place] = None
                    else:
                        self.ecosys[new_spot] = fish(new_spot)
                        self.ecosys[move_place] = None
                else:
                    raise ValueError("Undefined Creature")
            if text:
                self.display()
         
            self.gdata[self.itterationCount] = self.parsecosys()

            self.itterationCount += 1
         
    def parsecosys(self):
        result = []
        for x in range(len(self.ecosys)):
            if self.ecosys[x] is None:
                result.append(0.0)
            else:
                result.append(self.ecosys[x].color)
        return [result]

    def graphEcosy(self):
        fig, ax = plt.subplots()

        for x in range(len(self.gdata)):
            cmap = cm.get_cmap('coolwarm',4)
            im = ax.imshow(self.gdata[x], cmap = cmap)
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("bottom", size="500%", pad=.5)
            plt.colorbar(im, cax=cax, label = "Fish=0.7 Bear=0.5 \n None=0.0")

        for i in range(len(self.gdata)):
            ax.cla()
            ax.imshow(self.gdata[i], 'coolwarm')
            ax.set_title("River Ecosystem Time Step {}".format(i))
            plt.pause(0.1)

    def display(self):
        print('===================')
        print('Ecosystem status: \n')
        print(self.ecosys, '\n')
        print('===================')

itterations = int(input("How many itearatios do we want to observe? "))
River = river(100)
River.initalize(itterations)
River.display()
River.timeStep(itterations)
River.graphEcosy()
