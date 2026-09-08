import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data
#Series
# data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# data = data.cumsum()
# data.plot()
# plt.show()

#DataFrame
data1 = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=['A','B','C','D'])
data1 = data1.cumsum()
print(data1.head())
# data1.plot()
#bar,hist,box,kde,area,scatter.hexbin,pie
#plt.scatter()
ax = data1.plot.scatter(x='A',y='B',color="Red",label='class 1')
data1.plot.scatter(x='A',y='C',color="Blue",label='class 2',ax=ax)
#散点图

plt.show()