import numpy as np
import copy
a = np.arange(4,8)
b = a 
c = a 
print(a)
d = a.copy()#浅拷贝,只复制第一层容器；内部嵌套对象继续共享。
e = copy.deepcopy(a)#深拷贝,递归复制每一层容器，
                    #所有嵌套对象全部新建，完全不共享。
print(c)
print(c is a)
a[0] = 1
print(a)
print(c)#赋值的对象会跟着改变,a,b,c一个变化其他也跟着变化
b[1:3] = [22,33]#左闭右开，改变b[1]和b[2]
print(a)
#想不关联copy
print(d)
print(e)
#a = b 不是复制数组数据，只是复制内存地址（引用）
#.copy()：开辟一块全新内存，完整复制一份数据