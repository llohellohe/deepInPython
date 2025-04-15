import asyncio

import requests
import time


def req(url):
    text=requests.get(url).text
    return text

print(req("http://httpbin.org/get"))

async def print_hello():
    now = time.time()
    await asyncio.sleep(1)
    print(time.time() - now)
    print("Hello, world!")
    await asyncio.sleep(1)
    print(time.time() - now)

coro=print_hello()
print(coro) #<coroutine object print_hello at 0x10e7c8ac0>
print(print_hello) #<function print_hello at 0x10e825e10>
print(coro.__class__) #<class 'coroutine'>

asyncio.run(coro)


def normal_hello_world():
    now=time.time()
    time.sleep(1)
    print(time.time() - now)
    print("Hello, world!")
    time.sleep(1)
    print(time.time() - now)
now = time.time()
normal_hello_world()
normal_hello_world()
normal_hello_world()
print(f"Total time for running 3 normal function: {time.time() - now}")


## use coroutine
async def main():
    await asyncio.gather(print_hello(), print_hello(), print_hello())

now = time.time()
asyncio.run(main())
print(f"Total time for running 3 coroutine: {time.time() - now}")

