import matplotlib.pyplot as plt
import numpy as np
import os

# Get current and running directory
running_directory = os.path.dirname(os.path.abspath(__file__))
current_directory = os.getcwd()
#print("PWD: ", current_directory, "\n", "Running dir: ", running_directory)

# File name and path
file_name = "latencyTimeGraph.pdf"
file_path = os.path.join(running_directory, file_name) 

x = ['06:00','10:00','14:00','18:00','20:00']
y1 =  [12.949,13.125,30.162,12.698,12.733]
y2 =  [21.560,22.794,22.273,21.868,153.594]


plt.plot(x,y1, color='blue', label='West (stanford.edu)')
plt.plot(x,y2, color='red', label='East (unc.edu)')
plt.ylabel('Avg RTT (ms)')
plt.xlabel('Time of Day')
plt.title("UNC and Stanford RTT")

plt.legend()
plt.savefig(file_path)
