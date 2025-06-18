# 基本概念
## 运行协程
asyncio.run(函数名)

通过这个方法来运行协程

## 定义协程函数 async def
```
async def upload_to_remote():  
    print("Start to upload file to remote")  
    await asyncio.sleep(1)  
    print("Upload finished")

或者
async def main():  
    task = asyncio.create_task(upload_to_remote())  
    await task
```

## 运行多个协程
```
async def run_gather():  
    await asyncio.gather(upload_to_remote(), upload_to_remote(), upload_to_remote())  
  
  
asyncio.run(run_gather())
```


## 超时
设置超时，asyncio.wait_for
```
async def run(timeout):  
    try:  
        await asyncio.wait_for(upload_to_remote(), timeout=3)  
    except asyncio.TimeoutError:  
        print("Timeout error")
```