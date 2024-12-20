import matplotlib.pyplot as plt
import numpy as np

x = ['06:00','10:00','14:00','18:00','20:00']
y1 =  [12.949,13.125,30.162,12.698,12.733]
y2 =  [21.560,22.794,22.273,21.868,153.594]

plt.plot(x,y1, color='blue', label='West (stanford.edu)')
plt.plot(x,y2, color='red', label='East (unc.edu)')
plt.ylabel('Avg RTT (ms)')
plt.xlabel('Time of Day')
plt.title("UNC and Stanford RTT")

plt.legend()
plt.savefig("ECGR5187_FinalProj.pdf")
plt.show()
