import asyncio
import websockets

async def send(websocket):
    i = 100
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        await websocket.send(str(i))
        #正常地发送，此协程未挂起

        i += 1
        print("send"+str(i))


async def receive(websocket):
    while True:
        await asyncio.sleep(1)
        #此协程挂起1s，以切换到其他协程。不加此行不会切换到另一个协程。此处用time.sleep()不能起到这个作用。

        greeting = await websocket.recv()
        #正常地接受，此协程未挂起
        print("receive"+greeting)


async def hello(websocket, path):
        a = asyncio.get_event_loop().create_task(send(websocket))
        b = asyncio.get_event_loop().create_task(receive(websocket))
        #使用create_task()创建task

        await a
        await b
        # ab并发


start_server = websockets.serve(hello, "localhost", 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
