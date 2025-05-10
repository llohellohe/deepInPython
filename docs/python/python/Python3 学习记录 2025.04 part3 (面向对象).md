# 概念
```
class Team:  
    def __init__(self,team_id,team_name):  
        print(f"team instance is init now {team_id} {team_name}")  
        self.team_id=team_id  
        self.team_name=team_name  
  
    def show_team_name(self):  
        print(f"TEAM NAME IS {self.team_name}")
```

1，每个类初始化实例时会执行 init函数，在这里可以定义一些初始化变量，可以没有类型比较方便。
2，类函数定义时，默认参数必须要有(self),且需要第一个。其中self只是约定，也可以是this等。
3，self代表的是类的实例，self.class代表的是类的名字
4，2个下滑线开头的属性或者方法，声明为私有，不能被外部访问
```
# 私有化属性，不能对外访问  
__private_var=''
```


## global和nonlocal
![[Pasted image 20250504163956.png]]

![[Pasted image 20250504164010.png]]

## 继承
class HouTeam(Team):

1，类定义时，括号里面即为继承的父类
2，括号里面可以有多个父类，按照从左到右的顺序



## 测试
```
def average(values):  
    """Computes the arithmetic mean of a list of numbers.  
  
    >>> print(average([20, 30, 70]))  
    40.0    """    return sum(values) / len(values)  
  
import doctest  
doctest.testmod()
```

会按照doc注释来执行测试


# JSON
序列化成json或者从json反序列化
1,dumps
2,loads
```
data={  
    'id': 1,  
    'name': 'hou',  
    'url': 'https://hou.nba.com'  
}  
  
data_json=json.dumps(data)  
print(data_json)  
  
data2=json.loads(data_json)  
print(type(data2))  
print(data2)
```


## 类和JSON的互转
https://developer.aliyun.com/article/1558264
https://www.cnblogs.com/huzhongqiang/p/17475613.html
使用原始JSON在涉及到类时，可能会报无法序列化的问题，可以使用jsonpickle库
```
json_string = jsonpickle.encode(team, indent=4)  
print(json_string)  
  
team_from_json=jsonpickle.decode(json_string)  
print(team_from_json.show_team_name())

```

类的实例变量定义
![[Pasted image 20250504163253.png]]