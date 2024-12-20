import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1.75)
y1 =  x**2
y2 =  x + 0
y3 =  x**3 

plt.plot(x,y1, color='blue')
plt.plot(x,y2, color='red')
plt.plot(x,y3, color='green')

plt.savefig("Midterm_Jackson.pdf")
plt.show()
