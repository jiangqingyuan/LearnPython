# python websockets全双工通信

## 功能描述

客户端和服务端都可发送或接收数据。发送和接收各作为一个协程，收发分离，异步并发。

##  运行环境

python3.6.8

websockets9.1

## 服务端

```python
import asyncio
import websockets

async def send(websocket):
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        await websocket.send("hello")
        #正常地发送，不会切换到receive()
        print("send hello")


async def receive(websocket):
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        greeting = await websocket.recv()
        #正常地接收，不会切换到send()
        print("receive "+greeting)


async def hello(websocket, path):
        a = asyncio.get_event_loop().create_task(send(websocket))
        b = asyncio.get_event_loop().create_task(receive(websocket))
        #使用create_task()创建task

        await a
        await b
        # ab并发
        # ab并发，下面这行代码不会执行
        print("wait")
        #print("wait")不会执行

start_server = websockets.serve(hello, "localhost", 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

## 客户端

```python
import asyncio
import websockets

async def send(websocket):
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        await websocket.send("hello")
        #正常地发送，不会切换到receive()

        print("send hello")


async def receive(websocket):
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        greeting = await websocket.recv()
        #正常地接收，不会切换到send()
        print("receive"+greeting)


async def hello():
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        a = asyncio.get_event_loop().create_task(send(websocket))
        b = asyncio.get_event_loop().create_task(receive(websocket))
        await a
        await b
        # ab并发，下面这行代码不会执行
        print("wait")
        #print("wait")不会执行

asyncio.get_event_loop().run_until_complete(hello())
```

# LearnPython
