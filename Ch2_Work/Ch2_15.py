'''R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an integer
d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates
<4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it produces
a vector with coordinates based on that sequence.'''

class Vector:
    '''Represent a vector in a multidimensional space.'''

    def __init__(self, coords):
        self._coords = coords
        if isinstance(coords,list):
            for i in range(len(coords)):
                self._coords[i] = coords[i]
        elif isinstance(coords,int):
            self._coords = [0] * coords
       
    def __len__ (self):
        '''Return the dimension of the vector.'''
        return len(self._coords)

    def __getitem__ (self, j):
        '''Return jth coordinate of vector.'''
        return self._coords[j]

    def __setitem__ (self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val

    def __add__ (self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other): # relies on len method
            raise ValueError( 'dimensions must agree' )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__ (self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords

    def __ne__ (self, other):
        '''Return True if vector differs from other.'''
        return not self == other # rely on existing _eq_ definition

    def __str__ (self):
        '''Produce string representation of vector.'''
        return '<' + str(self._coords)[1:-1] + '>' # adapt list representation


ini_list1 = Vector([1, 2, 3, 4, 5])
print(ini_list1.__str__())

ini_list2 = Vector(5)
print(ini_list2.__str__())

