import sympy as sp

x= sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f,(x,0,2))
indefinite_integral = sp.integrate(f,x)
print("Defiinite Integral is: ", definite_integral)
print("Indefiinite Integral is: ", indefinite_integral)

