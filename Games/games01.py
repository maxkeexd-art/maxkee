# filename: simple_square.py

import turtle

def draw_square():
    """Draws a simple red square using turtle graphics."""

    # 1. Setup the screen (ສ້າງໜ້າຈໍ)
    screen = turtle.Screen()
    screen.setup(width=600, height=600) # Set window size
    screen.bgcolor("lightblue") # Set background color
    screen.title("Python Turtle - Simple Square")

    # 2. Create a turtle object (ສ້າງ turtle)
    pen = turtle.Turtle()
    pen.shape("turtle") # You can see a little turtle icon
    pen.color("red")    # Set the turtle's drawing color to red
    pen.pensize(5)      # Set the line thickness
    pen.speed(1)        # Set the drawing speed (1=slowest, 10=fastest, 0=instant)

    # 3. Draw the square (ແຕ້ມຮູບສີ່ຫຼ່ຽມ)
    # A square has 4 sides, and each corner is 90 degrees
    for _ in range(4): # Loop 4 times for 4 sides
        pen.forward(150) # Move forward by 150 units
        pen.right(90)    # Turn right by 90 degrees

    # 4. Keep the window open until closed manually (ປິດໜ້າຈໍ)
    # This ensures the window doesn't disappear immediately after drawing.
    screen.exitonclick()

# Run the drawing function
if  _ == "_main_":
    draw_square()