import numpy as np
a = np.arange(12,24).reshape((4,3))
print(a)
print(a[1])
print(a[0][0])
print(a[1,2])
print(a[:,1])#求第一列的数
print(a[0:1,2])#求第零行第一列到第二列之间的数，即(0,2)
for row in a:#默认是行
    print(row)
    print("\n")

for column in a.transpose():#把a转置就可以得到列了
    print(column)
    print("  ")

print(a.flatten())

for item in a.flatten():#提取出每一个元素
    print(item)