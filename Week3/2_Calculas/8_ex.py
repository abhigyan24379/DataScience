import sympy as sp

x ,y = sp.symbols('x y')
f = x**2 + x**5 -4
print (sp.diff(f,x))

expanded = sp.expand((x + y)**2)
print (expanded)

intergral = sp.integrate(x**2 , x)
lim = sp.limit(1/x, x, 00)
print (intergral, lim )

expr = x + y 
substituted_expr = expr.subs(x,5)

print (substituted_expr)
