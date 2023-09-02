from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]

    def create_snake(self):
        """ Creating a snake model """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle('square')
        timmy.penup()
        timmy.color('white')
        timmy.goto(position)
        self.segments.append(timmy)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Let the snake move 20 units of distance"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
            self.move()



