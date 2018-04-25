import turtle
import asyncio

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

async def drawSpiral( lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        # await asyncio.sleep(0.005)
        drawSpiral(lineLen-5)
    await asyncio.sleep(0.005)

async def draw():
    asyncio.gather(drawSpiral(100),drawSpiral(200))
    myWin.exitonclick()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(draw())
    loop.close()
