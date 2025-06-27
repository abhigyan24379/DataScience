import sympy as sp

#define a multivareiable function 

x, y = sp.symbols('x y')
f = x**2 + 3*y**2 - 4*x*y

# compute partial derivatives 
grad_x = sp.diff(f,x)
grad_y = sp.diff(f,y)

print ("Gradient of x: ", grad_x)
print ("Gradient of y: ", grad_y)



