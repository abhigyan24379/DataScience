# Ridge and lasson Regression 
# - Ridge and lasso Regression are regularization technique applied to linear regression to 
#   Prevent overfitting by penalizing large coefficients:
#       -> Ridge Regression adds an L2 penalty (sum of squared coefficients)
#       -> Lasso Regression adds an L1 penalty (sum of absolute values of coefficients), which 
#           can lead to feature selection by shrinking some coefficients to zero.
from sklearn.linear_model import Ridge , Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np

# Smaple data (house size v house price)
X = np.array([[1400],[1600],[1700],[1875],[1100],[1550],[2350],[2450],[1700],[3200]])
Y = np.array([24000,31200,43220,45009,67665,88008,120000,211100,31220,410000])

x_train ,x_test , y_train, y_test = train_test_split(X,Y , test_size=0.2 , random_state=42)

# Redge Regression 
ridge_model = Ridge(alpha=1.0)  # alpha controls the regularization strength with higher values 
ridge_model.fit(x_train,y_train)
ridge_pred = ridge_model.predict(x_test)
ridge_mse = mean_absolute_error(y_test, ridge_pred)

print ("Ridge Mean Square Error : ", ridge_mse)
print ("Ridge predict : ", ridge_pred)


# Lasso Regression 

lasso_model = Lasso(alpha = 0.1) # alpha controles the regularization strength with larger values, increasing the penalty on the coefficient 
lasso_model.fit(x_train,y_train)
lasso_pred = lasso_model.predict(x_test)
lasso_mse = mean_absolute_error(y_test,lasso_pred)

print ("Lasso Mean Square Error : ", lasso_mse)
print ("Lasso predict : ", lasso_pred)


































 
 
 