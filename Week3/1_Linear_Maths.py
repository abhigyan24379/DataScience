import numpy as np 

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# print ("Addition :\n", A + B)
# print ("Subtraction:\n " , A - B)
# print ("Subtraction:\n " ,  B - A)

C = 2 * A
print ("Scalar multiplication \n ", C)

# Matrix Multiplication 
# Formula (A.B) =  ∑  A  B
#              ij   k  ik kj

result = np.dot(A,B)
# print ("Matrix multiplication: \n", result)

#Special Matrix 

# Idenity Matrix
I = np.eye(3)
print ("Identity Matrix: \n ",I)

#Zero Matrix 
Z = np.zeros((2,3))
print ("Zero Matrix: \n", Z)

# Diagonal Matrix 
D = np.diag([1,2,3])
print ("Diagonal Matrix \n", D)
