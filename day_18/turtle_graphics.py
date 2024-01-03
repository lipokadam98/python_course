import turtle as t
from turtle import Turtle

import heroes


def draw_square(size: int):
    for i in range(4):
        tim.forward(size)
        tim.left(90)


def draw_dashed_line():
    for i in range(30):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


tim = Turtle()

tim.shape("turtle")
tim.color("coral2")
print(heroes.gen())
draw_square(100)
draw_dashed_line()
screen = t.Screen()
screen.exitonclick()
