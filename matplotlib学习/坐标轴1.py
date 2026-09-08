import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)
y1 = 2*x+2
y2 = 2**x
plt.figure(edgecolor="Red")
plt.plot(x,y1,color="Red",linewidth=1.0,linestyle='--')
plt.xlim((-1,2))
plt.xlabel("I am x")
plt.ylim((-1,2))
plt.ylabel("I am y")
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-1,0,1,2],[r'$bad$',r'$narmal$',r'$not\ bad$','perfect'])#可以改变字体,可以\alpha来打出希腊字母

plt.show()