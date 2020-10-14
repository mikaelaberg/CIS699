"""
Based on how we created the array before, we can subclass and add elementwise multiplication easily

Note, if we are talking about matrix multiplication (the dot product), we should stick to 2D and 
assert accordingly



"""

class MatrixwMult(Matrix):
    def __mul__(self, other):
        assert self._dimensions == other._dimensions, f'Dimension mismatch {self._dimensions}, {other._dimensions}'
        c = self._create_empty_3D_dataset(self._dimensions)
        return (self._op_lists_r(self._data, other._data, c, operator.mul))
    
    def dot_product(self, other):
        assert len(self._dimensions) == 2, 'Dot product not implemented for rank>2'
        
        
        ar, ac = self._dimensions
        br, bc = other._dimensions
        
        c = self._create_empty_3D_dataset([ar, bc])

        a = self._data
        b = other._data
        
        print(c._dimensions)
        
        for i in range(ar):
            for j in range(bc):
                total = 0
                for k in range(ac):
                    total += a[i][k]*b[k][j]
                    #print (total, a[i][k], b[k][j], 'Index', i, j, k)
                c._data[i][j] = total
                             
        return c

    
mm1 = MatrixwMult([[[i for i in range(10)] for i in range(7)] for i in range(4)])
mm2 = MatrixwMult([[[i for i in range(10)] for i in range(7)] for i in range(4)])
    
print(mm1*mm2)


mmm1 = MatrixwMult([[1,2,3],[4,5,6]], 2)
mmm2 = MatrixwMult([[1,2,3],[1,2,3],[1,2,3]], 2)


mmm1.dot_product(mmm2)