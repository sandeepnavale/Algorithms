import turtle
<<<<<<< HEAD
import asyncio
=======
>>>>>>> 402f9d971917be256908a5b3236a7076ba02b2c7

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

<<<<<<< HEAD
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
=======
def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()
>>>>>>> 402f9d971917be256908a5b3236a7076ba02b2c7
