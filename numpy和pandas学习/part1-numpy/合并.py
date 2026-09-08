import numpy as np
a = np.array([1,2,4])
b = np.array([2,3,5])

c = np.vstack((a,b))#vertical stack
print(a.shape,c.shape)
d = np.hstack((a,b))#horizontal stack
f = np.concatenate((a,b,a,b),axis=0)#concatenate拼接,axis=0为纵向合并，1为水平合并
print(f)

print(c)
print(d)
print(a)
print(a[np.newaxis,:].shape)
print(a.transpose())
print(a[np.newaxis,:].transpose())#给横向加一个维度
print(a[:,np.newaxis])#给纵向加一个维度
