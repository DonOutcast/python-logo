import turtle
from turtle import *


def curve() -> None:
    """For a drawing python logo

    This function draws the first part

    """
    for i in range(50):
        forward(0.5)
        right(1)

    for i in range(80):
        forward(2)
        right(1)

    for i in range(50):
        forward(0.5)
        right(1)


def line() -> None:
    """For drawing python logo

    This function drawing line

    """
    forward(130)
    left(90)
    forward(10)
    left(90)
    forward(90)
    right(90)
    forward(30)


def semicircle_right() -> None:
    """For drawing python logo

    This function drawing semicircle in position right

    """
    for i in range(90):
        forward(0.5)
        right(1)


def semicircle_left() -> None:
    """For drawing pytho logo

    This function drawing semicircle in position left

    """
    for i in range(90):
        forward(0.5)
        left(1)


def draw_logo() -> None:
    # init map
    title("Python")
    Screen().bgcolor('black')
    turtle.TurtleScreen._RUNNING=True
    shape('turtle')
    shapesize(2)
    color('#4584b6')
    fillcolor('#4584b6')
    speed(100)

    # for blue part
    begin_fill()
    penup()
    goto(-70, 20)
    left(180)
    pendown()
    forward(10)
    curve()
    line()
    curve()
    forward(80)
    semicircle_right()
    forward(120)
    semicircle_left()
    forward(72.7)
    right(90)
    right(1)
    forward(19)
    end_fill()

    # for yellow part
    penup()
    goto(160, 186)
    right(180)
    pendown()
    pencolor("#ffde57")
    fillcolor("#ffde57")
    begin_fill()
    forward(10)
    curve()
    line()
    curve()
    forward(80)
    semicircle_right()
    forward(120)
    semicircle_left()
    forward(72.7)
    right(90)
    forward(19)
    end_fill()

    # for white circle
    penup()
    goto(-20, 210)
    pendown()
    pencolor("white")
    fillcolor("white")
    begin_fill()
    circle(10)
    end_fill()
    pencolor('blue')
    penup()
    goto(110, -30)
    pendown()
    pencolor('white')
    fillcolor('white')
    begin_fill()
    circle(10)
    end_fill()
    hideturtle()
    done()


draw_logo()

if __name__ == "__main__":
    draw_logo()
