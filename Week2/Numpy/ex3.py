import numpy as np

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# vector = np.array([1,0,-1])

#genereate and filter random dataset
dataset = np.random.randint(1,51,size =(5,5))
print ("original : \n",dataset)

#filter value >25 replace by 0

dataset[dataset >25] =0
print("modified ", dataset)
