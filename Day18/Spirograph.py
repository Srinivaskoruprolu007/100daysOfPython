import turtle as t  # Import the turtle module, and alias it as 't' for ease of use.
import random       # Import the random module to generate random numbers.

# Create a turtle object named 'timmy'
timmy = t.Turtle()

# Set the color mode to 255 to allow RGB values for turtle colors
# This changes the color scheme to accept (R, G, B) values between 0-255.
t.colormode(255)

# Set the turtle speed to the fastest. 'fastest' is the highest speed setting for drawing.
timmy.speed('fastest')

# Define a function to generate and return a random color (R, G, B) values
def random_color():
    r = random.randint(0, 255)  # Generate a random integer for red (R) between 0 and 255
    g = random.randint(0, 255)  # Generate a random integer for green (G) between 0 and 255
    b = random.randint(0, 255)  # Generate a random integer for blue (B) between 0 and 255
    return r, g, b  # Return the generated RGB color as a tuple

# Define a function to draw a spirograph pattern
# size_of_gap determines the angle between consecutive circles
def spirograph(size_of_gap):
    # Loop through and draw circles, rotating by 'size_of_gap' each time
    for _ in range(360 // size_of_gap):  # 360//size_of_gap gives how many circles to draw in full rotation
        timmy.color(random_color())      # Set the turtle's color to a random color for each circle
        timmy.circle(100)                # Draw a circle with a radius of 100 units
        # Increment the turtle's heading (direction) by 'size_of_gap' degrees
        timmy.setheading(timmy.heading() + size_of_gap)

# Call the spirograph function with a gap of 5 degrees
spirograph(5)

# Create a screen object that keeps the window open
screen = t.Screen()
# The window will only close when the user clicks on the screen
screen.exitonclick()