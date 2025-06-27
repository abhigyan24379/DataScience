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


