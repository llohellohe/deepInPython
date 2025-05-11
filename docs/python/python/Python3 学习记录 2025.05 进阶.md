# str和repr函数
```
class Adv:  
    def __init__(self,campaign):  
        self.campaign = campaign  
  
    def __str__(self):  
        return f'camp:{self.campaign}'  
    def __repr__(self):  
        return f'Ad camp:{self.campaign}'  
a=Adv('Google')  
print(a)


__str__ 用于print输出时，用户友好的字符串表达
__repr__ 用于程序员使用，典型场景是在调试时，对象直接显示的名字来自于repr

```

# 原始字符串
如果要输出下面的C盘路径，如果不使用r或者R的原始字符串形式，那么就要自己使用反斜杠转义。
```
str_not_raw="C:\\Users\\Admin"  
str_raw=r"C:\Users\Admin"  
  
print(str_not_raw)  
print(str_raw)
```

字符串.join
```
t = ('我', '喜', '欢', '你')  
  
print("".join(t))
```
最终返回用空字符串连接起t的一个字符串“我喜欢你”
# Pandas
两个重要的数据结果
1. Series:列，类似list，具备索引等功能
2. DataFrame，多个Series组成，即多列组成的二维表格


# defaultdict
1. 默认的dict，若访问字典中的key值不存在时会报KeyError错误，这时候就可以使用defaultdict类来避免这种错误。
2. 参考文章：https://blog.csdn.net/u014248127/article/details/79338543

# Counter
1. 统计列表、元组等可迭代对象的次数
2. https://blog.csdn.net/Flag_ing/article/details/124026747
3. https://zhuanlan.zhihu.com/p/355601478
4. 继承了dict类，可以像dict那样使用
```
from collections import defaultdict,Counter  
  
lst = ['A', 'B', 'C', 'D', 'e','A','A']  
dic = {}  
  
#for i in lst:  
    #dic[i] += 1#print(dic)  
  
dict=defaultdict(Counter)  
for i in lst:  
    #dict[i][i] += 1  
    dict[i][i] += 1  
  
dict['A']['AZ']=20  
  
for k,v in dict.items():  
    print("key is {},value is {}".format(k,v))  
  
print("DICT ITEM")  
print(dict['A'])  
  
count=Counter(lst)  
count["hi"]=100  
for k,v in count.items():  
    print(k,v)  
print(count)
```


# 切片
详细教程：https://www.cnblogs.com/xxpythonxx/p/16870945.html
一个完整的切片表达式包含两个“:”，用于分隔三个参数（start_index、end_index、step），当只有一个“:”时，默认第三个参数step=1。

切片操作基本表达式：object[start_index : end_index : step]

- step：正负数均可，其绝对值大小决定了切取数据时的“步长”，而正负号决定了“切取方向”，正表示“从左往右”取值，负表示“从右往左”取值。当step省略时，默认为1，即从左往右以增量1取值。“切取方向非常重要！”“切取方向非常重要！”“切取方向非常重要！”，重要的事情说三遍！
    
- start_index：表示起始索引（包含该索引本身）；该参数省略时，表示从对象“端点”开始取值，至于是从“起点”还是从“终点”开始，则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。
    
- end_index：表示终止索引（不包含该索引本身）；该参数省略时，表示一直取到数据”端点“，至于是到”起点“还是到”终点“，同样由step参数的正负决定，step为正时直到”终点“，为负时直到”起点“。


```
比如 
t = ('我', '喜', '欢', '你')  
print(t[:-1])

-1不包含，代表从第一个到倒数第二个，即‘我’，‘喜’，‘欢’
```

```
tokens[-1:]

首先
* 第三个step参数为非负数，所以顺序为从左到右；
* start为-1,代表从倒数第一个开始，且包含
* end为无，代表按照从左到右的顺序，到最后一个端点
* 所以tokens[-1:]代表为取最后一个元素
```

## #切片 使用切片方式的插入

```
list1 = [1, 3, 11, 2, 4, 4]  
list1[1:3] = ['A','B','C','D']  
print(list1)
# [1, 'A', 'B', 'C', 'D', 2, 4, 4]

list1[1:1]=['A1']
# [1, 'A1', 'A', 'B', 'C', 'D', 2, 4, 4]
```

在list的[1:3]位置范围处，抹去位置上的对应值，插入新的值。
* 假设实际插入的值，比位置元素范围多，则原列表中的后续元素递延
* 假设实际插入的值，比位置元素范围少，则依旧按照原位置元素抹去
* 即最终执行顺序为：
	* 1.先按照位置的start\end删除元素
	* 2.按照具体的新值做插入
* 如果插入的切片为 [start:start]代表在这个位置处，直接插入新值，原来的元素不会被抹除
	* 切片 list[start:start]返回[]列表

```
list1 = [1, 3, 11, 2, 4, 4]  
list1[1:3] = ['A','B','C','D']  
print(list1)
# [1, 'A', 'B', 'C', 'D', 2, 4, 4]

print(list1[-3:-4:-1])  
print(list1[-3:-2:-1])
# [2] ，因为-1 代表start和end顺序变为从右到左，按照-3 到 -4，包含一个元素
# [] ，因为-1 代表start和end顺序变为从右到左，按照-3 到 -2 顺序，不包含任何东西，所以为空
```
# MAX函数
https://blog.csdn.net/u013250071/article/details/118220139
![[Pasted image 20250510144831.png]]

* 可以获得list\tuple等中最大的值
* 可以获得dict中，key最大的值
* 也可以获得dict中,value最大的值，需要使用key=dict.get 参数
* 也可以获得字符串，按照字符出现的个数
```
字符串count函数
s1 = "AAAccBBe"  

# S1中，最大的字符
print(max(s1))  
# S1中，出现次数最多的字符
print(max(s1, key=s1.count))  
print(s1.count('B'))
# S1中B出现的次数
```

通过 Counter 类也可以给字符串计数
```
s1 = "AAAccBBe"  
print(Counter(s1))

# Counter({'A': 3, 'c': 2, 'B': 2, 'e': 1})
```


# 推导式的用法
```
corpus = ["我特别特别喜欢看电影",  
          "这部电影真的是很好看的电影",  
          "今天天气真好是难得的好天气",  
          "我今天去看了一部电影",  
          "电影院的电影都很好看"]  
import jieba  
  
corpus_tokenized = [list(jieba.cut(sentence)) for sentence in corpus]  
print(corpus_tokenized)
```

通过推导式，创建一个新的包含list的list