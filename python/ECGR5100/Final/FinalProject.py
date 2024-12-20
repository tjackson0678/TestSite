import matplotlib.pyplot as plt
import numpy as np
import os

# Get current and running directory
running_directory = os.path.dirname(os.path.abspath(__file__))
current_directory = os.getcwd()
#print("PWD: ", current_directory, "\n", "Running dir: ", running_directory)

# File name and path
file_name = "ProgramClockSpeeds.pdf"
file_path = os.path.join(running_directory, file_name) 

x = ['1','2','3','4']
y1 =  [0,26,168,634]
y2 =  [0,4,4,4]

plt.plot(x,y1, color='blue', label='Special Multiply/Divide')
plt.plot(x,y2, color='red', label='Regular Multiply/Divide')
plt.ylabel('Run-Times (10^-6 ms)')
plt.xlabel('Iterations')
plt.title("Run-Times C Program Chart")

plt.legend()
plt.savefig(file_name)
plt.show()