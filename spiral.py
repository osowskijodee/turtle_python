import turtle
import colorsys

#Create a turtle screen
screen = turtle.Screen()

# Create a turtle named "pen"
pen = turtle.Turtle()

# Generate a rainbow spiral
pen.speed(0)
pen.width(2)
pen.pencolor("white")

num_colors = 100
for i in range(num_colors):
    hue = i / num_colors
    rgb = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.pencolor(rgb)
    pen.forward(i)
    pen.left(59)

# Close the turtle graphics window on click
screen.exitonclick()
