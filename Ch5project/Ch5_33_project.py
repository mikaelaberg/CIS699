# Write a Python program for a matrix class that can add and multiply two dimensional
# arrays of numbers, assuming the dimensions agree appropriately
# for the operation.

# MB TODO:
# 1. read and write into a file 
# 2. any way to make this biologically relevant?

class matrixMath():

    def __init__(self):
        X = [[1,2,3],  
            [4,5,6],  
            [7,8,9]]  
        Y = [[10,11,12],  
            [13,14,15],  
            [16,17,18]]   
        result = [[0,0,0],  
                    [0,0,0],  
                    [0,0,0]]

    def matrixMultiplication(self):
        """Multiplication of the matrix"""

        for i in range(len(X)):  
           for j in range(len(Y[0])):  
               for k in range(len(Y)):  
                   self.result[i][j] += X[i][k] * Y[k][j]  
        for r in self.result:  
           return(r) 

    def matrixAddition(self):
        """Addtion of the matrix"""

        for i in range(len(X)):  
           for j in range(len(Y[0])):  
               for k in range(len(Y)):  
                   self.result[i][j] += X[i][k] + Y[k][j]  
        for r in self.result:  
           return(r) 


