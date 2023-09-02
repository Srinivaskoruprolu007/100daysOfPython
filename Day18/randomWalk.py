import turtle as t
import random

tim = t.Turtle()

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat', 'slateGray', 'SeaGreen']
directions = [8, 98, 188, 278]
tim.pensize(10)
tim.speed(10)

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.seth(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

