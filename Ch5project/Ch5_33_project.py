"""
MB:
TODO Would like to improve this by using files as well as make it work in
the way I want it to work so that I understand the concepts better. Like
maybe have a user input or pull from a file.
DOCUMENTATION!

GW:
#TODO write utility programs to do test cases (data)
# write small scripts that generate strings of intgers into af file and test against it
# does this work with negative numbers, zeros, ect.

"""

import operator
class Matrix():
    #For subclassing...
    @classmethod
    def getClass(cls):
        return cls

    def __init__(self, data, numberOfdimensions = 3):
        self.data = data
        self.dimensions = []
        self.numberOfdimensionsims = numberOfdimensions
        temp = data
        for i in range(numberOfdimensions):
            self.dimensions.append(len(temp))
            temp = temp[0]

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return (self.dimensions[0])

    def __repr__(self):
        return (f'{self.numberOfdimensionsims}D Matrix with dimensions {self.dimensions}:' + '\n' + f'{self.data}')

    def createEmpty3dDataset(self, dimensions):
        a = None
        for d in reversed(dimensions):
            a = [None for _ in range(d)] if a is None else [a.copy() for _ in range(d)]
        return self.getClass()(a, len(dimensions))

    def operationListReturn(self, a, b, c, operation):
        """ a + b = c """
        assert len(a) == len(b) == len(c), 'Length mismatch'
        for i in range(len(a)):
            if isinstance(a[i], list): self.operationListReturn(a[i], b[i], c[i], operation)
            else: c[i] = operation(a[i],b[i])
        return c

    def __add__(self, other):
        assert self.dimensions == other.dimensions, f'Dimension mismatch {self.dimensions}, {other.dimensions}'
        c = self.createEmpty3dDataset(self.dimensions)
        return (self.operationListReturn(self.data, other.data, c, operator.add))


class MatrixwMult(Matrix):
    def __mul__(self, other):
        assert self.dimensions == other.dimensions, f'Dimension mismatch {self.dimensions}, {other.dimensions}'
        c = self.createEmpty3dDataset(self.dimensions)
        return (self.operationListReturn(self.data, other.data, c, operator.mul))

    def dotProduct(self, other):
        assert len(self.dimensions) == 2, 'Dot product not implemented for rank>2'


        ar, ac = self.dimensions
        br, bc = other.dimensions

        c = self.createEmpty3dDataset([ar, bc])

        a = self.data
        b = other.data

        print(c.dimensions)

        for i in range(ar):
            for j in range(bc):
                total = 0
                for k in range(ac):
                    total += a[i][k]*b[k][j]
                    # print (total, a[i][k], b[k][j], 'Index', i, j, k)
                c.data[i][j] = total
        return c


"""Ch5_P_33: Write a Python program for a matrix class that can add and multiply two dimensional
arrays of numbers, assuming the dimensions agree appropriately for the operation."""

matrixA = MatrixwMult([[1,2,3],[4,5,6]], 2)
matrixB = MatrixwMult([[1,2,3],[1,2,3],[1,2,3]], 2)

matrixA.dotProduct(matrixB)

# print(matrixA * matrixB)    #Showing how the Assertion works for if the dimensions don't match

""" Reflection:
Completed this project last week and I honestly feel like I had BAD documentation with this one,
because I honestly don't remember why I have some bits vs others. I also was never actually able
to complete the file stuff I wanted to do.
"""
