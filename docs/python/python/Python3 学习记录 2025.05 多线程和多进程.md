
```
def upload_file():  
    print("start upload")  
    count = 0  
    while count < 5:  
        print(f"start upload file {count}")  
        print(threading.current_thread())  
        count += 1  
        time.sleep(1)  
  
  
try:  
    threading.Thread(target=upload_file, name="Thread--1").start()  
    threading.Thread(target=upload_file, name="Thread--2").start()  
except Exception as e:  
    print(e)  
  
print(f"TOTAL THREAD {threading.enumerate()}")
```

* threading库处理多线程
* Thread定义一个线程，其中target为执行的函数
* start启动线程

# 使用继承Thread类的方式定义
```
class FileUploadThread(threading.Thread):  
    def __init__(self, name, delay):  
        threading.Thread.__init__(self)  
        self.name = name  
        self.delay = delay  
  
    def run(self):  
        print("开始线程：" + self.name)  
        print_time(self.name, self.delay, 5)  
        print("退出线程：" + self.name)  
  
  
def print_time(name, delay, counter):  
    while counter > 0:  
        time.sleep(delay)  
        print("%s: %s" % (name, time.ctime(time.time())))  
        counter -= 1
```

* 继承threading.Thread类
* init函数初始化
* run函数执行具体内容，其中调用的函数不能定义在类里面。

# 加锁
```
  
threadLock = threading.Lock()

threadLock.acquire()  
print_time(self.name, self.delay, 5)  
threadLock.release()
```

threading.Lock
acquire 获得锁、release 释放锁

### 更加优雅的
```
import threading  
  
# 创建一个锁对象  
lock = threading.Lock()  
  
def my_function():  
    with lock:  
        print("线程开始执行")  
        # 在这里编写线程要执行的代码  
        print("线程执行结束")  
  
# 创建线程实例  
thread1 = threading.Thread(target=my_function)  
thread2 = threading.Thread(target=my_function)  
# 启动线程  
thread1.start()  
thread2.start()  
# 等待线程执行完毕  
thread1.join()  
thread2.join()  
print("主线程结束")
```

# 线程优先级队列（ Queue）


# urllib
## parse url
```
def parse_url(url):  
    o = urlparse(url)  
    print(o)  
  
  
# open_page(url="https://www.amazon.co.jp/-/en/dp/B0DJCWG43J/?language=en_US&psc=1&th=1")  
  
parse_url("https://www.amazon.co.jp/-/en/dp/B0DJCWG43J/?language=en_US&psc=1&th=1")
```

## open url
```
def open_page(url):  
    try:  
        page = urlopen(url)  
    except Exception as e:  
        if e.code == 404:  
            print(404)  
  
    print(page.getcode())  
    print(page.read())
```

urlopen后read获得

# 多进程
https://zhuanlan.zhihu.com/p/64702600
需要再仔细研究下