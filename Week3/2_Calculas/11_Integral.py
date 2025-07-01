import sympy as sp

x= sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f,(x,0,2))
indefinite_integral = sp.integrate(f,x)
print("Defiinite Integral is: ", definite_integral)
print("Indefiinite Integral is: ", indefinite_integral)

#optimization concepts 
# Local vs Global Minima
# --> loacal Minimum
# --> Global Minimum
# Convex Functions
# --> f(λx1 + (1 - λ)x2) ≤ λf(x1) + (1 - λ)f(x2)   for all lamda [0,1]

# Non-Convex Function in ML
# --> Most neural Network loss function 
 
# Stochastic Gradient Descent (SGD) and its variants 
# What is stochastic Gradient Descent?
# --> optimization algorithm that uses random subsets (mini-batches )of the data to compute 
#     gradients and update parameters 

# Why use SGD?
# --> SGD is used for faster convergence for large data sets compared to batch gradient descent 

# Variants of SGD
# --> Mini-Batch SGD - we have mini batch SGD which update parametes using small batches intead of single example 
# --> momentum - Which adds a fraction of the previous update to the current to accurate 
# --> Adam optimizer - it combines momentumwith adaptive lerning rates for faster convergence 

