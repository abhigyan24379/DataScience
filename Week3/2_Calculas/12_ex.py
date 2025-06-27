import sympy as sp 

#define a function 
x = sp.Symbol('x')
f = sp.exp(-x)

#compute indefinite integral 
indefinit_integral = sp.integrate(f,x)  # this is indefinite and if we pass the range it will be definite
print("indefinite integral : " , indefinit_integral)

#compute the dfinite integral 
definite_integral = sp.integrate(f,(x,0,sp.oo))
print ("definite integral : ", definite_integral)

