import turtle
t = turtle.Turtle()
w = turtle.Screen()


def drawSpiral(angle, itr=10):
    for i in range(itr):
        t.forward(i)
        t.right(angle)
        # if itr > 0:
        #     drawSpiral(45, itr-10)


if __name__ == '__main__':
    drawSpiral(90, 100)
    drawSpiral(45)

    w.exitonclick()
