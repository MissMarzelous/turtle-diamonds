# PROGRAMMER:  Marlena Fabrick
# PROGRAM NAME: Double Diamond Graphic Design
# PURPOSE:      Uses Python turtle graphics to draw two overlapping
#               diamonds with circles and a caption label.

import turtle


def setup_screen():
    """Sets up the turtle screen."""
    screen = turtle.Screen()
    screen.bgcolor("light grey")
    screen.title("Double Diamond Graphic Design")
    return screen


def setup_pen():
    """Creates and configures the turtle pen."""
    pen = turtle.Turtle()
    pen.speed(10)
    pen.shape("turtle")
    pen.width(5)
    pen.pencolor("purple")
    return pen


def draw_circle(pen, x, y, radius, fill_color):
    """Draws a filled circle at the given screen position."""
    pen.fillcolor(fill_color)
    pen.begin_fill()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(radius)
    pen.end_fill()


def main():
    setup_screen()
    pen = setup_pen()

    # Get radius value from user
    radius_value = turtle.numinput(
        "Radius Input",
        "Enter a numerical value for the circle radius:",
        default=50, minval=10, maxval=150
    )

    # Rotate pen to create diagonal diamond orientation
    # exactly as in the original program
    pen.right(135)

    # Draw first diamond (cyan) turning right
    pen.fillcolor("cyan")
    pen.begin_fill()
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.end_fill()

    # Draw second diamond (yellow) turning left
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.end_fill()

    pen.hideturtle()

    # Draw two circles using the user-entered radius
    draw_circle(pen, -170, 30, radius_value, "green")
    draw_circle(pen, 120,  30, radius_value, "white")

    # Write caption label
    pen.penup()
    pen.goto(-50, -200)
    pen.pendown()
    pen.write("DIAMOND", font=("Times New Roman", 30, "bold"))

    turtle.done()


main()
