# Determinant and Inverse of a Matrix
#  --> Determinants 
#     -scalar value that provides information about a matrix's properties  
#     -only for square matrices 
#     -det(A) = 0, the matrix A is singular 
#     -det(A)!= =, A is invertible
#     -Geometric Interpretation 
#          - for a 2X2 matrix the dterminant represents the scaling factor of the area formed by its column vectors 
#     -Formula for 2X2 matrix = ad - bc

import numpy as np 
A = np.array([[2,3],[1,4]])
determinant = np.linalg.det(A)
print ("determinant \n", determinant)

 # --> Inverse of a Matrix
 #    - denoted as A^-1
 #    - product of a matrix and its inverse is the identity matrix AXA^-1 = 1
 #    - Matrix is invertible only if det(A) != 0
 #    formula A^-1 = 1/det *Adj[A]
 
inverse = np.linalg.inv(A)
print ("Inverse of A :\n" , inverse) 
 