import turtle
t = turtle.Turtle()
w = turtle.Screen()

def drawSprial(l):
    if l > 0:
        t.forward(l)
        t.right(90)
        drawSprial(l-2)

drawSprial(200)
w.exitonclick()
