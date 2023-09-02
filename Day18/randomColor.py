import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = r, g, b
    return color


directions = [0, 98, 188, 278]
tim.pensize(15)
tim.speed("fastest")

for _ in range(1000):
    tim.color(random_color())
    tim.fd(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()