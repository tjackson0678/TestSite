import pandas as pd
import numpy as np

# creat a simple dataset of people
df = pd.read_csv('python/ECGR5105/D3.csv')
#print(df.head())

theta0 = 0.5
theta1 = 0.5
learn_rate = 0.1

#compute prediction
def pred(theta0, theta1, x):
    ans = theta0 + theta1*x
    return ans 

def compute_mse(theta, x, y):
    m = len(y)
    t0_total = 0
    t1_total = 0

    #compute gradient wrt theta0
    for r in range(0, m): 
        t0_total += ((pred(theta0, theta1, x[r]) - y[r])) 
        #compute gradient wrt theta1
        t1_total += ((pred(theta0, theta1, x[r]) - y[r])*x[r]) 
    t0_cost = (1/m) * t0_total 
    t1_cost = (1/m) * t1_total 

    cost = [t0_cost, t1_cost]
   
    return cost



print("Compute_mse X1: ", compute_mse(theta0,df.X1, df.Y))
print("Compute_mse X2: ", compute_mse(theta0,df.X2, df.Y))
print("Compute_mse X3: ", compute_mse(theta0,df.X3, df.Y))

#print("First round of data: ", pred(theta0, theta1, df.X1[2]))