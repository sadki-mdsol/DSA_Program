from numpy import *

m1 = array([
    [1,2,3],
    [2,3,4],
    [4,5,6]
])

m2 = array([
    [1,2,3],
    [2,6,4],
    [5,5,6]
])

matrix1 = matrix(m1)
matrix2 = matrix(m2)

print(m1.ndim) #no of dimensions
print(m1.diagonal()) #diagonal of matrix
print(m1.dtype) #type of matrix
print(m1.shape) #(no of rows,no of columns)
print(m1.size) #total elemtns
print("Additon----")
print(m1+m1)
print("Multiplication----")
print(m1*m2)