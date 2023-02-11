import numpy as np
import matplotlib.pyplot as plt 

x=np.arange(8)
y1=4*x+5
y2=3*x+5
y3=2*x+5
y4=x+5

plt.plot(x,y1,label="4x+5")
plt.plot(x,y2,label="3x+5")
plt.plot(x,y3,label="2x+5")
plt.plot(x,y4,label="x+5")

plt.title("Plot Mutiple lines in Matplotlib",fontsize=15)
plt.xlabel("X",fontsize=13)
plt.ylabel("Y",fontsize=13)
plt.legend()
plt.show()