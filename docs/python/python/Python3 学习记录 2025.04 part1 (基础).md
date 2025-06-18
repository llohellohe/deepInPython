参考教程：https://www.runoob.com/python3/python3-tutorial.html

# 一、基础语法
1. 可以用中文作为变量名
2. 查看所有保留字
```
import keyword  
print(keyword.kwlist)
```
3. - 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 **r"this is a line with \n"** 则 \n 会显示，并不是换行。
4. - 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# 二、数字(Number)类型

python中数字有四种类型：整数、布尔型、浮点数和复数。

- **int** (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
- **bool** (布尔), 如 True。
- **float** (浮点数), 如 1.23、3E-2
- **complex** (复数) - 复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j

# 三、import 与 from...import

在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *

# 四、数据结构

## list 和tuple
1. 一个用[]，另个用()
2. list可变，tuple不可变
3. 删除一个list元素 del list[2]
4. 指定位置操作
	1. 指定位置插入元素，insert(0,'xx')
	2. 指定位置删除,pop(index)
5. 删除操作
	1. 后续不使用 del list[index]
	2. 后续使用 x=pop(index)
	3. pop()没有index，代表删除最后一个
6. append 增加在末尾

###  排序
sort() 永久排序
sorted()临时排序
reverse()永久改变排序


## Set和Dict
1. 都使用{}初始化
2. set用于存储不重复的值，{}里面的值
3. dict键值对
4. 删除dict某个key,del dict[key]

## bytes
x = b"hello"，字符串变bytes数组
print(x[0])
变为字符：chr(x[0])


## 数据类型可以显示转换
字符串和整数相加会报错，但是可以直接用函数显示转换
z = int("3")
z=str(3)

## 海象运算符
取值的时候，同时返回这个值
if (n:=100)>10:  
    print("> 10 ok")

传统写法
```
# 传统写法  
n = 100  
if n > 10:  
    print(n)
```


## 运算符
1. 成员运算符 in / not in，用户判断是否在集合里
2. 身份运算符 is / is not，用于判断是否引用自同一对象。== 用于判断值是否相同。

# 五、字符串
可以在双引号中引用单引号，也可以反过来
```
w = {'name': 'kongming', 'url': 'www.kongming.com'}  
  
w1=f'{w["name"]}: {w["url"]}'  
w2=f"{w['name']}: {w['url']}"
```

title()方法
*  title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。

# 六、条件控制
1. if，没有else if 只有elif
2. match case，类似switch case
```
def http_error(status):  
    match status:  
        case 400:  
            return "Bad request"  
        case 404:  
            return "Not found"  
        case 418:  
            return "I'm a teapot"  
        case _:  
            return "Something's wrong with the internet"
 其中默认用 case _:  
```
3. 循环，循环结束可以用else
```
for i in num_list:  
    print(i)  
else:  
    print("finished")
```


# 七、函数
```
可变参数的函数，用 * 表示，转化成元组
def function2(arg1,*var_args):  
    print(f"arg1:{arg1}")  
    print(type(var_args))  
    print(var_args)  
  
function2(1)  
function2(1,2)  
function2(1,2,3)
```

```
可变参数的函数，用**表示，转换成dict。输入时，必须带上变量名，如a=2,c=3
def function3(arg1,**var_args):  
    print(f"arg1:{arg1}")  
    print(type(var_args))  
    print(var_args)  
    if('a' in var_args):  
        print("here")  
        print(var_args['a'])  
  
function3(1)  
function3(1,a=2)  
function3(1,a=2,c=3)
```

## return
不带参数值的 return 语句返回 None。

# 八、lambda
Python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 **def** 语句这样标准的形式定义一个函数。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
```
lambda [arg1 [,arg2,.....argn]]:expression

如：
x = lambda a : a + 10
print(x(5))
```

通常和内置的map、filter、reduce等函数一起执行
如：
```
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]
```

filter
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8]  
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
print(even_numbers)  # 输出：[2, 4, 6, 8]
```

reduce
```
from functools import reduce  
  
numbers = [1, 2, 3, 4, 5]  
  
# 使用 reduce() 和 lambda 函数计算乘积  
product = reduce(lambda x, y: x * y, numbers)  
  
print(product)  # 输出：120
```


# 九、数据集合
1. set 空集合只能通过set()来创建，{}创建的是空字典
2. 一个元素的元组，只能通过(x,)来创建；如果只是(x)，括号会被当作运算。
3. update函数
	1. 字典具有update方法，d1.update(d2)，把d2加到d1中
		1. key相同时，会覆盖。
	2. Set也有update函数
4. remove函数
	1. Set中移除指定元素
	2. dict中没有这个函数
	3. tuple不可修改，所以没有这个函数
	4. list中，remove(x)，移除第一个匹配x的;如果不存在，会报错；
5. pop(
	1. Set中随机移除元素
	2. Dict中,pop(key):指定key移除；popitem():删除最后一对key和value
	3. tuple不可修改，所以没有这个函数
	4. list中，pop(index=-1)，移除一个元素，默认最后一个
6. list.append(x) 将x当作一个元素插入到list中
7. list.extend(L) 将L列表内的元素，扩展到list中
8. 字典没有切片操作

# 十、条件控制等
1. match...case
```
case _: 代表默认，类似default
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```

print(b, end=',') 用于将结果输出在同一行，用,分割


# 十一、推导式
![[Pasted image 20250504151425.png]]

![[Pasted image 20250504151554.png]]

Set、Tuple的推导式和列表类似，只是对应的符号不同

# 十二、迭代器和生成器
  
  迭代器
```
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。

next方法可以输出下一个

>>> list=[1,2,3,4]
>>> it = iter(list)    # 创建迭代器对象
>>> print (next(it))   # 输出迭代器的下一个元素
1
>>> print (next(it))
2
>>>


```

生成器
在 Python 中，使用了 **yield** 的函数被称为生成器（generator）。
当在生成器函数中使用 **yield** 语句时，函数的执行将会暂停，并将 **yield** 后面的表达式作为当前迭代的值返回。

```
def countdown(n):
    while n > 0:
        yield n
        n -= 1
 
# 创建生成器对象
generator = countdown(5)
 
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
```

生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。此外，生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。

