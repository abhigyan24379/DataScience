import numpy as np

#create matrices 
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([1,0,-1])

#Matrix-Vector multiplication
result = np.dot(A,B)
# print("Matrix- Vector Multiplication\n", result)

# print("Identity Matrix \n", np.eye(3))

# Determinant of a matrix 
C = np.array([[1,2],[3,4]])
determinant = np.linalg.det(C)
print ("Determinant :",determinant)

d = np.diag([1,2,4,8])
print("Diagonal matrix \n", d)