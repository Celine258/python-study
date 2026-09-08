import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
fig,ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))
def animation1(i):
    line.set_ydata(np.sin(x+i/10))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
#其中一种animation的方式
ani = animation.FuncAnimation(fig=fig,func=animation1,frames=100,init_func=init,interval=20,blit=False)

plt.show()