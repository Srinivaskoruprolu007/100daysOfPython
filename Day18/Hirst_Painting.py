import turtle as t
import random

screen = t.Screen()
screen.bgcolor(0, 0, 0)
t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.ht()
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
       (222, 201, 136), (53, 93, 123), (255, 0, 255), (255, 110, 0), [200, 200, 9]]

timmy.setheading(225)
timmy.fd(300)
timmy.seth(0)
number_of_dots = 100

for dots in range(1, number_of_dots):
    timmy.dot(20, random.choice(color_list))
    timmy.fd(50)

    if dots % 10 == 0:
        timmy.seth(90)
        timmy.forward(58)
        timmy.seth(180)
        timmy.forward(500)
        timmy.setheading(0)


screen.exitonclick()