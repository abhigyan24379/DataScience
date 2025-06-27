import numpy as np

A= np.array([[4,-2],[1,1]])

eigvals , eigvector = np.linalg.eig(A)
print ("Eiven Value ", eigvals)
print ("Eiven Vector ", eigvector)

B = np.array([[3,1,-1],[-1,3,1],[1,1,3]])
U, S, Vt = np.linalg.svd(B)

print ("U:\n ", U)
print ("Singular Values : \n", S)
print("V Transpose: \n", Vt)


#Reconstruct 
Sigma = np.zeros((3,3))
np.fill_diagonal(Sigma , S)
reconstructed = U @ Sigma @ Vt  # '@' this is used for matrix multiplication in python(like the dot product)
print("Reconstructed Matrix \n: ", reconstructed)
