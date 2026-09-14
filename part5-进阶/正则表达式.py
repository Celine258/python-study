import re
s = "python itheima"
result = re.match("python",s)
print(result)
# print(result.span())
# print(result.group())
s1 = "1python itheima"
result1 = re.search("python",s1)
print(result1)

s2 = "python itheima python python world"
result3 = re.findall("python",s2)
result4 = re.findall("celine",s2)
print(result3)
print(result4)