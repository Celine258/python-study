import numpy as np

a = np.array([2,13,213],dtype=np.int64)
print(a.dtype)

a1 = np.array([[1,2,3],
               [4,5,6]])
print(a1)

a3 = np.zeros((3,4))
print(a3)

a4 = np.ones((3,4))
print(a4)

a5 = np.empty((3,4),dtype=np.int64)
print(a5)

a6 = np.arange(10,20,2).reshape((5,1))
print(a6)

a7 = np.linspace(1,10,20).reshape((4,5))
print(a7)