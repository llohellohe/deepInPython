import math

print("hello world !")
姓="诸葛"
名="亮"
字="孔明"

print(f"姓名:{姓}{名},字:{字}")

import keyword
print(keyword.kwlist)

# 注释

"""
双引号注释
"""

'''
单引号注释
'''

var1=1
var2=2
var3=3

var4=var1+var2+var3

var4=var1+\
    var2+\
    var4

print(var4)

str1="this is a line with \n new line"
print(str1)

str2=r"this is a line with \n new line"
print(str2*3)
print(str1+str2*2)

num="123456789"
print(num[0:-1])

x=10
y=11.2
z="Alex"
ok=True

print(type(x))
print(type(y))
print(type(z))
print(type(ok))
print(ok)
print(not ok)
print(True or False)
print(True and False)

if ok:
    print("ok!")

if not ok:
    print("not ok!")
else:
    print("ok!!")

list=[1,2,3,"hello",字,名]
list.append("hi")
print(list[4])

for item in list:
    print(item)

tuple=(1,2,3)
for item in tuple:
    print(item)


sites = {'Google', 'Google','Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
sites.add("Bing")

if "Bing" in sites:
    print("Bing in")

if "Bing2" not in sites:
    print("Bing2 not in")

for item in sites:
    print(item)

x = b"hello"
y=x[1:3]
print("bytes is")
print(x[0])
print(chr(x[0]))
print(x[1])
print(chr(x[1]))

z = int("3")
print(z)

z=str(z)
print(z)

if (n:=100)>10:
    print("> 10 ok")


print("\a")

print("Hello\rWorld!")
print('google runoob taobao\r123456')

import time

for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
   # time.sleep(0.05)
print()

w = {'name': 'kongming', 'url': 'www.kongming.com'}

w1=f'{w["name"]}: {w["url"]}'
w2=f"{w['name']}: {w['url']}"

print(len(w1))
print(w2)


list.append("add site")
print(list)

del list[0]
print(list)

d={'name':'o2'}
d['age']=20
print(d)

s={1,2,3,4,5}
s.add(11)
print(s)

if(len(s)>4):
    print("size > 4")
elif(len(s)<4):
    print("size < 4")
else:
    print("size == 4")

print(math.pi)