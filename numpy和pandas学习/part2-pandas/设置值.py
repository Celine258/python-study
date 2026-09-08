import numpy as np
import pandas as pd
dates = pd.date_range("20260829",periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[2,2] = 1111
df.loc['2026-09-02','B'] = 2222
df.A[df.A < 5] = 0 
df['F'] = np.nan
print(df)