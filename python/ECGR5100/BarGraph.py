import matplotlib.pyplot as plt

x =  ['SOTA','Improved']
y = [0.970, 0.985]

plt.bar(x,y,width=0.7)
plt.ylabel('% Accuracy')
plt.yticks([ (x+1)/10.0 for x in range(10)])
plt.title("accuracy of Competing")
plt.savefig("example3.pdf")
