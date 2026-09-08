import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left,right,on='key')
print(res)
left1 = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right1 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})
res1 = pd.merge(left1,right1,on=['key1','key2'])#默认是how='inner'
res2 = pd.merge(left1,right1,on=['key1','key2'],how='outer',indicator=True)
print(res1)
print(res2)#indicator告诉你怎么merge的

# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                     'A': ['A0', 'A1', 'A2', 'A3'],
#                     'B': ['B0', 'B1', 'B2', 'B3']})

# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                      'C': ['C0', 'C1', 'C2', 'C3'],
#                      'D': ['D0', 'D1', 'D2', 'D3']})
# res3 = pd.merge(left,right,)
boys = pd.DataFrame({'k':['k0','k1','k2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['k0','k1','k2'],'age':[4,5,6]})
res3 = pd.merge(boys,girls,on='k',suffixes=['_boys','_girls'],how='inner')
print(boys)
print(girls)
print(res3)