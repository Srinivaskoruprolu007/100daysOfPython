import turtle as t  # Import the turtle module and alias it as 't'.
import random       # Import the random module to randomly select colors.

# Set up the turtle screen
screen = t.Screen()      # Create a screen object.
screen.bgcolor(0, 0, 0)  # Set the background color to black using RGB values (0, 0, 0).
t.colormode(255)         # Set color mode to 255 to allow RGB values.

# Create a turtle object named 'timmy'
timmy = t.Turtle()
timmy.speed("fastest")   # Set the turtle's speed to the fastest.
timmy.penup()            # Lift the pen so that the turtle doesn't draw lines between the dots.
timmy.ht()               # Hide the turtle's shape for a cleaner appearance.

# Define a list of colors in RGB format
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), 
              (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
              (255, 0, 255), (255, 110, 0), [200, 200, 9]]  # Colors are chosen for the dots.

# Move the turtle to the starting position
timmy.setheading(225)    # Set the heading to 225 degrees (diagonal).
timmy.fd(300)            # Move the turtle forward by 300 units.
timmy.seth(0)            # Set the heading to 0 degrees (pointing right).

# Define the number of dots to be drawn
number_of_dots = 100     # Draw 100 dots in total.

# Loop to create the dot pattern
for dots in range(1, number_of_dots):
    timmy.dot(20, random.choice(color_list))  # Draw a dot of size 20 with a random color from color_list.
    timmy.fd(50)  # Move the turtle forward by 50 units after drawing each dot.

    # Move to the next row after drawing 10 dots
    if dots % 10 == 0:
        timmy.seth(90)    # Set the heading to 90 degrees (pointing up).
        timmy.forward(58) # Move forward by 58 units (spacing between rows).
        timmy.seth(180)   # Set the heading to 180 degrees (pointing left).
        timmy.forward(500) # Move back to the start of the next row.
        timmy.setheading(0) # Set the heading back to 0 degrees (pointing right).

# Keep the turtle window open until a user clicks on it
screen.exitonclick()