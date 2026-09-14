from 魔法方法 import CompareStr
a = CompareStr("abc")
b = CompareStr("xyz")
c = CompareStr("hello")

print(a)        # 你输入的字符串是abc
print(repr(a))  # CompareStr('abc')
print(len(a))   # 3
print(a == b)   # True
print(a == c)   # False
print(a == 123) # False（加上类型检查后）