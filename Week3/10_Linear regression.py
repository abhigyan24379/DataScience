import numpy as np 

#define the gradient descent function 
def gradient_descent(x, y, theta, learning_rate , iterations):
    m = len(y)
    for _ in range (iterations):
        predictions = np.dot(x,theta) #dot product of two array
        errors = predictions - y
        gradients = (1/m) * np.dot(x.T, errors)
        theta -=learning_rate * gradients
    return theta

#sampe data 

x = np.array([[1,1],[1,2],[1,3]])
y = np.array([2,2.5,3.5])

theta = np.array([0.1,0.1])
learning_rate = 0.1
iterations = 1000

#perform gradient descent
optimized_theta = gradient_descent(x,y , theta, learning_rate,iterations)
print("optimized Parameters : ",optimized_theta)
        
    
    
    
    
    
    
    