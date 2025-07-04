# linear regression is a supervised learning algo used for predicting a continuous target 
# variable based on one or more input features it finds the line of best fit (linear relationship)
# by minimizing the sum of a squared differences between the actual and predicted values 


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np 

#sample data (e.g house size vs house price)
X = np.array([[1400],[1600],[1700],[1875],[1100],[1550],[2350],[2450],[1700]])
Y = np.array([24000,31200,43220,45009,67665,88008,120000,211100,31220])

#split the data into training and testing sets
# test_size = 0.2 means 20 percent of the data is used for testing and rest 80 percent is used as training
# random_state = 42 ensures everytime we run the function we get the same split of the data 
X_train , X_test , Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

# Initialize and train the model 
model = LinearRegression() # this creates an instance of the linear regression class which represents s simple linear regression
model.fit(X_train,Y_train) # this trains the model on the training data X_train and Y_train, during this process, the model learns the relationship between house size and price by finding the best fit that minimize the error in predicting Y_Train from XTrain


# make Predictions
y_pred = model.predict(X_test) # this generate prediction for the testing set X_test. The predict method uses the trained model to output estimated house price, which are ypred for the house size in x test 

# Evaluate the model MSE(mean square error)
mse = mean_squared_error(Y_test,y_pred) # this function calculates mean squared error b/w the actual values y_test and the predicated values 

print ("Mean Squared Error : ", mse)
print ("Predicated Values : ", y_pred)




 



