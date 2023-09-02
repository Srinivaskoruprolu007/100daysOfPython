from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(6):
    timmy = Turtle('turtle')
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won and {user_bet} color turtle won the race.")
            else:
                print(f"You lose. {winning_color} tutle is won the race.")
            is_race_on = False
        ran_motion = random.randint(0, 10)
        turtle.fd(ran_motion)

screen.exitonclick()

