from turtle import Turtle, Screen

sam = Turtle()
sam.shape('square')
sam.color('yellow')

# Function to draw a triangle
def triangle():
    for t in range(3):
        sam.fd(100)
        sam.lt(120)


triangle()

# Move the turtle back to start drawing the square
sam.back(100)

# Function to draw a square
def square():
    for i in range(4):
        sam.fd(100)
        sam.lt(90)


square()

# Move the turtle to a different position to start the dashed line
sam.penup()
sam.goto(-200, 0)  # Move turtle to a new position
sam.pendown()

# Draw a dashed line
for i in range(10):
    sam.fd(5)
    sam.penup()
    sam.fd(5)
    sam.pendown()

# Set up the screen to exit on click
screen = Screen()
screen.exitonclick()
