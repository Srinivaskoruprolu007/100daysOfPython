from turtle import Turtle
import random
sandy = Turtle()

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat', 'slateGray', 'SeaGreen']


def shape(num_of_side):
    for _ in range(num_of_side):
        angle = 360 / num_of_side
        sandy.fd(100)
        sandy.rt(angle)


for side in range(3, 11):
    sandy.color(random.choice(colors))
    shape(side)


