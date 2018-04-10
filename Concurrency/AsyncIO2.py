import asyncio
import turtle




def drawSpiral(itr,angle):
    t = turtle.Turtle()
    for i in range(itr):
        t.forward(i)
        t.right(angle)

async def coroutine1(counter,angle):
    print('Started Corutine with ',counter,angle)
    await drawSpiral(counter,angle)
    print('End Corutine with ', counter, angle)

async def helloWorld(str1):
    print("Hello ",str1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # tasks = loop.create_task([coroutine1(100,90),coroutine1(100,45)])
    # loop.run_until_complete(asyncio.gather(coroutine1(100,90),coroutine1(100,45)))

    loop.run_until_complete(helloWorld('Sandeep'))

    loop.close()