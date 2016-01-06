# Madison Thorburn-Gundlach
# Due September 13, 2015
# Draw a polygon with input sides.  Prompt for color of interior.

import turtle
# input
sides_int = int(input("Think of a polygon.  How many sides does it have?\n"))
inside_color = input("What color would you like it to be colored: black, red, blue, purple, blank\n")

# calculate degrees to turn
turn_int = 360/sides_int

# program color
if inside_color == "":
    turtle.pencolor("black")
else:
    turtle.pencolor(inside_color)

# draw
turtle.pendown()
if inside_color != "":
    turtle.fillcolor(inside_color)
    turtle.begin_fill()
    for side in range (sides_int):
       turtle.forward(100)
       turtle.right(turn_int)
    turtle.end_fill()
else:
    for side in range (sides_int):
        turtle.forward(100)
        turtle.right(turn_int)
turtle.penup()
