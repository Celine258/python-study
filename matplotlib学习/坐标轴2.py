import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)
y1 = 2*x+2
y2 = 2**x
# plt.figure(edgecolor="Red")
# plt.plot(x,y1,color="Red")

plt.figure(num=3,figsize=(8,5))
#gca = get current axis
plt.xlim((-1,2))
plt.xlabel("I am x")
plt.ylim((-1,2))
plt.ylabel("I am y")
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-1,0,1,2],[r'$bad$',r'$narmal$',r'$not\ bad$','perfect'])#可以改变字体,可以\alpha来打出希腊字母
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.plot(x,y2)
ax.xaxis.set_ticks_position('bottom')#把底部的边界设置为x轴
ax.yaxis.set_ticks_position('left')#把底部的边界设置为x轴
ax.spines['bottom'].set_position(('data',0))#纵坐标的-1就是横坐标的位置
ax.spines['left'].set_position(('data',0))#axes定位到y的百分之多少位置,ourward
plt.show()