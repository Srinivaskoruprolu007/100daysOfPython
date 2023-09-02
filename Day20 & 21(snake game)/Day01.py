# create snake body and control the snake
from turtle import Turtle, Screen
import time

# set up a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# snake body using turtle
x_cor = [0, 20, -20]
segments = []
for i in range(3):
    timmy = Turtle()
    timmy.penup()
    timmy.shape('square')
    timmy.color('white')
    timmy.goto(x=x_cor[i], y=0)
    segments.append(timmy)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()