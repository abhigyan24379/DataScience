import numpy as np 

arr = np.array([1,2,3,4,])
# print (arr)

zeroes = np.zeros((3,3))
# print (zeroes)

ones = np.ones((2,4))
# print (ones)

range_array = np.arange(1,10,2) # create an array with an  interval of 2 from 1 to ten we can 
#even change the difference and increase or decrease the ranges 

#print (range_array)



#numpy.linspace is a function in Python's NumPy library 
# that generates an array of evenly spaced numbers over
# a specified interval. It is a fundamental tool for various 
# numerical and scientific computing tasks, including data 
# visualization, simulations, and algorithm development
linspace_array = np.linspace(0,10,5)
# print(linspace_array)

# arr = np.array([1,2,3,4,5,6])
# reshaped = arr.reshape([2,3])
# print (reshaped)
# print(arr)

arr= np.array([1,2,3])
expended = arr[: , np.newaxis]
# print(expended)

a = np.array([1,2,3])
b = np.array([4,5,6])

# print (a+b)
# print (a*b)
# print (a/b)


array = np.array([1,2,3,4])
# print(np.sqrt(arr))
# print (np.mean(array))
# print (np.max(array))

array1 = np.array([10,20,30,40,50 ])
print(array1[2])
print(array1[-1])
print(array1[1:4])
print(array1[3:])
