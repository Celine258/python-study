import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)
y1 = 2*x+2
y2 = 2**x
plt.figure(edgecolor="Red")
plt.plot(x,y1,color="Red")

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)


plt.show()