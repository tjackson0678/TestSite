import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Get current and running directory
running_directory = os.path.dirname(os.path.abspath(__file__))

# create a simple dataset of people
df = pd.read_csv('python/ECGR5105/D3.csv')

theta0 = 0
theta1 = .5
learn_rate = 0.06

# File name and path
file_name = "regressionModel.pdf"
file_path = os.path.join(running_directory, file_name)

#compute prediction
def pred(theta, x):
    ans = theta0 + theta*x
    return ans 

def compute_mse(theta, x, y):
    m = len(y)
    t0_total = 0
    t1_total = 0

    #compute gradient wrt theta0
    for r in range(0, m): 
        t0_total += ((pred(theta, x[r]) - y[r])) 
        #compute gradient wrt theta1
        #t1_total += ((pred(theta, x[r]) - y[r])*x[r]) 
        
    cost = (1/m) * t0_total 
    #t1_cost = (1/m) * t1_total
   
    return cost

# Gradient Descent Function
def gradient_descent(X, y, learning_rate, iterations):
    m = len(y)
    theta = theta1 # Initialize parameters
    cost_history = []

    #tmp0 = compute_mse(theta, X, y)

    for i in range(iterations):
        gradients = compute_mse(theta, X, y) #(1/m) * X.T.dot(X.dot(theta) - y)
        theta -= learning_rate * gradients
        cost_history.append(compute_mse(theta, X, y))

    return theta, cost_history


# Interactive visualization of learning rates
def plot_gradient_descent(learning_rate):
    iterations = 50
    _, cost_history = gradient_descent(df.X1, df.Y, learning_rate=learning_rate, iterations=iterations)
    _, cost_history_2 = gradient_descent(df.X2, df.Y, learning_rate=0.05, iterations=iterations)
    _, cost_history_3 = gradient_descent(df.X3, df.Y, learning_rate=0.08, iterations=iterations)

    
    plt.figure(figsize=(8, 5))
    plt.plot(range(iterations), cost_history, label=f'X1 Learning Rate: {learning_rate}', color='blue')
    plt.plot(range(iterations), cost_history_2, label=f'X2 Learning Rate: {0.05}', color='red')
    plt.plot(range(iterations), cost_history_3, label=f'X3 Learning Rate: {0.08}', color='green')
    plt.xlabel('Iterations')
    plt.ylabel('Cost Function')
    plt.title('Effect of Learning Rate on Gradient Descent Convergence')
    plt.legend()
    plt.grid()
    plt.savefig(file_path)

    #plt.show()


theta_opt, cost = gradient_descent(df.X1, df.Y, learning_rate=learn_rate, iterations=30)
print("Optimized X1 Theta:", theta_opt)
print("cost at optimized theta: ",cost[-1], "\n")

theta_opt, cost = gradient_descent(df.X2, df.Y, learning_rate=.05, iterations=30)
print("Optimized X2 Theta:", theta_opt)
print("cost at X2 optimized theta",cost[-1], "\n")

theta_opt, cost = gradient_descent(df.X3, df.Y, learning_rate=.08, iterations=30)
print("Optimized X3 Theta:", theta_opt)
print("cost at X3 optimized theta",cost[-1], "\n")

plot_gradient_descent(learn_rate)
