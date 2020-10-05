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
# GW list:
# TODO Average of the full run times:
    # how long on average would it take to mkae the list full of an animal type: 
    # 1.fullList will have to be converted to an int from a str
    # 2.store fullList by loop over river class over and over OR store in data in a file 
    # 2.1 in loop you need control manager function to control how its looping 
    # 2.2 in the file - read in from file - run applicaiton a good amount of times
# MB List:
# TODO Reflection of this project at the end 

from pylab import *
import numpy.random as random
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

class animal():

    def __init__(self, place):
        self.place = place

    def movement(self):
        """Moving the animal right or left one 
        and a print statement staying what animal 
        moved and in what direction"""

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
        """Initalize river"""

        self.ecosys = []
        animal = random.choice ([bear, fish, None], size=self.spot)
        for place, animal in enumerate(animal):
            self.ecosys.append(animal(place) if animal is not None else None)

        self.gdata = []
        self.fullList = ''

        for x in range((timestep)):
            self.gdata.append([[]])
        
    def getecosys(self):
        """Getter for the ecosystem"""

        return self.ecosys
    
    def add_random(self, animal):
        """Add animal to empty cell of river list after mating occurs"""
        
        if self.ecosys.count(None) > 0:
            choices = [i for i, x in enumerate(self.ecosys) if x is None]
            index = random.choice(choices)
            animal.place = index
            self.ecosys[index] = animal


    def manageAnimalInteraction(self, orgin, destinationIndex, finalDestination, animalCreationSpot, animalDeletionSpot):
        """
        Manages animal encounters in the ecosystem and storage lists. 

        orgin:                  The animals place in the list at the timestep. 
        destinationtIndex:      The index that the animal is goig to attempt to move to.
        finalDestination:       The index that the animal has moved to after testing for other animal types.
        animalCreationSpot:     An empty spot in the list where a new animal will be created.
        animalDeletionSpot:     After the animal moves its spot in the index is replace with a None

        """

        if isinstance(orgin, bear):
            if isinstance(finalDestination, bear):
                self.add_random(bear(0))
            elif isinstance(finalDestination, fish):
                animalCreationSpot = bear(destinationIndex)
                animalDeletionSpot = None
            else:
                animalCreationSpot = bear(destinationIndex)
                animalDeletionSpot = None

        elif isinstance(orgin, fish):
            if isinstance(finalDestination, fish):
                self.add_random(fish(0))
            elif isinstance(finalDestination, bear):
                animalDeletionSpot = None
            else:
                animalCreationSpot = fish(destinationIndex)
                animalDeletionSpot = None

        else:
            raise ValueError("Undefined Creature")

    def timeStep(self, t=1, text=True):
        """A point in time what the ecosystem looks like"""

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
                # else:
                    # orgin = self.ecosys[move_place]
                    # destinationIndex = new_spot
                    # finalDestination = self.ecosys[destinationIndex]
                    # animalCreationSpot = self.ecosys[new_spot]
                    # animalDeletionSpot = self.ecosys[move_place]

                    # self.manageAnimalInteraction(orgin, destinationIndex, finalDestination, animalCreationSpot, animalDeletionSpot)

            if text:
                self.display()


            bearCount = len([i for i, x in enumerate(self.ecosys) if isinstance(x,bear)])

            fishCount = len([i for i, x in enumerate(self.ecosys) if isinstance(x,fish)])

            print('Total number of bears in the ecosystem: ' , bearCount)
            print('Total number of fish in the ecosystem: ', fishCount)
                        
            self.gdata[self.itterationCount] = self.parsecosys()

            if self.fullList != '':
                pass
            elif bearCount == len(self.ecosys):
                self.fullList =  'The list became full of bears at ' + str(self.itterationCount) + ' timestep. '

            elif fishCount == len(self.ecosys):
                self.fullList =  'The list became full of fish at ' + str(self.itterationCount) + ' timestep. '


            self.itterationCount += 1

        print (self.fullList)


         
    def parsecosys(self):
        """Converting the animals to their associated colors for graphing"""

        result = []
        for x in range(len(self.ecosys)):
            if self.ecosys[x] is None:
                result.append(0.0)
            else:
                result.append(self.ecosys[x].color)
        return [result[1:len(self.ecosys)-1]]

    def graphEcosy(self):
        """Graphing the ecosystem"""
        
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
        """Print statent for the ecosystem"""

        print('===================')
        print('Ecosystem status: \n')
        print(self.ecosys, '\n')
        print('===================') 

 
itterations = 50
River = river(50)
River.initalize(itterations)
River.display()
River.timeStep(itterations)
River.graphEcosy()
