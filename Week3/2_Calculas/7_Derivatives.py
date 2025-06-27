# # Introduction to derivtives
# # sympy is used for symbolic computation and math is used for numberical computation 

import sympy as sp 
# # import math as m
# x = sp.Symbol('x')
# f = x**2
# derivative = sp.diff(f,x)
# print("Derivatives: ", derivative)

# y = sp.sin(x)
# derivative1 = sp.diff(y, x)
# print ("Sin derivative ", derivative1)


# #Partial derivative

x, y = sp.symbols('x y')
f = x**2 + y**2
grad_x = sp.diff(f,x)
grad_y = sp.diff(f,y)

print ("partial derivativesd : ", grad_x,grad_y)


# Gradient Descent optimization Algorithm 
# what is gradient descent 
# - iterative optimization algorithm used to minimize a function 
# - updates parameters in the direction of the negative gradient to find the munimum 

# update Rules: 0 = 0 - α∇f(0)
#  - 0: Parameters of the model
#  - α: Learning rate (step size)

# Why is gradient descent important in machine learning
# --> Gradient descent is important in machine learning because it is the core 
# algorithm used to optimize model parameters by minimizing a loss function, 
# which measures how well the model performs



