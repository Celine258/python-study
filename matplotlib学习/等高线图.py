import matplotlib.pyplot as plt
import numpy as np
def f(x,y):
    return (1 - x /2 + x**5 + y**3) * np.exp(-x**2 - y**2)
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X, Y = np.meshgrid(x,y) 
#use plt.contourf to filling contours
#x,y and value for (x,y) point
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
#use plt.contourf to add contourf lines
C = plt.contour(X,Y,f(X,Y),8,color='black',lw=0.5)#等高线分成8+2份
#adding labels
plt.clabel(C,inline=True,fontsize=10)

plt.yticks(())
plt.xticks(())
plt.show()

