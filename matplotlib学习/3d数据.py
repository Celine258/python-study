import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fg = plt.figure()
#ax = Axes3D(fg)
ax = fg.add_subplot(111,projection="3d")
#X,Y value
x = np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(x,y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('gist_rainbow'))
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='gist_rainbow')
#等高线图压到z轴的-2平面上去
plt.ylim(-2,2)
plt.show()
