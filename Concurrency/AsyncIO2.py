import asyncio
import turtle


def drawSpiral(itr, angle):
    t = turtle.Turtle()
    # w = turtle.Screen()
    for i in range(itr):
        t.forward(i)
        t.right(angle)

    # w.exitonclick()
    # asyncio.sleep(1)


async def CoRoutine1(counter, angle):
    print('Started Corutine with ', counter, angle)
    drawSpiral(counter, angle)
    print('End Corutine with ', counter, angle)


async def CoRoutine2(counter, angle):
    print('Started Corutine with ', counter, angle)
    await CoRoutine1(100, 45)
    print('End Corutine with ', counter, angle)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # tasks = loop.create_task([coroutine1(100,90),coroutine1(100,45)])
    loop.run_until_complete(
        asyncio.gather(CoRoutine1(10, 90), CoRoutine2(10, 45)))

    loop.close()
