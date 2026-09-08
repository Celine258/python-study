import numpy as np
import pandas as pd
s = pd.Series([1,2,3,np.nan,44,1])
print(s)

dates = pd.date_range('20260829',periods=6)
print(dates)

data = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(data)
data1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(data1)
print(data1.dtypes)
print(data1.index)
print(data1.columns)
print(data1.values)
print(data1.describe())#只能运算数字
print(data1.T)#转置
print(data.sort_index(axis=1,ascending=False))
print(data.sort_index(axis=0,ascending=False))
