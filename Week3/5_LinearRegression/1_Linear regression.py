import numpy as np 

#data 
np.random.seed(42)
x = 2 * np.random.rand(100,1)
y = 4 + 3 * x + np.random.randn(100, 1)

#Add bias term to feature matrix 

x_b = np.c_[np.ones((100, 1 )),x]

# Initilize parameter 
theta = np.random.randn(2,1)
leaning_rate = 0.1
iteration = 100 




def predict(X,theta):
    return np.dot(X,theta)

def gradient_descent (x,y,theta, learning_rate , iteration):
    m = len(y)
    for _ in range (iteration):
        gradients =(1/m) * np.dot(x.T,(np.dot(x,theta)-y))
        theta -= learning_rate * gradients
    return theta

def mean_square_error(y_true , y_pred):
    return np.mean((y_true - y_pred)**2)

def r_squared (y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1-(ss_res /  ss_tot)


theta_optimized = gradient_descent(x_b, y , theta,leaning_rate,iteration )

y_pred = predict(x_b ,theta_optimized)
mse = mean_square_error(y,y_pred )
r2 = r_squared(y , y_pred)

print("optimized Parameter (Theta ): ", theta_optimized)
print("MSE: ", mse)
print("r2: ", r2)

