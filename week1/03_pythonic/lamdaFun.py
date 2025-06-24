# A lambda function in Python is a small, anonymous function defined using the 
# lambda keyword. Unlike standard functions defined with def, lambda functions
# do not have a name and are typically used for short, simple operations.
 
 
# add = lambda x, y : x + y
# print (add(3, 4))


#common function are map(), filter, reduce()


# #map() --> applies a function to each item in an iterable
# numbers = [1, 2, 3, 4]
# square = map (lambda x: x**2 , numbers)
# print (list(square))

#filter() --> filters items based on a condition

# even_List = filter(lambda x: x % 2 ==0 , numbers  )
# print (list(even_List))

#reduce() --> reduces an iterable to a single value 

# from functools import reduce

# number = [1, 2, 3, 4]
# product = reduce(lambda x , y:  x * y , number)
# print (product)

# import os

# print (os.getcwd())
# # os.mkdir("text_dir1")
# os.remove("text_dir")

import sys

print (sys.argv)
print(sys.version)
