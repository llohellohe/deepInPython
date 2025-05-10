参考文章：https://zhuanlan.zhihu.com/p/698683843
```
async def print_hello():  
    await asyncio.sleep(1)  
    print("hello")  
  
coro=print_hello()  
print(coro) #1 <coroutine object print_hello at 0x10e7c8ac0>  
print(print_hello) #2 <function print_hello at 0x10e825e10>  
print(coro.__class__) #3 <class 'coroutine'>  
  
asyncio.run(coro)
```

注意点：
1. 用async定义的函数，内部才可以使用await，否则会报编译错误。
2. 用async定义的函数，返回的是一个coroutine ，参考#1；返回的coroutine对象的class是coroutine
3. 函数依旧是个函数。参考#2


coroutine最大的优势在于用单个线程模拟多个线程并发：
```
async def main():  
    await asyncio.gather(print_hello(), print_hello(), print_hello())
```

也可以是
在Python的异步编程中，真正并发的对象是任务（[Task](https://zhida.zhihu.com/search?content_id=243393276&content_type=Article&match_order=1&q=Task&zhida_source=entity)）。当我们对一个Task进行`await`的时候，event loop开始调度当前可执行的全部任务，直到被`await`的Task结束。
```
async def main():
    task1 = asyncio.create_task(async_hello_world())
    task2 = asyncio.create_task(async_hello_world())
    task3 = asyncio.create_task(async_hello_world())
    await task1
    await task2
    await task3
```

