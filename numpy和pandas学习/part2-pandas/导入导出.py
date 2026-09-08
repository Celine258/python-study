import pandas as pd
import numpy as np
#read_csv,read_pickle,read_excel
#to_csv,to_
data = pd.read_csv("D:/Python学习/numpy和pandas学习/part2-pandas/练习1.csv")
print(data)
print(data[data['age'] > 20])
data1 = data[data['age'] > 20]
data1.to_pickle("student.pickle")