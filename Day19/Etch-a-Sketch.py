import turtle as t

timmy = t.Turtle()
screen = t.Screen()


def forward():
    timmy.fd(50)


def backward():
    timmy.bk(50)


def turn_left():
    new_heading = timmy.heading()+10
    timmy.seth(new_heading)


def turn_right():
    new_heading = timmy.heading()-10
    timmy.seth(new_heading)


def clear():
    screen.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(fun=clear, key='c')
screen.exitonclick()



