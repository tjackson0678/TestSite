import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split

# Get current and running directory
running_directory = os.path.dirname(os.path.abspath(__file__))

# create a simple dataset of people
df = pd.read_csv('python/ECGR5105/Energy.csv')


Y = df.Y1.values
X1 = df.drop(columns=['Y2', 'Y1'])
X = X1.values


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.20, random_state=0)

# Feature scaling to scale data between 0 and 1.
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

def min_max_normalize(data):
  min_val = np.min(data) + .00000001
  max_val = np.max(data)
  return (data - min_val) / (max_val - min_val)


## Normalize the data 
Y_train = min_max_normalize(Y_train)
Y_test = min_max_normalize(Y_test)

# Import Logistic Regrsession and train the model on the training data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
classifier = LinearRegression()
classifier.fit(X_train, Y_train)

# Now predict the target for the test data
Y_pred = classifier.predict(X_test)

# Evaluate the classifier performance in terms of MSE, RMSE, and R2
def rmse_sklearn(actual, predicted):
  """Calculates RMSE using scikit-learn."""
  return np.sqrt(mean_squared_error(actual, predicted))

# Plots actual vs. predicted values.
def plot_predictions(actual, predicted):
  plt.figure(figsize=(8, 6))
  plt.scatter(actual, predicted)
  plt.xlabel("Actual Values")
  plt.ylabel("Predicted Values")
  plt.title("Actual vs. Predicted Values")
  
  # Add a diagonal line for reference
  min_val = min(min(actual), min(predicted))
  max_val = max(max(actual), max(predicted))
  plt.plot([min_val, max_val], [min_val, max_val], 'r--') # Dashed red line
  
  plt.grid(True)
  plt.show()

print("MSE: ", 1 - mean_squared_error(Y_test, Y_pred))
print(f"RMSE: ", 1 - rmse_sklearn(Y_test, Y_pred))
print("R2: ", r2_score(Y_test, Y_pred))

#Display the plotted predictions 
plot_predictions(Y_test, Y_pred)

## Second model for predictiosn    

# Round to nearest integer
Y_train2 = np.round(Y_train) 
Y_test2 = np.round(Y_test)

from sklearn.naive_bayes import GaussianNB
classifier_GNB = GaussianNB()
classifier_GNB.fit(X_train, Y_train2)

# Now predict the target for the test data
Y_pred_GNB = classifier_GNB.predict(X_test)

print("MSE: ", 1 - mean_squared_error(Y_test2, Y_pred_GNB))
print("RMSE: ", 1 - rmse_sklearn(Y_test2, Y_pred_GNB))
print("R2: ", r2_score(Y_test2, Y_pred_GNB))

#Display the plotted predictions 
plot_predictions(Y_test2, Y_pred_GNB)
