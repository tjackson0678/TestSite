import matplotlib.pyplot as plt
import numpy as np

x = ['1','2','3','4']
y1 =  [0,26,168,634]
y2 =  [0,4,4,4]

plt.plot(x,y1, color='blue', label='Special Multiply/Divide')
plt.plot(x,y2, color='red', label='Regular Multiply/Divide')
plt.ylabel('Run-Times (10^-6 ms)')
plt.xlabel('Iterations')
plt.title("Run-Times C Program Chart")

plt.legend()
plt.savefig("ECGR5100_FinalProj.pdf")
plt.show()