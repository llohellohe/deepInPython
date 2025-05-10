from collections import Counter

print("字符串计数的集中方法")
list1 = [1, 3, 11, 2, 4, 4]
print(max(list1))

t1 = tuple(list1)
print(max(t1))

s1 = "AAAccBBe"

print(max(s1))
print(max(s1, key=s1.count))
print(s1.count('B'))

print(Counter(s1))

print("切片的插入")

list1 = [1, 3, 11, 2, 4, 4]
list1[1:3] = ['A','B','C','D']
print(list1)

print(list1[1:1])
print(list1[-3:-2])
print("从负数开始")
print(list1[-3:-4:-1])
print(list1[-3:-2:-1])
list1[1:1]=['A1']
print(list1)