import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle named "pen"
pen = turtle.Turtle()

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.right(90)
# Close the turtle graphics window on click
screen.exitonclick()
