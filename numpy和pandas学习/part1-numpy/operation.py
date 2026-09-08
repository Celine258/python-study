import numpy as np
a = np.array([1,2,3,4,5])
b = np.arange(3,8)
c = a + b
print(c)

print(np.sin(a))

print(b < 6)

a2 = np.array([[1,2],
               [3,4]])
b2 = np.arange(7,11).reshape((2,2))


#矩阵的乘法
print(a2)
print(b2)
print(np.dot(a2,b2))
print(a2.dot(b2))

print(np.sum(a2,axis=1))#axis=0求列的和，1求行的和
print(np.sum(a2))
print(np.min(a2,axis=0))
print(np.max(a2))

a3 = np.arange(2,14).reshape((3,4))
print(a3)
print(np.argmax(a3))#求出最大值的索引
print(np.argmin(a3))#求出最小值的索引
print(np.mean(a3))#求出平均值，average也可以
print(a3.mean())#不可用average
print(np.average(a3))

print(a3)

print(np.median(a3))#求中位数
#print(a3.median())不可用

print(np.cumsum(a3))#累加
print(np.diff(a3))#累差
print(np.nonzero(a3))#找出非零元素
a4 = np.arange(14,2,-1).reshape((3,4))
print(a4)
print(np.sort(a4))#逐行进行排序

print(a4)
print(np.transpose(a4))#矩阵的转置
print(a4.transpose().dot(a4))

print(np.clip(a4,5,9))#矩阵的裁剪