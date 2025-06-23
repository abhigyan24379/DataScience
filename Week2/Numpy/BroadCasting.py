import numpy as np

#aray and scalar broadcasting 

# arr = np.array([1,2,3])
# print(arr + 10)  # this adds 10 to all the values of array this is array broadcasting 

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9,]])

# vector = np.array ([1,0,1])
# print (matrix + vector)

#aggrigation fucntion 

# arr = np.array([[1,2,3],[4,5,6]])
# print("sum" , np.sum(arr))
# print("mean" , np.mean(arr))
# print("max" , np.max(arr))
# print("min" , np.min(arr))
# print("Standard deviatin" , np.std(arr))
# print("sum along the row " , np.sum(arr , axis=1))
# print("sum along the column " , np.sum(arr , axis=0))

#boolean indexing and filtering 
# arr = np.array([1,2,3,4,5,6])

# even = arr[arr % 2 == 0]
# print ("even", even)

# arr[arr> 3] = 0
# print("modified Array ", arr) 

#Random NUmber Generation and setting seeds 

np.random.seed(42)

random = np.random.rand(3,3)
print ("random array ", random)

random_int = np.random.randint(0,10,size = (2,3))

print ("random int ", random_int)

