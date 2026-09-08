import pandas as pd
import numpy as np
dates = pd.date_range('20260829',periods=6)
df = pd.DataFrame(np.arange(12,36).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df['A'])
print(df.A)
print(df[0:3])
print(df.loc['20260829'])#select by label
print(df.loc[:,['A','B']])#:表示所有行的数据
print(df)
print(df.iloc[3])#select by position第三行
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3],1:4])
print(df[df.A > 20])
print(df['A'][df.A > 25])#只能选择列