import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)
y1 = 2*x+2
plt.figure(edgecolor="Red")
plt.plot(x,y1,color="Red")
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#annotation
x0 = 0.5
y0 = 2*x0 + 2
plt.scatter(x0,y0,s=50,color='purple')
#plt.plot([x0,x0],[y0,0],color='black',linestyle='--',lw=2.5)#连接点(x0,y0)到(x0,0)
#简写
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
plt.annotate(r'$2x+2=%s$'% y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
            fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.text(-0.5,0.75,'$This\\ is\\ data.\\mu\ \\sigma_i$',fontdict={'size':15,'color':'red'})
plt.show()