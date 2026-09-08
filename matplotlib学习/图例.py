import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)
y1 = 2*x+2
y2 = 2**x
plt.figure(edgecolor="Red")
line1, = plt.plot(x,y1,color="Red",label='element1')
line2, = plt.plot(x,y2,label='element2')
plt.xlim((-1,2))
plt.xlabel("I am x")
plt.ylim((-1,2))
plt.ylabel("I am y")
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-1,0,1,2],[r'$bad$',r'$narmal$',r'$not\ bad$','perfect'])
#legend图例
# line1, = plt.plot(x,y1,color="Red",label='element1')
# line2, = plt.plot(x,y2,label='element2')
plt.legend(handles=[line1,line2,],labels=['aaa','bbb'],loc='best',)#loc,handles
#handles输入对应的line然后labels来命名不同line的legend名字，不使用原本定义的label
#注意逗号
plt.show()