import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get current and running directory
running_directory = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(running_directory, 'Housing.csv'))
#df =pd.read_csv('https://raw.githubusercontent.com/satishgunjal/datasets/master/univariate_profits_and_populations_from_the_cities.csv')
#print(df.head()) # To get first n rows from the dataset default value of n is 5


plt.scatter(df.price, df.area, color='red',marker= '+')
plt.grid()
plt.ylabel('Price of home in 1,000s')
plt.xlabel('Area of home in 1000s SqFt')
plt.title('Scatter plot of training data')
#plt.show()

#Lets create a matrix with a dimension of m by 1. m is the number of observations
m = df.price.size

X_0 = np.ones((m, 1))
X_0 = pd.DataFrame(X_0)
X_1 = np.divide(df.price, 100000)
X_1 = pd.DataFrame(X_1)
X_2 = np.divide(df.area, 1000)
X_2 = pd.DataFrame(X_2)
df.insert(0, "intercept",X_0)
df.insert(0, "price2",X_1)
df.insert(0, "area2",X_2)
# print(df.head())


X = df.loc[:,['intercept','bathrooms']]
y = df.price2
theta = np.zeros(2)
iterations = 1200
# use a smaller, safer learning rate to avoid overflow
alpha = 0.01

def computeCost(X,y,theta):
  """
  Compute cost for linear regression.
  Input Parameters
  ----------------
  X : 2D array where each row represent the training example and each column represent
  m= number of training examples
  n= number of features (including X_0 column of ones)
  y : 1D array of labels/target value for each traing example. dimension(1 x m)
  theta : 1D array of fitting parameters or weights. Dimension (1 x n)
  Output Parameters
  -----------------
  J : Scalar value.
  """
  m = len(X)
  predictions = X.dot(theta)
  errors = np.subtract(predictions, y)
  sqrErrors = np.square(errors)
  J = 1 / (2 * m) * np.sum(sqrErrors)
  return J

def gradientDescent(X, y, theta, alpha, iterations):
  """
  Compute cost for linear regression.

  Input Parameters
  ----------------
  X : 2D array where each row represent the training example and each column represent
      m= number of training examples
      n= number of features (including X_0 column of ones)
  y : 1D array of labels/target value for each traing example. dimension(m x 1)
  theta : 1D array of fitting parameters or weights. Dimension ( n x 1)
  alpha : Learning rate. Scalar value
  iterations: No of iterations. Scalar value.

  Output Parameters
  -----------------
  theta : Final Value. 1D array of fitting parameters or weights. Dimension (1 x n)
  cost_history: Conatins value of cost for each iteration. 1D array. Dimansion(m x 1)  """
  # ensure inputs are numpy arrays with float dtype
  X = np.array(X, dtype=float)
  y = np.array(y, dtype=float)
  theta = np.array(theta, dtype=float)

  cost_history = np.zeros(iterations)
  m_local = X.shape[0]

  for i in range(iterations):
    predictions = X.dot(theta)
    errors = predictions - y
    sum_delta = (alpha / m_local) * X.T.dot(errors)
    theta = theta - sum_delta
    cost_history[i] = computeCost(X, y, theta)
    # stop early if numerical issues appear
    if np.any(np.isnan(theta)) or np.any(np.isinf(theta)):
      print(f"Stopping early at iteration {i} due to numerical instability")
      cost_history[i+1:] = np.nan
      break
  return theta, cost_history

Xarray = X.loc[:,['intercept','bathrooms']].values.astype(float)
yarray = y.values.astype(float)
# initialize theta for this model (n features)
theta = np.zeros(Xarray.shape[1])
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Bathrooms =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','bedrooms']]
Xarray = X.loc[:,['intercept','bedrooms']].values.astype(float)
yarray = y.values.astype(float)
theta = np.zeros(Xarray.shape[1])
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Bedrooms =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','stories']]
Xarray = X.loc[:,['intercept','stories']].values.astype(float)
yarray = y.values.astype(float)
theta = np.zeros(Xarray.shape[1])
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Stories =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','parking']]
Xarray = X.loc[:,['intercept','parking']].values.astype(float)
yarray = y.values.astype(float)
theta = np.zeros(Xarray.shape[1])
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Parking =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','area2']]
Xarray = X.loc[:,['intercept','area2']].values.astype(float)
yarray = y.values.astype(float)
theta = np.zeros(Xarray.shape[1])
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Area =', theta)
print('cost_history =', cost_history)



