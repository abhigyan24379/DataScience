import numpy as np 

# Dataset 
data = [10,20,30,40,50]

#calculate stats 
mean = np.mean(data )
variance = np.var(data)
std_dev = np.std (data)

print("mean",mean)
print("Variance", variance)
print("std deviation ", std_dev)
