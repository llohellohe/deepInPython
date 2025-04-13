num_list = list(range(10))
print(num_list)

for i in num_list:
    print(i)
else:
    print("finished")


def function1(arg1):
    print(f"function1:{arg1}")
    return arg1

f=function1("city")

def function2(arg1,*var_args):
    print(f"arg1:{arg1}")
    print(type(var_args))
    print(var_args)

function2(1)
function2(1,2)
function2(1,2,3)

def function3(arg1,**var_args):
    print(f"arg1:{arg1}")
    print(type(var_args))
#    print(var_args['a'])
#    print(var_args['b'])
    print(var_args)
    if('a' in var_args):
        print("here")
        print(var_args['a'])

function3(1)
function3(1,a=2)
function3(1,a=2,c=3)


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)

print(product)  # 输出：120

## 装饰器函数

def monitor(func):
    def wrapper(*args, **kwargs):
        print("starting")
        func(*args, **kwargs)
        print("finished")
    return wrapper

@monitor
def say_hello(name):
    print(f"hello{name}")

say_hello("guy")


## 类装饰器

def class_monitor(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
        def display(self):
            print("monitor start")
            self.wrapped.display()
            print("monitor end")
    return Wrapper

@class_monitor
class   MyClass:
    def display(self):
        print("MyClass display")

obj=MyClass()
obj.display()


