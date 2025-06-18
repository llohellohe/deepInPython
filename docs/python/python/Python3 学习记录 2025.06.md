# Queue
## 定义
queue是一种线程安全的队列实现，用于在多线程编程中安全的传递数据。

### 普通queue
q = queue.Queue()

先进先出的

### FILO queue
先进后出，类似于栈

## 优先级队列
```
priority_queue = queue.PriorityQueue()  

priority_queue.put((2, 'Medium priority'))  
priority_queue.put((3, 'High priority'))  
priority_queue.put((1, 'Low priority'))  
priority_queue.put((1, "P1"))  
print(type(priority_queue.get()))  
print(priority_queue.get()[1])  
print(priority_queue.get()[1])  
print(priority_queue.get()[1])  
print(priority_queue.get()[1])
```

put时，放置的是一个元祖 （优先级，具体元素）
get时，使用get()[1]来获得具体的元素

## 常用方法
* ### `get(block=True, timeout=None)`
	* 默认没有元素时会阻塞 timeout秒，timeout没有设置时，无限等待
* ### `qsize()`
	* 队列中的元素大小
* ### `put(item, block=True, timeout=None)`
	* 将 `item` 放入队列。如果 `block` 为 `True` 且队列已满，则等待 `timeout` 秒，直到队列有空闲空间。如果 `timeout` 为 `None`，则无限等待。
* ### `full()`
	* 如果队列已满，返回 `True`，否则返回 `False`。
* ### `empty()`
	* 如果队列为空，返回 `True`，否则返回 `False`。



# logging 模块
https://www.runoob.com/python3/python-logging.html

## 基础用法
导入模块 import logging

日志级别 debug/info/warning/error/critical

通过format可以设置格式，datafmt设置时间格式
```
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
```

## 高级用法
通过getLogger获得日志对象，Handler设置输出对象，Formatter设置日志格式

```
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler("my_logger.log")
file_handler.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录日志
logger.debug("这是一条调试信息")
logger.info("这是一条普通信息")
```

### 日志轮转 
RotatingFileHandler 或者 TimedRotatingFileHandler
```
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=1024, backupCount=3)
logger.addHandler(handler)
```