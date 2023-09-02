import turtle as t


timmy = t.Turtle()
screen = t.Screen()


def move_forward():
    timmy.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

