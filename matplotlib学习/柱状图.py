import matplotlib.pyplot as plt
import numpy as np
n = 12
x = np.arange(n)
y1 = (1 - x/float(n)) * np.random.uniform(0.5,1.0,n)
y2 = (1 - x/float(n)) * np.random.uniform(0.5,1.0,n)
plt.bar(x,y1,facecolor='red',edgecolor='white')
plt.bar(x,-y2,facecolor='blue',edgecolor='white')
plt.xticks(())
plt.yticks(())
plt.xlim(-0.5,n)
plt.ylim(-1.25,1.25)
for a,b in zip(x,y1):
    plt.text(a,b+0.05,'%.2f' % b,ha='center',va='bottom')
for a,b in zip(x,-y2):
    plt.text(a,b-0.05,'%.2f' % b,ha='center',va='top')#ha:horizontal alignment
#ha和va都是对齐方式
plt.show()