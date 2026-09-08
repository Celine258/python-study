import re
r = '^[0-9a-zA-Z]{6,10}$'
s1 = "1234577a"
print(re.findall(r,s1))

r1 = '^[1-9][0-9]{4,10}$'
s2 = "0123456"
s3 = "1234456"
print(re.findall(r1,s2))
print(re.findall(r1,s3))

r2 = r'^[\w-]+(\.[\w-]+)*@(qq|163|gmail)?\.[\w-]+(\.[\w-]+)*$'
qq = "2405679830@qq.com"
print(re.match(r2,qq))
