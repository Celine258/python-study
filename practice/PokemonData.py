import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
PkmData = pd.read_csv('D:/Python学习/practice/pokemonData.csv')
#print(PkmData.head())
print("data type:",type(PkmData))
print("data dim:",PkmData.shape)
print(PkmData.dtypes)
print("number of generation:",len(PkmData['Generation'].unique()))
print(PkmData['Generation'].value_counts())
sb.catplot(y = "Generation",data = PkmData,kind = "count")