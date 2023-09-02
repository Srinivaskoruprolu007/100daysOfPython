from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Verdana', 24, 'normal'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.ht()

    def update_score(self):
        self.write(arg=f"score : {self.score}", font=FONT,  align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over ! Your score: {self.score}", font=FONT, align=ALIGNMENT)
