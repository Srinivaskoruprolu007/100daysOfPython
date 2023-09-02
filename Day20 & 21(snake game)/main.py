import time
from turtle import Screen

from Food import Food
from ScoreBoard import ScoreBoard
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

my_snake = Snake()
food = Food()
score_card = ScoreBoard()

screen.listen()
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # detect collision with food
    if my_snake.head.distance(food) < 17:
        food.refresh()
        my_snake.extend()
        score_card.increase_score()

    # detect collision with wall.
    if my_snake.head.xcor() > 290 or my_snake.head.ycor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() < -290:
        is_game_on = False
        score_card.game_over()

    # detect collision with tail.
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 13:
            is_game_on = False
            score_card.game_over()


screen.exitonclick()

