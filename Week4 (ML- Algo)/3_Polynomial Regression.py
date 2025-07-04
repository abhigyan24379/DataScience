# Polynomial Regression 
# - polynomial regression is an extension of linear regression thet models the relationship b/w the input features and the target 
#   variable as an nth-degree polynomial. it can capture non-linear relationship in the data by adding polynomial terms to the feature 

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np 

x = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([45000,50000,60000,80000,110000,150000,200000,300000,400000,450000])

x_train , x_test , y_train , y_test = train_test_split(x,y ,test_size=0.2, random_state=42 )

# Transforming feature into polynomial feature 
poly = PolynomialFeatures(degree=2) #degree determine the polynomial components 
x_train_poly = poly.fit_transform(x_train) # this will transform the feature into polynomial feature s
x_test_poly = poly.transform(x_test)

# Initialize and train the model 
model = LinearRegression()
model.fit(x_train_poly , y_train)

y_pred = model.predict(x_test_poly)

# Evaluate the model 
mse = mean_absolute_error(y_test, y_pred)


print  ("Mean Squared error :",mse)
print ("predicated values : ", y_pred)







































