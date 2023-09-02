from turtle import Turtle, Screen

sam = Turtle()
sam.shape('square')
sam.color('yellow')
# Triangle


def triangle():
    for t in range(3):
        sam.fd(100)
        sam.lt(120)


triangle()
# square
sam.back(100)


def square():
    for i in range(4):
        sam.fd(100)
        sam.lt(90)


square()

# dashed_line
for i in range(10):
    sam.bk(5)
    sam.penup()
    sam.bk(5)
    sam.pendown()


screen = Screen()
screen.exitonclick()
