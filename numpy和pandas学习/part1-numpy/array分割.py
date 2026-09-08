import numpy as np
a = np.arange(12,24).reshape((3,4))
b = np.arange(12,24).reshape((4,3))
print(a)
#等量分割
print(np.split(a,2,axis=1))#按行去分割，分割成左右两个部分
print(np.split(b,2,axis=0))#按列去分割，分割成上下两个部分
#当然首先需要保证可以分成
#要改变什么就去输入什么，0代表列，1代表行
#不等量分割
print(np.array_split(a,2,axis=0))
print(np.vsplit(a,3))
print(np.hsplit(a,2))