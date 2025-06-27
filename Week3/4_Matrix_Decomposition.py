# What is Matrix Decomposition ?
# --> process of breaking a matrix into simpler components to analyze or solve problem 

# Singular Value Decomposition(SVD)
# -->SVD decompose a matrix 'A' into three matrix : A U.∑.V^T
#    - U: Left singular vector (orthogonal matrix)
#    - ∑: Diagonal matrix of a singular values (non-negative).
#    - V^T: Right singular  vector (ortogonal matrix)


import numpy as np
A = np.array([[2,3],[1,4]])
determinant = np.linalg.det(A)

U, S, Vt = np.linalg.svd(A)
print ("U:\n ", U)
print ("Singular Values : \n", S)
print("V Transpose: \n", Vt)



