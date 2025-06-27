import numpy as np 

#generate synthetic data 
np.random.seed(32)
x = 2 * np.random.rand(100,1)
y = 4 + 3 * x + np.random.randn(100,1)

# Add bias term to X
X_b = np.c_[np.ones((100,1)), x]

# SGD implementation 
def SGD(x,y,theta,learning_rate , n_epocs):
    m = len(y)
    for  epoch in range (n_epocs):
        for i in range (m):
            random_index = np.random.randint(m)
            xi = x[random_index : random_index+1]
            yi = y[random_index : random_index+1]
            gradients = 2 * xi.T @(xi @ theta -yi )
            theta -= learning_rate *gradients
    return theta

# initilize parameters 
theta = np.random.randn(2,1)
learning_rate = 0.01
n_epochs = 50 
# perfom SGD 
theta_opt = SGD(X_b, y, theta, learning_rate, n_epochs)  
print ("optimized parameters \n ", theta_opt)    



