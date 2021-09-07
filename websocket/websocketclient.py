import asyncio
import websockets

async def send(websocket):
    i = 100
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        await websocket.send(str(i))
        #发送，此协程不会挂起

        i += 1
        print("send"+str(i))


async def receive(websocket):
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        greeting = await websocket.recv()
        #接受，此协程不会挂起
        print("receive"+greeting)


async def hello():
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        a = asyncio.get_event_loop().create_task(send(websocket))
        b = asyncio.get_event_loop().create_task(receive(websocket))
        await a
        await b
        # ab并发，后面的两行代码不会执行
        while True:
            print(1)
        #这两行不会运行

asyncio.get_event_loop().run_until_complete(hello())
