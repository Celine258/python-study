import numpy as np
import pandas as pd
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])
print(df1)
print(df2)
print(df3)
results = pd.concat([df1,df2,df3],axis=0)#0为竖向
print(results)
print("索引不对")
results1 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(results1)

df4 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'],index=['1','2','3'])
df5 = pd.DataFrame(np.ones((3,4))*1,columns=['E','F','C','D'],index=['2','3','4'])
results2 = pd.concat([df4,df5],axis=0,join='outer')#默认的join模式outer
results3 = pd.concat([df4,df5],axis=1)
results4 = pd.concat([df4,df5],axis=1,join='inner')#只会找都有的部分
print(results2)
print(results3)
print(results4)
