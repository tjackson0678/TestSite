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
iterations = 1200;
alpha = 0.09;

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
  cost_history = np.zeros(iterations)

  for i in range(iterations):
    predictions = X.dot(theta)
    errors = np.subtract(predictions, y)
    sum_delta = (alpha / m) * X.transpose().dot(errors);
    theta = theta - sum_delta;
    cost_history[i] = computeCost(X, y, theta)
  return theta, cost_history

Xarray = X.loc[:,['intercept','bathrooms']].values
yarray = y.values
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Bathrooms =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','bedrooms']]
Xarray = X.loc[:,['intercept','bedrooms']].values
yarray = y.values
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Bedrooms =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','stories']]
Xarray = X.loc[:,['intercept','stories']].values
yarray = y.values
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Stories =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','parking']]
Xarray = X.loc[:,['intercept','parking']].values
yarray = y.values
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Parking =', theta)
print('cost_history =', cost_history)

X = df.loc[:,['intercept','area2']]
Xarray = X.loc[:,['intercept','area2']].values
yarray = y.values
theta, cost_history = gradientDescent(Xarray, yarray, theta, alpha, iterations)
print('Final value of theta - Area =', theta)
print('cost_history =', cost_history)